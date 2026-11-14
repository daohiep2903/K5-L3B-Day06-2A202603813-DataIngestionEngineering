"""Run preparation without services, then dev and frozen test separately."""
import argparse
from dataclasses import asdict
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import time
from datetime import datetime, timezone
from .models import DocumentPage
from .chunking import fixed_size, by_paragraph
from .evaluation import evaluate_query, summarize

ROOT = Path(__file__).resolve().parents[2]


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--split", choices=["dev", "test"], default="dev")
    parser.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    parser.add_argument("--revision", help="Optional pinned Hugging Face model commit")
    parser.add_argument("--backend", choices=["qdrant", "pgvector"], default="qdrant")
    args = parser.parse_args()
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    source_path = ROOT / "data/oauth2_sections_2_to_7.txt"
    text = source_path.read_text(encoding="utf-8")
    units = [json.loads(line) for line in (ROOT / "data/corpus_units.jsonl").read_text(encoding="utf-8").splitlines()]
    if len(units) < 30 or any(len(u["text"].strip()) < 1500 for u in units):
        raise ValueError("Corpus does not meet source-unit requirements")
    if "".join(u["text"] for u in units) != text:
        raise ValueError("Corpus differs from source")
    headings = list(re.finditer(r"^(\d+)(?:\.\d+)*\.  .+$", text, re.M))
    pages = []
    for unit in units:
        section = [h.group(1) for h in headings if h.start() <= unit["char_start"]][-1]
        pages.append(DocumentPage(unit["document_id"],unit["source"],unit["page"],unit["text"],dict(unit["metadata"],char_start=unit["char_start"],top_level_section=section)))
    strategies = {"A": [c for p in pages for c in fixed_size(p,500,50)], "B": [c for p in pages for c in by_paragraph(p,1000)]}
    strategies["C"] = strategies["B"]
    for chunks in strategies.values():
        assert len({c.chunk_id for c in chunks}) == len(chunks)
        for c in chunks:
            assert text[c.metadata["char_start"]:c.metadata["char_end_exclusive"]] == c.text
            assert len(c.text) <= (500 if chunks is strategies["A"] else 1000)
    stats = {s: {"chunk_count":len(cs),"characters":sum(len(c.text) for c in cs),"min_length":min(len(c.text) for c in cs),"max_length":max(len(c.text) for c in cs)} for s,cs in strategies.items()}
    save(out / "chunk_stats.json",stats)
    for strategy,chunks in strategies.items():
        (out / f"chunks_{strategy}.jsonl").write_text("".join(json.dumps(asdict(c))+"\n" for c in chunks),encoding="utf-8")
    print(json.dumps(stats,indent=2))
    if args.prepare_only:
        print("Preparation validated. No embeddings or retrieval metrics generated.")
        return
    from dotenv import load_dotenv
    from .embeddings import MyEmbedder
    load_dotenv(ROOT / "starter/.env")
    url = os.getenv("DATABASE_URL")
    if args.backend == "pgvector" and not url:
        raise ValueError("DATABASE_URL missing; configure starter/.env")
    benchmark_path = ROOT / "benchmark/questions.jsonl"
    code_hash = hashlib.sha256(b''.join(p.read_bytes() for p in sorted(Path(__file__).parent.glob('*.py')))).hexdigest()
    identity = {"source_sha256":hashlib.sha256(source_path.read_bytes()).hexdigest(),"benchmark_sha256":hashlib.sha256(benchmark_path.read_bytes()).hexdigest(),"code_sha256":code_hash,"model":args.model,"revision":args.revision,"backend":args.backend,"chunk_stats":stats}
    if args.split == "test":
        frozen = json.loads((out / "dev_selection.json").read_text(encoding="utf-8"))
        if frozen["identity"] != identity:
            raise ValueError("Test settings differ from frozen dev run")
    embedder = MyEmbedder(args.model,args.revision)
    token_audit = {}
    for strategy, chunks in strategies.items():
        lengths = [len(embedder.model.tokenizer.encode(c.text, truncation=False)) for c in chunks]
        token_audit[strategy] = {"max_tokens":max(lengths), "total_tokens":sum(lengths), "model_max_seq_length":embedder.model.max_seq_length, "truncated_chunks":sum(n > embedder.model.max_seq_length for n in lengths)}
    save(out / f"token_audit_{args.split}.json",token_audit)
    if args.backend == "pgvector":
        from .store import PgVectorStore
        store = PgVectorStore(url,embedder.dimensions)
    else:
        from .local_store import LocalVectorStore
        store = LocalVectorStore(ROOT / "local_vectors",embedder.dimensions)
    store.create_schema()
    timings = {}
    vectors = {}
    for strategy in ["A","B","C"]:
        started = time.perf_counter()
        if strategy != "C":
            vectors[strategy] = embedder.embed_documents([c.text for c in strategies[strategy]])
        else:
            vectors[strategy] = vectors["B"]
        store.upsert(strategy,strategies[strategy],vectors[strategy])
        first = store.count(strategy)
        store.upsert(strategy,strategies[strategy],vectors[strategy])
        if first != store.count(strategy) or first != len(strategies[strategy]):
            raise ValueError("Re-ingestion duplicate check failed")
        timings[strategy] = time.perf_counter()-started
    questions = [json.loads(line) for line in benchmark_path.read_text(encoding="utf-8").splitlines()]
    traces = []
    for question in questions:
        if question["split"] != args.split:
            continue
        query = embedder.embed_query(question["question"])
        for strategy in strategies:
            started = time.perf_counter()
            hits = store.search(strategy,query,filters=question.get("filter") if strategy == "C" else None)
            trace = evaluate_query(question,hits)
            traces.append(dict(trace,strategy=strategy,retrieval_seconds=time.perf_counter()-started))
    (out / f"traces_{args.split}.jsonl").write_text("".join(json.dumps(t)+"\n" for t in traces),encoding="utf-8")
    metrics = summarize(traces)
    save(out / f"metrics_{args.split}.json",metrics)
    save(out / f"run_{args.split}.json",dict(identity,completed_at_utc=datetime.now(timezone.utc).isoformat(),dimensions=embedder.dimensions,ingest_seconds_including_reingest=timings,provider="local sentence-transformers",service_cost=0,search="exact cosine",packages={p:importlib.metadata.version(p) for p in ["sentence-transformers","torch", "qdrant-client" if args.backend == "qdrant" else "psycopg"]}))
    if args.split == "dev":
        selected = sorted(metrics,key=lambda r:(-r["hit3"],-r["hit1"],stats[r["strategy"]]["chunk_count"],r["strategy"]))[0]["strategy"]
        save(out / "dev_selection.json",{"identity":identity,"selected_strategy":selected,"rule":"dev Hit@3, Hit@1, fewer chunks, alphabetical tie"})
    print(json.dumps(metrics,indent=2))
    if hasattr(store, "close"):
        store.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        import traceback
        errors = ROOT / "results/errors.log"
        errors.parent.mkdir(exist_ok=True)
        with errors.open('a', encoding='utf-8') as stream:
            stream.write(f"{datetime.now(timezone.utc).isoformat()} {type(error).__name__}: {error}\n")
        traceback.print_exc()
        raise SystemExit(1)
