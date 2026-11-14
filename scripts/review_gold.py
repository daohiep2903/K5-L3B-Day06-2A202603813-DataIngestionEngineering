"""Record a post-run AI gold review without changing the frozen benchmark."""
import hashlib
import json
from pathlib import Path
from starter.src.evaluation import evaluate_query, summarize

ROOT = Path(__file__).resolve().parents[1]
REASONS = [
    'Section 2.2 explicitly states both non-secret status and prohibition on authentication with the identifier alone.',
    'Section 2.3 prohibits more than one authentication method per request; at most one preserves that wording.',
    'Section 2.3.1 requires HTTP Basic support specifically for clients issued a client password; the question retains this condition.',
    'Section 2.3.1 restricts these credential parameters to the body and prohibits the request URI. The source also discourages this method; the answer concerns placement only.',
    'Primary section 2.3.1 evidence supports brute-force protection for client-password authentication. Alternative section 4.3.2 concerns resource-owner password credentials and is a different authentication context.',
    'Primary section 3.1 evidence supports the authorization endpoint rule. Alternatives 3.1.2 and 3.2 concern redirect and token endpoints, respectively, so they are not evidence about the endpoint named in the question.',
    'Section 3.2 explicitly requires POST for access token requests.',
    'Section 4.1.2 recommends a maximum code lifetime of ten minutes. It is RECOMMENDED, not a universal MUST. The extracted quote ends in an incomplete following sentence; the answer-bearing recommendation itself is complete.',
    'Section 4.2.2 prohibits refresh tokens; its heading and surrounding context establish the implicit grant.',
    'Section 4.3.1 requires discarding resource-owner credentials once an access token is obtained.',
    'Section 4.4 restricts the client credentials grant to confidential clients.',
    'Section 5.1 specifies both Cache-Control: no-store and Pragma: no-cache for sensitive responses.',
    'Section 5.2 defines invalid_grant and explicitly includes expired or revoked grants and refresh tokens.',
    'Section 6 requires discarding and replacing the old token when a new refresh token is issued; this condition is present in the question.',
    'Section 7.1 prohibits using a token whose type the client does not understand.',
    'Section 2.2 leaves size undefined and says clients should avoid identifier-size assumptions.',
    'Primary section 3.1 evidence prohibits duplicate authorization request parameters. Alternative section 3.2 is about token endpoint requests and does not by itself establish the authorization endpoint rule.',
    'Section 6 explicitly requires identical scope when a replacement refresh token is issued.',
    'Section 7 explicitly states validation, expiration and scope checks by the resource server, distinct from authorization server client authentication.',
    'Section 5.1 explicitly requires ignoring unrecognized response value names.',
]


def main():
    path = ROOT / 'benchmark/questions.jsonl'
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    questions = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
    text = (ROOT / 'data/oauth2_sections_2_to_7.txt').read_text(encoding='utf-8')
    units = {u['page']: u for u in map(json.loads, (ROOT / 'data/corpus_units.jsonl').read_text(encoding='utf-8').splitlines())}
    flagged = {'q05', 'q06', 'q08', 'q17'}
    reviewed = []
    for q, reason in zip(questions, REASONS):
        for gold in q['gold_evidence']:
            assert text[gold['char_start']:gold['char_end_exclusive']] == gold['evidence_quote']
            assert gold['evidence_quote'] in units[gold['gold_page']]['text']
        reviewed.append({'id': q['id'], 'expected_answer_supported': True,
                         'status': 'gold_annotation_issue' if q['id'] in flagged else 'pass',
                         'reason': reason, 'reviewer': 'AI',
                         'method': 'Direct reading of question, answer, all quoted alternatives and source context; exact source offsets also verified.',
                         'student_personally_confirmed': False})
    # Sensitivity analysis only: remove the context-inappropriate alternative golds.
    # Do not rewrite benchmark, original traces, metrics or selection.
    keep_sections = {'q05': {'2.3.1'}, 'q06': {'3.1'}, 'q17': {'3.1'}}
    traces = []
    for split in ['dev', 'test']:
        for t in map(json.loads, (ROOT / f'results/traces_{split}.jsonl').read_text(encoding='utf-8').splitlines()):
            q = next(q for q in questions if q['id'] == t['id'])
            q = dict(q)
            if q['id'] in keep_sections:
                q['gold_evidence'] = [g for g in q['gold_evidence'] if g['section'] in keep_sections[q['id']]]
            traces.append(dict(evaluate_query(q, t['hits']), strategy=t['strategy']))
    result = {'reviewer': 'AI', 'timing': 'post-run review; not independent human validation',
              'benchmark_sha256': before, 'questions_reviewed': len(reviewed),
              'answers_supported': sum(r['expected_answer_supported'] for r in reviewed),
              'annotation_issues': len(flagged), 'reviews': reviewed,
              'sensitivity_analysis': {'method': 'Reuse original retrieval traces; remove context-inappropriate alternative golds for q05, q06, q17 only. q08 incomplete quote left unchanged.',
                                       'metrics': summarize(traces)}}
    acknowledgment = ROOT / 'benchmark/student_acknowledgment.json'
    if acknowledgment.exists():
        result['student_acknowledgment'] = json.loads(acknowledgment.read_text(encoding='utf-8'))
    (ROOT / 'results/gold_ai_review.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before
    print(json.dumps({'reviewed': len(reviewed), 'answers_supported': 20, 'annotation_issues': 4,
                      'sensitivity_metrics': summarize(traces)}, indent=2))


if __name__ == '__main__':
    main()
