# Measured retrieval results

Real local all-MiniLM-L6-v2 embeddings (384 dimensions), persistent Qdrant local, exact cosine search. No paid API service was used. Model hashes, revision, package versions and full traces are stored beside this file.

| Strategy | Chunks | Dev Hit@1 | Dev Hit@3 | Test Hit@1 | Test Hit@3 |
|---|---:|---:|---:|---:|---:|
| A | 182 | 7/15 | 8/15 | 2/5 | 3/5 |
| B | 116 | 7/15 | 11/15 | 4/5 | 5/5 |
| C | 116 | 7/15 | 11/15 | 4/5 | 5/5 |

B was selected on dev before the test run. B and C tied, including chunk count, so the predeclared alphabetical tie-break selected B. Do not retune using these test results.

Limits: only five test questions; all questions come from one RFC and topics overlap. AI-authored gold answers require student review. Two B/C chunks exceed the model's 256-token limit and are truncated during embedding (maximum 271 tokens). A has no truncated chunks. The student confirmed checking and accepting the AI-assisted coherence, metadata and grounding audit on 2026-11-14; automatic Hit@3 is not a substitute. Excerpt redistribution terms were reviewed on 2026-11-13; see data/RIGHTS_REVIEW.md and keep the accompanying RFC6749_NOTICES.txt with this related dataset.

Automated trace checks: all 60 strategy/question traces contain three hits; C obeys every supplied filter. Dev B/C rankings match on questions without filters. Store integration verified filtering, cosine ordering, repeat ingestion, stale removal and persistence across reopening.

Example dev retrieval failures with A: q03, q05, q07, q08, q09, q12, q14. Inspect traces_dev.jsonl to analyze exact evidence cuts and ranking errors.

AI qualitative review is now available in coherence_ai_review.jsonl and grounding_ai_review.jsonl, with explicit reviewer identity and reasons. Metadata source/offset checks are in metadata_verification.json. The student subsequently confirmed checking these audit items; see student_audit_confirmation.json and the separate manual_review files. The original AI review records remain unchanged. See audit_summary.json and the individual report for interpretation, including A q18/q19 where strict quote matching misses answer-bearing evidence. Original retrieval metrics are unchanged.
