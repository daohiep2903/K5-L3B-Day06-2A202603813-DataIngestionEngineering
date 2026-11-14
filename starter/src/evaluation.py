"""Evidence retrieval metrics, independent of human audit labels."""
from collections import defaultdict


def evaluate_query(question, hits):
    golds = question.get("gold_evidence", [question])
    def match(hit):
        return any(hit["document_id"] == gold["gold_source_id"] and hit["page"] == gold["gold_page"]
                   and " ".join(gold["evidence_quote"].split()) in " ".join(hit["text"].split()) for gold in golds)
    labels = [match(hit) for hit in hits[:3]]
    return dict(question, hits=hits[:3], evidence_hits=labels, hit1=bool(labels and labels[0]), hit3=any(labels))


def summarize(traces):
    groups = defaultdict(list)
    for trace in traces:
        groups[(trace["strategy"], trace["split"])].append(trace)
    return [{"strategy": strategy, "split": split, "n": len(rows),
             "hit1_count": sum(r["hit1"] for r in rows), "hit3_count": sum(r["hit3"] for r in rows),
             "hit1": sum(r["hit1"] for r in rows)/len(rows), "hit3": sum(r["hit3"] for r in rows)/len(rows)}
            for (strategy, split), rows in sorted(groups.items())]
