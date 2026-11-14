# Benchmark RFC 6749

Source attribution: text evidence is extracted from IETF RFC 6749, D. Hardt (Ed.), October 2012. Source notices and redistribution conditions accompany this related dataset in `data/RFC6749_NOTICES.txt` and `data/RIGHTS_REVIEW.md`; include them when sharing extracted evidence separately.

`questions.jsonl`: 20 English questions, 15 dev / 5 test, authored before retrieval experiments. English matches the corpus language. Four questions explicitly name a section and supply a filter; two are in test. Each record contains an expected answer and exact evidence with source-unit and character offsets. `gold_evidence` includes all matching paragraphs found for the chosen evidence anchor; other valid equivalent evidence may still need documented review.

## Reproduce validation

From the repository root:

```powershell
python scripts/prepare_corpus.py
python scripts/prepare_benchmark.py
```

Validation checks exact evidence text, complete containment in one source unit, source offsets, split counts and filter counts. It does not measure retrieval quality or substitute for a student's review of whether each answer is fully supported. The questions and answers were authored with AI; independent human review is pending.

`page` / `gold_page` means a sequential corpus unit, not the original RFC page. The source file and zero-based character offsets provide traceability. Preserve the original supplied text, including its copyright notice.

## Split and selection rule

The fixed split is q01–q15 dev and q16–q20 test. Both sets draw from one document and share topics, so the holdout has topic leakage and only five examples. It illustrates within-document retrieval; it does not measure generalization to new documents. Test questions and gold are already visible during dataset preparation. Do not use test retrieval results to tune configurations; disclose this preparation context in the report.

Before running retrieval, fix model, corpus, cosine metric and these configurations: A fixed-size 500 characters with 50 overlap; B paragraph-aware with maximum 1000 characters; C exactly B with filters only for questions that explicitly supply them. If a paragraph exceeds the maximum, split it deterministically and retain offsets. Choose on dev by Evidence Hit@3, then Hit@1, then fewer stored chunks. Evaluate test only after that choice; report all three configurations on the same test.

## Filter semantics

`top_level_section` is the actual numbered RFC section containing the chunk text, such as `2` or `6`. Determine it from source heading offsets. Source units can cross sections: `metadata.top_level_sections` lists sections covered by the unit, but must not be copied as a scalar section label to every chunk. Split chunks at top-level section boundaries and attach the verified scalar `top_level_section`. Both B and C must use the same boundary handling. Never derive filters from gold evidence; the benchmark question itself supplies the section.

## Retrieval scoring and audit

A hit requires matching `document_id` and source-unit `page`, plus sufficient evidence in one retrieved chunk. Accept any entry in `gold_evidence`. Normalize whitespace consistently for matching, and document reviewed equivalent evidence. Save full top-3 traces and aggregate Hit@1 / Hit@3 separately by strategy and split, with numerators and denominators. Do not infer coherence or grounding labels from string matches.

Manual audit remains to be completed after retrieval: the same ten source locations for coherence, five test questions per strategy for grounding, and source/position/filter correctness for their top-3 results. No retrieval results or manual audit scores have been generated yet.
