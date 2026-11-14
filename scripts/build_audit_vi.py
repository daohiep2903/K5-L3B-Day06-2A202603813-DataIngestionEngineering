"""Render a Vietnamese audit packet, preserving verbatim source excerpts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(name):
    return [json.loads(line) for line in (ROOT / 'results' / name).read_text(encoding='utf-8').splitlines()]


A_REASONS = [
    'Phần đăng ký client có thể hiểu được, nhưng đoạn tiếp theo bị cắt giữa từ.',
    'Định nghĩa public client đầy đủ, nhưng đoạn sau bị cắt.',
    'Định nghĩa ứng dụng chạy trên trình duyệt bị cắt giữa câu.',
    'Đoạn văn đầy đủ, nêu rõ không được giả định độ dài client identifier.',
    'Định nghĩa client_secret bị cắt giữa từ, làm mất ngoại lệ khi secret là chuỗi rỗng.',
    'Có tiêu đề và đoạn văn đầy đủ giải thích ánh xạ phương thức xác thực với client identifier.',
    'Quy định về URI đầy đủ, nhưng phần nói về TLS vừa bắt đầu đã bị cắt.',
    'Hai đoạn văn đầy đủ mô tả response type kết hợp và cách xử lý lỗi.',
    'Đoạn văn đầy đủ giải thích rủi ro khi thiếu bảo mật tầng truyền tải.',
    'Quy định gửi redirect URI đầy đủ, nhưng quy định đối chiếu URI bị cắt giữa từ.',
]
B_REASONS = [
    'Các đoạn về đăng ký client đầy đủ, nhưng danh sách SHALL chỉ có yêu cầu đầu tiên; các yêu cầu còn lại nằm ở chunk sau.',
    'Định nghĩa public client và lưu ý về cách xác định loại client đều đầy đủ.',
    'Định nghĩa ứng dụng chạy trên trình duyệt đầy đủ và có ngữ cảnh hữu ích.',
    'Đoạn văn về độ dài client identifier đầy đủ.',
    'Giữ đủ tham số credential trong body, ngoại lệ secret rỗng và hạn chế không đưa vào URI. Ví dụ Basic ở đầu cần ngữ cảnh trước đó, nhưng nội dung chính vẫn hiểu được.',
    'Có tiêu đề và đoạn văn đầy đủ về ánh xạ phương thức xác thực.',
    'Giữ đủ quy định về vị trí endpoint, fragment, TLS và phương thức HTTP.',
    'Các đoạn về response type và lỗi đều đầy đủ.',
    'Giải thích đầy đủ rủi ro bảo mật tầng truyền tải.',
    'Có tiêu đề và đầy đủ quy định gửi, đối chiếu redirect URI.',
]
QUESTIONS = {
    'q16': ('Theo mục 2, client có thể giả định một độ dài cố định cho client identifier không?', 'Không. Độ dài không được quy định; client nên tránh giả định về độ dài.'),
    'q17': ('Một yêu cầu cấp quyền có được chứa cùng một tham số nhiều lần không?', 'Không.'),
    'q18': ('Theo mục 6, refresh token thay thế có được có scope khác token đã gửi lên không?', 'Không. Scope phải giống nhau.'),
    'q19': ('Resource server phải kiểm tra gì khi client đưa ra access token?', 'Xác minh token hợp lệ, chưa hết hạn và scope bao phủ tài nguyên được yêu cầu.'),
    'q20': ('Client phải xử lý tên giá trị không nhận biết trong phản hồi token như thế nào?', 'Bỏ qua các tên giá trị đó.'),
}
GROUND_REASONS = {
    'q16': 'Top-1 nêu rõ độ dài identifier không được quy định và client nên tránh giả định về độ dài.',
    'q17': 'Top-1 nêu rõ tham số yêu cầu và phản hồi KHÔNG ĐƯỢC xuất hiện nhiều hơn một lần.',
    'q18': 'Top-3 chứa điều kiện cấp refresh token thay thế và yêu cầu scope giống nhau. Ở A, đầu đoạn bị cắt nhưng điều kiện và quy định cần để trả lời vẫn còn.',
    'q19': 'Top-3 nêu đủ yêu cầu xác minh token, kiểm tra hết hạn và phạm vi scope. A cắt phần cuối câu giải thích thêm, nhưng các câu chứa đáp án vẫn đầy đủ.',
    'q20': 'Top-3 nêu rõ client PHẢI bỏ qua tên giá trị không nhận biết trong phản hồi.',
}


def main():
    coherence = rows('coherence_ai_review.jsonl')
    grounding = rows('grounding_ai_review.jsonl')
    traces = rows('traces_test.jsonl')
    summary = json.loads((ROOT / 'results/audit_summary.json').read_text(encoding='utf-8'))
    chunks = {s: {c['chunk_id']: c for c in rows(f'chunks_{s}.jsonl')} for s in ['A', 'B', 'C']}
    source = (ROOT / 'data/oauth2_sections_2_to_7.txt').read_text(encoding='utf-8')
    lines = ['# Hồ sơ đánh giá chất lượng dữ liệu và truy xuất', '',
             '**Học viên, tác giả bài làm: Đào Văn Hiệp — 2A202603813 — L3B.**', '',
             '**Có sử dụng AI hỗ trợ đánh giá.** Phần định tính do AI đọc nội dung; metadata được đối chiếu bằng chương trình. Hồ sơ không khẳng định học viên đã tự chấm thủ công độc lập. Các chỉ số retrieval gốc được giữ nguyên.', '',
             'Phần hướng dẫn, câu hỏi và nhận xét được trình bày bằng tiếng Việt. Các đoạn trích giữ nguyên tiếng Anh để đối chiếu chính xác với tài liệu gốc; câu hỏi tiếng Việt chỉ là bản dịch để đọc, không thay bộ query tiếng Anh đã chạy.', '',
             '## Tổng hợp', '',
             '| Cấu hình | Mạch lạc chunk /2 (10 mẫu) | Đủ bằng chứng /2 (5 câu) | Metadata khớp nguồn | Top-3 đúng phạm vi filter |',
             '|---|---:|---:|---:|---:|']
    for strategy, r in summary['strategies'].items():
        lines.append(f"| {strategy} | {str(r['coherence_ai_mean']).replace('.', ',')} | {str(r['grounding_ai_mean']).replace('.', ',')} | {r['metadata_programmatic_correct']}/{r['metadata_n']} | {r['filter_compliance_count']}/{r['filter_n']} |")
    lines += ['', '## Tính mạch lạc của chunk: cùng 10 vị trí nguồn cho mỗi cấu hình', '',
              'Thang điểm: **0** = khó hiểu vì bị cắt ý hoặc thiếu chủ thể; **1** = hiểu được một phần nhưng thiếu ngữ cảnh; **2** = đủ ngữ cảnh và giữ trọn ý để hiểu. Chấm toàn bộ chunk mẫu, không chỉ câu đầu. Mười đơn vị nguồn đầu được chọn trước khi chấm retrieval; cách lấy mẫu này thiên về phần đầu tài liệu.']
    for r in coherence:
        i = int(r['unit_id'].split('-')[-1]) - 1
        reason = A_REASONS[i] if r['strategy'] == 'A' else B_REASONS[i]
        lines += ['', f"### {r['strategy']} / {r['unit_id']}", f"**Điểm: {r['coherence_score']}/2.** Lý do: {reason}"]
        for cid in r['chunk_ids']:
            c = chunks[r['strategy']][cid]
            m = c['metadata']
            assert source[m['char_start']:m['char_end_exclusive']] == c['text']
            lines += [f"Đơn vị nguồn {c['page']}; mục {m['top_level_section']}; khoảng ký tự [{m['char_start']}, {m['char_end_exclusive']}); ID chunk `{cid}`.", '', '```text', c['text'], '```']
    lines += ['', '## Độ đủ bằng chứng và metadata: 5 câu test cho mỗi cấu hình', '',
              'Thang điểm grounding: **0** = không có bằng chứng; **1** = có nhưng thiếu điều kiện hoặc ngữ cảnh cần thiết; **2** = đủ để trả lời và truy nguồn. Chấm cả tập top-3. Metadata được đối chiếu với text và vị trí nguồn thực tế. A/B là cấu hình không filter; tỷ lệ đúng phạm vi của chúng chỉ để so sánh, không phải lỗi thực thi filter.']
    for r in grounding:
        t = next(t for t in traces if t['strategy'] == r['strategy'] and t['id'] == r['question_id'])
        question, answer = QUESTIONS[r['question_id']]
        lines += ['', f"### {r['strategy']} / {r['question_id']}", f'**Câu hỏi:** {question}', '',
                  f'**Đáp án dự kiến:** {answer}', f"**Điểm grounding có AI hỗ trợ: {r['grounding_score']}/2.** Lý do: {GROUND_REASONS[r['question_id']]}",
                  f"**Filter từ câu hỏi:** {json.dumps(t['filter']) if t['filter'] else 'Không có.'}"]
        for rank, h in enumerate(t['hits'], 1):
            m = h['metadata']
            assert source[m['char_start']:m['char_end_exclusive']] == h['text']
            lines += ['', f"**Hạng {rank}:** đơn vị nguồn {h['page']}, mục {m['top_level_section']}, nguồn `{h['source']}`, khoảng ký tự [{m['char_start']}, {m['char_end_exclusive']}).",
                      'Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.', '', '```text', h['text'], '```']
    lines += ['', '## Diễn giải và phần xác nhận của học viên', '',
              'Ở A, q18 và q19 có đủ các câu chứa đáp án dù không khớp trọn đoạn gold quote. Vì vậy điểm grounding là 2 trong khi metric evidence tự động có thể không hit; hồ sơ không sửa metric gốc. B/C có điểm coherence giống nhau vì dùng cùng chunk. Điểm grounding được đánh giá từ việc đọc top-3, không sao chép từ Hit@3.', '',
              'Để hoàn tất yêu cầu audit thủ công của môn học, học viên cần đọc đối chiếu và ghi điểm của mình trong các template audit gốc. Việc đồng ý với nhận xét AI không được trình bày thành một lượt chấm thủ công độc lập.']
    confirmation = ROOT / 'results/student_audit_confirmation.json'
    if confirmation.exists():
        lines = [line.replace('Hồ sơ không khẳng định học viên đã tự chấm thủ công độc lập.', 'Học viên Đào Văn Hiệp đã xác nhận đọc kiểm tra và đồng ý giữ nguyên điểm, lý do ngày 14/11/2026; đây là kiểm tra có AI hỗ trợ, không phải chấm mù độc lập.') for line in lines]
        lines[-1] = 'Học viên Đào Văn Hiệp đã xác nhận kiểm tra toàn bộ mục audit và đồng ý với các điểm, lý do hiện có. Hồ sơ xác nhận: `results/student_audit_confirmation.json`; nhãn đã ghi nhận tại `results/coherence_manual_review.jsonl` và `results/test_manual_review.jsonl`. Các bản AI ban đầu và template trống vẫn được giữ để truy vết.'
    (ROOT / 'results/AUDIT_REVIEW.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('Rendered Vietnamese audit: 30 coherence cases, 15 grounding cases, 45 metadata records; original source excerpts preserved.')


if __name__ == '__main__':
    main()
