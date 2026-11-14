"""Build traceable, paragraph-aligned source units, not embedding chunks."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'data/oauth2_sections_2_to_7.txt'


def main():
    text = SOURCE.read_text(encoding='utf-8')
    # Python Unicode character offsets into the UTF-8-decoded selected file.
    headings = list(re.finditer(r'^(\d+(?:\.\d+)*)\.  (.+)$', text, re.M))
    boundaries = [m.end() for m in re.finditer(r'\n\n', text)] + [len(text)]
    spans = []
    start = 0
    for end in boundaries:
        if len(text[start:end].strip()) >= 1500:
            spans.append([start, end])
            start = end
    if start < len(text):
        spans[-1][1] = len(text)
    records = []
    for index, (start, end) in enumerate(spans, 1):
        active = [h for h in headings if h.start() <= start]
        overlaps = ([active[-1]] if active else []) + [h for h in headings if start <= h.start() < end]
        sections = list(dict.fromkeys(h.group(1) for h in overlaps))
        records.append({
            'document_id': 'rfc6749', 'source': SOURCE.relative_to(ROOT).as_posix(),
            'page': index, 'unit_id': f'rfc6749-unit-{index:03d}',
            'char_start': start, 'char_end_exclusive': end,
            'normalized_characters': len(text[start:end].strip()),
            'metadata': {'sections': sections, 'top_level_sections': list(dict.fromkeys(s.split('.')[0] for s in sections)), 'language': 'en'},
            'text': text[start:end],
        })
    assert len(records) >= 30
    assert all(r['normalized_characters'] >= 1500 for r in records)
    assert ''.join(r['text'] for r in records) == text
    assert all(text[r['char_start']:r['char_end_exclusive']] == r['text'] for r in records)
    output = ROOT / 'data/corpus_units.jsonl'
    output.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    manifest = {
        'source_id': 'rfc6749', 'title': 'The OAuth 2.0 Authorization Framework',
        'source_path_or_url': 'data/data_tu_tim.txt',
        'source_url_stated_in_document': 'http://www.rfc-editor.org/info/rfc6749',
        'license_or_permission': 'IETF Trust Legal Provisions 4.0 (effective 2009-12-28), sections 3.c.iii and 3.d: attributed unmodified excerpts with original notices; not a blanket modification license. See data/RIGHTS_REVIEW.md and data/RFC6749_NOTICES.txt.',
        'rights_reviewed_at': '2026-11-13',
        'rights_sources': ['https://www.rfc-editor.org/rfc/rfc6749.html', 'https://trustee.ietf.org/documents/trust-legal-provisions/', 'https://trustee.ietf.org/wp-content/uploads/IETF-TLP-4.pdf'],
        'redistribution_notice_files': ['data/RFC6749_NOTICES.txt', 'results/RFC6749_NOTICES.txt'],
        'accessed_at': '2026-11-13', 'access_note': 'Local supplied copy inspected; no online source verification.',
        'selected_sections': ['2', '3', '4', '5', '6', '7'],
        'selected_source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'unit_count': len(records), 'physical_page_count': None,
        'counting_rule': 'Sequential non-overlapping units, >=1500 stripped Unicode characters each; end at paragraph boundaries; merge final short remainder. Not physical RFC pages.',
        'offset_convention': 'Zero-based Python Unicode offsets, end exclusive, into selected source read as UTF-8 with universal newlines.',
        'units': [{k: r[k] for k in ('unit_id', 'page', 'char_start', 'char_end_exclusive', 'normalized_characters')} for r in records],
    }
    (ROOT / 'data/manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Validated {len(records)} units; minimum {min(r['normalized_characters'] for r in records)} characters; exact complete coverage.")


if __name__ == '__main__':
    main()
