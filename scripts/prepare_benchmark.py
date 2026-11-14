"""Create and validate a fixed benchmark before retrieval experiments."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Each anchor identifies a source paragraph, not an embedding query.
# Filters come from the explicit section named in the question.
ITEMS = [
    ('The client identifier is not a secret', 'Is a client identifier secret, and can it authenticate a client alone?', 'It is not secret and MUST NOT be used alone for client authentication.', None),
    ('The client MUST NOT use more than one authentication method', 'How many authentication methods may a client use in one request?', 'At most one.', None),
    ('The authorization server MUST support the HTTP Basic', 'According to section 2, which authentication scheme must the server support for clients issued a client password?', 'HTTP Basic.', '2'),
    ('The parameters can only be transmitted', 'Where may client credentials supplied as body parameters be transmitted?', 'Only in the request body, never in the request URI.', None),
    ('against brute force attacks', 'What attack must endpoints using password client authentication protect against?', 'Brute force attacks.', None),
    ('endpoint URI MUST NOT include a fragment component', 'According to section 3, may the authorization endpoint URI contain a fragment?', 'No.', '3'),
    ('The client MUST use the HTTP "POST"', 'Which HTTP method must clients use for access token requests?', 'POST.', None),
    ('maximum authorization code lifetime of 10 minutes', 'What maximum authorization code lifetime is recommended?', '10 minutes.', None),
    ('The authorization server MUST NOT issue a refresh token.', 'May the authorization server issue a refresh token in the implicit grant?', 'No.', None),
    ('MUST discard the credentials once', 'When must a client discard resource owner credentials in the password credentials grant?', 'Once an access token has been obtained.', None),
    ('The client credentials grant type MUST only', 'Which client type is permitted to use the client credentials grant?', 'Confidential clients only.', None),
    ('value of "no-store"', 'Which cache-control headers are required in responses containing tokens or credentials?', 'Cache-Control: no-store and Pragma: no-cache.', None),
    ('invalid_grant', 'Which token error covers an expired or revoked authorization grant or refresh token?', 'invalid_grant.', None),
    ('the client MUST discard the old refresh token', 'What must a client do when the authorization server issues a replacement refresh token?', 'Discard the old refresh token and replace it with the new one.', None),
    ('MUST NOT use an access token if it does not understand', 'May a client use an access token whose token type it does not understand?', 'No.', None),
    ('The client identifier string size is left undefined', 'According to section 2, is there a fixed client identifier length that clients may assume?', 'No. The size is undefined; clients should avoid assumptions about it.', '2'),
    ('Request and response parameters MUST NOT be included more than once.', 'May an authorization request include the same parameter more than once?', 'No.', None),
    ('refresh token scope MUST be identical', 'According to section 6, may a replacement refresh token have a different scope from the submitted token?', 'No. Its scope MUST be identical.', '6'),
    ('resource server MUST validate the access token', 'What must a resource server verify when a client presents an access token?', 'Validate it, ensure it has not expired, and ensure its scope covers the requested resource.', None),
    ('The client MUST ignore unrecognized value names', 'How must a client handle unrecognized value names in a token response?', 'Ignore them.', None),
]


def normalized(text):
    return ' '.join(text.split())


def main():
    source = ROOT / 'data/oauth2_sections_2_to_7.txt'
    text = source.read_text(encoding='utf-8')
    units = [json.loads(line) for line in (ROOT / 'data/corpus_units.jsonl').read_text(encoding='utf-8').splitlines()]
    paragraphs = list(re.finditer(r'\S[^\n]*(?:\n(?![ \t]*\n)[^\n]*)*', text))
    headings = list(re.finditer(r'^(\d+(?:\.\d+)*)\.  (.+)$', text, re.M))
    questions = []
    for index, (anchor, question, answer, section_filter) in enumerate(ITEMS, 1):
        gold = []
        for paragraph in paragraphs:
            quote = paragraph.group().strip()
            if anchor not in normalized(quote):
                continue
            start = paragraph.start() + len(paragraph.group()) - len(paragraph.group().lstrip())
            end = start + len(quote)
            section = [h.group(1) for h in headings if h.start() <= start][-1]
            if section_filter and section.split('.')[0] != section_filter:
                continue
            containing = [u for u in units if u['char_start'] <= start and end <= u['char_end_exclusive']]
            if len(containing) != 1:
                raise ValueError(f'q{index:02d}: evidence crosses source unit boundary')
            unit = containing[0]
            assert text[start:end] == quote and quote in unit['text']
            gold.append({'gold_source_id': 'rfc6749', 'gold_page': unit['page'], 'unit_id': unit['unit_id'], 'section': section, 'evidence_quote': quote, 'char_start': start, 'char_end_exclusive': end})
        if not gold:
            raise ValueError(f'q{index:02d}: anchor not found: {anchor}')
        questions.append({'id': f'q{index:02d}', 'split': 'dev' if index <= 15 else 'test', 'question': question, 'expected_answer': answer,
                          'gold_source_id': gold[0]['gold_source_id'], 'gold_page': gold[0]['gold_page'], 'evidence_quote': gold[0]['evidence_quote'],
                          'gold_evidence': gold, 'filter': {'top_level_section': section_filter} if section_filter else None})
    assert len(questions) == 20
    assert sum(q['split'] == 'test' for q in questions) == 5
    assert sum(bool(q['filter']) for q in questions) >= 3
    assert any(q['filter'] and q['split'] == 'test' for q in questions)
    destination = ROOT / 'benchmark'
    destination.mkdir(exist_ok=True)
    output = destination / 'questions.jsonl'
    output.write_text(''.join(json.dumps(q, ensure_ascii=False) + '\n' for q in questions), encoding='utf-8')
    status = {'question_count': 20, 'dev': 15, 'test': 5, 'filter_questions': sum(bool(q['filter']) for q in questions),
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'benchmark_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
              'exact_evidence_verified': True, 'complete_unit_containment_verified': True, 'retrieval_experiments_run': False,
              'review_status': 'AI-authored and checked against local text; student review pending. No independent human audit claimed.'}
    (destination / 'validation.json').write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(status, indent=2))


if __name__ == '__main__':
    main()
