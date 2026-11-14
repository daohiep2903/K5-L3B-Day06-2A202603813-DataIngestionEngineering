# Run the RFC 6749 experiment

## Local Qdrant (default, no Docker)

From the repository root:

```powershell
python -m venv starter/.venv
starter/.venv/Scripts/python.exe -m pip install -r starter/requirements-local.txt
starter/.venv/Scripts/python.exe -m starter.src.run --split dev
starter/.venv/Scripts/python.exe -m starter.src.run --split test
```

Models are downloaded into `local_models/`; persistent vectors are in `local_vectors/`. Both are excluded from Git. This is a real Qdrant vector store using cosine search, not a custom SQLite search implementation. All A/B/C strategies use the same backend. The initial model download needs internet. To reproduce a specific run, use its recorded model revision and `results/dependencies.txt` when available.

The actual recorded run used a pinned local model. Reproduce from the repository root:

```powershell
python scripts/download_model.py
starter/.venv/Scripts/python.exe -m starter.src.run --model local_models/all-MiniLM-L6-v2 --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 --split dev
starter/.venv/Scripts/python.exe -m starter.src.run --model local_models/all-MiniLM-L6-v2 --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 --split test
```

From the repository root, validate preparation without external services:

```powershell
python scripts/prepare_corpus.py
python scripts/prepare_benchmark.py
python -m starter.src.run --prepare-only
```

The prepared outputs go to `results/`. Source units are accounting and traceability units; the pipeline splits each into smaller embedding chunks. Every numbered heading is a shared chunk boundary in A/B/C. A uses 500 characters with overlap 50; B uses paragraph-aware grouping up to 1000 characters; C reuses B's exact chunks and vectors and applies only the supplied question filters.

## Optional PostgreSQL backend

For PostgreSQL embedding and retrieval, install Docker Desktop and start it, then run from `starter/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
docker compose -p day6_student_starter up -d --wait
python scripts/check_setup.py
python -m src.run --backend pgvector --split dev
```

Default embedding: `sentence-transformers/all-MiniLM-L6-v2`, a real local English model. Its first download requires network access. There is no mock fallback. For reproducibility, pass `--revision` with a verified Hugging Face model commit on both dev and test; record that commit. Long inputs may be truncated by the model tokenizer, a limitation to inspect in failure analysis. Service cost is zero; hardware and download costs are not measured.

Review dev results and the recorded selection. Without changing corpus, benchmark, model or chunk settings, run:

```powershell
python -m src.run --backend pgvector --split test
```

Test refuses to run without the matching saved dev selection. Results include full top-3 traces, per-split metrics with counts, configuration hashes, package versions and timings. Store uses exact cosine search, persists in the Docker volume, and atomically replaces only this experiment's rows for each strategy. Each run reloads twice and checks row counts to detect duplication. The `day6_chunks` table is dedicated to this lab; ingestion replaces its current strategy snapshot. Do not share it with another experiment. Re-embedding a changed model requires re-ingestion; a dimensional mismatch fails explicitly.

PostgreSQL integration must be validated on a machine with that service; the recorded run used Qdrant local. Preparation output alone is not a retrieval benchmark. The student has confirmed checking and accepting the AI-assisted coherence, grounding and metadata audit; see results/student_audit_confirmation.json. Excerpt sharing conditions were reviewed in `data/RIGHTS_REVIEW.md`; include original notices with redistributed data and trace excerpts. AI-authored gold answers still require student review before final submission.
