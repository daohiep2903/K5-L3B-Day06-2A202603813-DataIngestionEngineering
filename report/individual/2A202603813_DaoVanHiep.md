# Báo cáo cá nhân — Day 6

Học viên: **Đào Văn Hiệp** · MSSV: **2A202603813** · Lớp: **L3B**

Chủ đề: Truy xuất tài liệu OAuth 2.0 — RFC 6749, mục 2–7. Có sử dụng AI hỗ trợ; học viên đã xác nhận kiểm tra nhãn audit ngày **14/11/2026**.

## Dữ liệu và pipeline

**Chủ đề, nguồn/quyền, số trang và quy tắc tính trang:**

Corpus là RFC 6749, *The OAuth 2.0 Authorization Framework*, bản văn bản do học viên cung cấp trong `data/data_tu_tim.txt`. Chọn liên tục mục 2–7: đăng ký client, protocol endpoints, authorization grants, cấp token, refresh token và truy cập protected resources. Phần đã chọn nằm trong `data/oauth2_sections_2_to_7.txt`; phạm vi và hash file gốc được ghi tại `data/corpus_selection.json`. Tài liệu gốc ghi nguồn `http://www.rfc-editor.org/info/rfc6749`, tác giả biên tập D. Hardt và thời điểm October 2012. Đây là corpus để thí nghiệm retrieval trên nội dung lịch sử của tài liệu.

Phần đã chọn có khoảng 69.758 ký tự. TXT không được tính là trang PDF: corpus được chia tuần tự thành **41 đơn vị nguồn không chồng lặp**, mỗi đơn vị ít nhất **1.502 ký tự** sau loại khoảng trắng đầu/cuối. Ranh giới đặt ở đoạn văn; phần dư ngắn cuối tài liệu nhập vào đơn vị cuối. Các đơn vị bao phủ toàn bộ nội dung đã chọn, không nhân bản. `page` trong dữ liệu và trace là số đơn vị này, không phải số trang RFC. Manifest lưu từng ID, ranh giới ký tự và số ký tự tại `data/manifest.json`.

**Chuẩn hóa, lỗi và giới hạn:**

Văn bản được chuẩn hóa Unicode NFC, loại header/footer RFC lặp và dòng trắng thừa; giữ đoạn văn, thụt dòng, ví dụ và sơ đồ ASCII. Không dùng OCR. Các bước chuẩn bị có thể chạy lại bằng `scripts/prepare_corpus.py`. Pipeline kiểm tra text chunk bằng lát cắt ký tự của nguồn để giữ truy vết.

**Quyền sử dụng:** đã đối chiếu nguồn RFC Editor và IETF Trust ngày 13/11/2026. RFC xuất bản October 2012, tương ứng TLP 4.0 hiệu lực 28/12/2009. Cơ sở chia sẻ trích đoạn và giới hạn được ghi tại `data/RIGHTS_REVIEW.md`; thông báo gốc đi kèm ở `data/RFC6749_NOTICES.txt` và `results/RFC6749_NOTICES.txt`. Cần giữ các tệp này khi chia sẻ corpus/trace và ghi rõ nguồn IETF RFC 6749. Không cấp lại giấy phép cho toàn bộ RFC hoặc coi text xử lý là bản RFC chính thức.

**Embedding model/provider/version/số chiều, vector store/version, metric, lệnh chạy và chi phí:**

Embedding thật chạy local: `sentence-transformers/all-MiniLM-L6-v2`, commit `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, **384 chiều**, chuẩn hóa vector. Document và query dùng cùng model và phương pháp encode. Model đã tải trong `local_models/`, hash từng tệp nằm tại `results/model_manifest.json`. Phiên bản đã chạy: sentence-transformers 6.3.0, torch 2.15.0, qdrant-client 1.20.0; danh sách phụ thuộc đầy đủ tại `results/dependencies.txt`.

Vector store là **Qdrant local lưu bền vững** trong `local_vectors/`, metric cosine, tìm kiếm exact. Chọn backend này vì máy chưa có Docker. Cả ba cấu hình dùng cùng backend; không dùng vector ngẫu nhiên cho benchmark. Các collection `day6_A`, `day6_B`, `day6_C` dành riêng cho bài thí nghiệm. ID chunk xác định từ nguồn, đơn vị, offset và nội dung. Nạp lại ghi đè ID hiện tại và xóa ID cũ không còn trong snapshot; đã kiểm tra nạp hai lần không tăng số bản ghi. Kiểm tra tích hợp riêng đã xác nhận lọc metadata, thứ tự cosine, xóa dữ liệu cũ và mở lại store vẫn còn dữ liệu.

Hướng dẫn đầy đủ: `starter/RUN_CORPUS.md`. Chạy từ root:

```powershell
python scripts/prepare_corpus.py
python scripts/prepare_benchmark.py
python scripts/download_model.py
starter/.venv/Scripts/python.exe -m starter.src.run --model local_models/all-MiniLM-L6-v2 --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 --split dev
starter/.venv/Scripts/python.exe -m starter.src.run --model local_models/all-MiniLM-L6-v2 --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 --split test
```

Chi phí dịch vụ API trả phí: **0**; chưa định lượng điện, phần cứng và mạng. Thời gian đo không gồm cài thư viện hoặc tải model.

**Metadata bắt buộc, trường lọc bổ sung, nguồn giá trị và lý do chọn:**

Metadata bắt buộc: `document_id`, `source`, `page`; bổ sung `char_start`, `char_end_exclusive`, `top_level_section` và `language`. `top_level_section` là chuỗi lấy từ tiêu đề số thực tế tại vị trí chunk, không suy ra từ đáp án gold. Đơn vị nguồn có thể chứa nhiều mục nên pipeline tách chunk tại mọi tiêu đề đánh số và gắn mục đúng cho từng chunk. Offset ký tự bắt đầu từ 0, kết thúc không bao gồm ký tự tại offset cuối, trên file UTF-8 đã đọc với xuống dòng chuẩn Python.

## Cấu hình và benchmark

**A / B / C (tham số cụ thể, khác biệt duy nhất B–C):**

| Cấu hình | Chunking | Metadata filter |
|---|---|---|
| A | Cửa sổ tối đa 500 ký tự, overlap 50 | Không |
| B | Gom theo đoạn, tối đa 1.000 ký tự; đoạn quá dài được tách xác định | Không |
| C | Chính xác cùng chunk và vector với B | Áp dụng `top_level_section` chỉ khi câu hỏi có filter |

Cả ba cấu hình cùng tôn trọng ranh giới đơn vị nguồn và tiêu đề số. Vì vậy A là fixed-size có ràng buộc cấu trúc chung, không phải cửa sổ chạy xuyên toàn tài liệu. B có thể vẫn cắt danh sách qua chunk dù không cắt đoạn văn. So sánh A–B thay chính sách chia chunk; B–C chỉ thay filter.

**Bộ câu hỏi, phân chia dev/test, filter và kiểm chứng evidence:**

Benchmark gồm **20 câu tiếng Anh**, cùng ngôn ngữ corpus: q01–q15 dev, q16–q20 test. Có **4 câu filter**, trong đó **2 câu test**; phạm vi mục được nêu ngay trong câu hỏi. Mỗi câu có đáp án, nguồn/đơn vị, đoạn evidence và offset. Script `scripts/prepare_benchmark.py` kiểm tra evidence tồn tại nguyên văn và nằm trọn trong một đơn vị. Với anchor có nhiều đoạn khớp, các evidence được tìm thấy được lưu trong `gold_evidence`; danh sách này không được coi là đã bao quát mọi cách diễn đạt tương đương.

AI đã soạn bộ câu hỏi và kiểm tra với text nguồn; học viên chưa xác nhận từng câu. Tách dev/test trước khi chạy retrieval nhưng cùng một RFC và có chồng lặp chủ đề; người chuẩn bị dữ liệu đã thấy câu hỏi/gold test. Đây không phải kiểm tra mù trên tài liệu mới.

Kiểm chứng nội dung bổ sung sau chạy: AI đã đọc toàn bộ 20 câu/đáp án và evidence, ghi từng nhận xét tại `results/gold_ai_review.json`. Cả 20 đáp án chính đều được nguồn hỗ trợ, nhưng có 4 điểm về annotation: q05 nhận thêm đoạn về resource-owner password, khác client-password authentication; q06 nhận thêm đoạn về redirect/token endpoint thay vì authorization endpoint; q17 nhận thêm đoạn token endpoint thay vì authorization endpoint; q08 có quote kết thúc giữa câu tiếp theo. Đây là lỗi chất lượng gold cần công bố, không đồng nghĩa đáp án chính sai. Tính lại trên trace cũ sau khi loại các alternative khác ngữ cảnh của q05/q06/q17 cho kết quả Hit@1/Hit@3 không đổi ở cả hai split. Phân tích nhạy này không sửa benchmark/metric gốc, không tạo holdout mới, và chưa xử lý quote chưa trọn câu của q08. Đây vẫn là kiểm chứng bằng AI, không ghi nhận học viên đã tự đọc.

**Tiêu chí chọn chiến lược đã chốt trước khi xem test:**

Tiêu chí chọn cố định trước test: ưu tiên dev Evidence Hit@3, tiếp theo Hit@1, rồi ít chunk hơn; nếu vẫn hòa, chọn theo tên cấu hình. Dev chọn **B**, sau đó chạy test với cùng hash corpus, benchmark, code, model và cấu hình, không tinh chỉnh theo test. Quyết định lưu trong `results/dev_selection.json`.

Metric tự động yêu cầu chunk thuộc nguồn và đơn vị gold, đồng thời chứa **toàn bộ đoạn quote** sau chuẩn hóa khoảng trắng; chấp nhận các alternative gold đã ghi. Cách kiểm tra này bảo thủ hơn việc xem đoạn còn đủ thông tin trả lời hay không. Các nhận xét tương đương về ngữ nghĩa do AI đọc bên dưới chưa được dùng để sửa metric đã công bố.

Ngày 14/11/2026, học viên **Đào Văn Hiệp** đã ghi nhận kết quả kiểm chứng gold do AI thực hiện, gồm bốn điểm annotation cần công bố. Thông tin xác nhận lưu tại `benchmark/student_acknowledgment.json`; Ghi nhận này chỉ áp dụng phần gold, không tự động xác nhận các nhãn coherence/grounding.

## Kết quả

| Strategy | Split | Hit@1 (n/N) | Evidence Hit@3 (n/N) | Chunk count | Thời gian | Chi phí |
|---|---|---|---|---|---|---|
| A | dev | 7/15 | 8/15 | 182 | 8,942 giây | 0 (dịch vụ API) |
| B | dev | 7/15 | 11/15 | 116 | 7,069 giây | 0 (dịch vụ API) |
| C | dev | 7/15 | 11/15 | 116 | 1,232 giây | 0 (dịch vụ API) |
| A | test | 2/5 | 3/5 | 182 | 8,230 giây | 0 (dịch vụ API) |
| B | test | 4/5 | 5/5 | 116 | 6,564 giây | 0 (dịch vụ API) |
| C | test | 4/5 | 5/5 | 116 | 1,314 giây | 0 (dịch vụ API) |

**Đường dẫn trace, nhãn thủ công và cách chọn mẫu:**

Đường dẫn kết quả: `results/metrics_dev.json`, `results/metrics_test.json`; đủ 60 trace strategy/câu hỏi tại `results/traces_dev.jsonl` và `results/traces_test.jsonl`. Mỗi trace lưu 3 chunk, text đầy đủ, score, metadata, gold và nhãn tự động. Nhật ký tại `artifacts/experiment_log.csv`.

| Strategy | Tổng ký tự chunk, gồm overlap | Tổng token trước truncation | Ingest lần dev, giây | Ingest lần test, giây |
|---|---:|---:|---:|---:|
| A | 74.271 | 15.349 | 8,942 | 8,230 |
| B | 69.222 | 14.087 | 7,069 | 6,564 |
| C | 69.222 | 14.087 | 1,232 | 1,314 |

Thời gian trên gồm nạp và nạp lại để kiểm tra trùng lặp. C dùng lại vector đã tính cho B nên **không được suy ra C embedding nhanh hơn B**. Mỗi split chạy một lần; số đo không có khoảng tin cậy và không gồm thời gian cài thư viện/tải model. Chi phí dịch vụ API trả phí: 0; chưa định lượng điện, phần cứng hoặc mạng. Thời điểm và cấu hình mỗi lần chạy ở `results/run_dev.json` và `results/run_test.json`; latency truy xuất từng câu có trong trace.

### Đánh giá định tính có AI hỗ trợ, học viên đã kiểm tra và xác nhận

AI đọc trực tiếp các chunk ở cùng 10 vị trí đầu đơn vị nguồn 1–10 cho coherence, và toàn bộ top-3 của 5 câu test cho grounding. Đây là mẫu tập trung phần đầu corpus nên chưa đại diện đều mục 2–7. Không dùng Hit@3 để suy ra nhãn coherence/grounding. Mỗi nhãn có lý do và ghi reviewer là AI.

| Strategy | Coherence trung bình /2 (n) | Metadata đủ và đúng (n/N) | Filter tuân thủ (n/N hoặc N/A) | Grounding 0/1/2 (số câu) và trung bình /2 |
|---|---|---|---|---|
| A | 1,4 (10) | 15/15 | 0/2 | 0 / 0 / 5; TB 2,0/2 |
| B | 1,9 (10) | 15/15 | 1/2 | 0 / 0 / 5; TB 2,0/2 |
| C | 1,9 (10) | 15/15 | 2/2 | 0 / 0 / 5; TB 2,0/2 |

Metadata được đối chiếu bằng chương trình: nguồn, ID đơn vị, text tại offset và tiêu đề mục tại vị trí thực. Học viên đã xác nhận kiểm tra và đồng ý toàn bộ 45 bản ghi cùng các điểm coherence/grounding trong hồ sơ audit. A/B không được thiết kế áp filter nên tỷ lệ 0/2, 1/2 là mức tuân thủ phạm vi tự nhiên, không phải lỗi thực thi filter. C đáp ứng cả hai yêu cầu phạm vi dù Hit@3 không tăng.

Nhãn AI gốc: `results/coherence_ai_review.jsonl`, `results/grounding_ai_review.jsonl`. Bản học viên xác nhận sau khi kiểm tra: `results/coherence_manual_review.jsonl`, `results/test_manual_review.jsonl`, reviewer Đào Văn Hiệp, giữ ghi nhận AI hỗ trợ. Xác nhận qua trao đổi lưu tại `results/student_audit_confirmation.json`. Minh chứng metadata: `results/metadata_verification.json`; tổng hợp: `results/audit_summary.json`. Template trống và nhãn AI được giữ để truy vết.

## Phân tích và kết luận

**So sánh A–B và B–C; hai ví dụ sai có ID câu và nguồn:**

**A–B:** B tăng dev Hit@3 từ 8/15 lên 11/15 và test từ 3/5 lên 5/5, đồng thời giảm số chunk từ 182 xuống 116. Phần tăng phù hợp với khả năng giữ đoạn evidence nguyên vẹn hơn. Tuy nhiên metric dùng toàn bộ quote và thiên về chunk chứa đủ đoạn dài; chưa chứng minh mức tăng tương đương về khả năng trả lời thực tế.

**B–C:** chưa thấy chênh lệch Hit@1/Hit@3 trong bộ câu hỏi này. Metadata filter vẫn tăng mức tuân thủ phạm vi test từ 1/2 lên 2/2. Ví dụ q18 yêu cầu mục 6: B đưa cả chunk mục 5 vào top-3; C chỉ trả chunk mục 6. Kết quả minh họa giá trị kiểm soát phạm vi của metadata dù metric evidence không đổi. Hạn chế: filter chỉ theo mục của một tài liệu, chưa kiểm tra phiên bản hoặc nhiều nguồn xung đột; filter sai có thể loại evidence đúng.

**Ví dụ lỗi q18 (A), mục 6, đơn vị 39:** rank 2 bắt đầu bằng “server MAY issue a new refresh token” thay vì trọn mở đầu đoạn “The authorization server…”. Chunk vẫn chứa điều kiện cấp refresh token mới và yêu cầu scope giống token gửi lên, nhưng thiếu phần đầu quote nên metric tự động không hit. AI đọc thấy đủ để trả lời, gán grounding 2; cần học viên xác nhận evidence tương đương. Không sửa điểm tự động sau khi xem test.

**Ví dụ lỗi q19 (A), mục 7, đơn vị 39:** rank 3 chứa đầy đủ ba yêu cầu: validate access token, chưa hết hạn và scope bao phủ tài nguyên. Cuối đoạn bị cắt giữa phần giải thích phối hợp resource server/authorization server, nên không chứa toàn bộ gold quote. Metric tự động không hit, còn AI gán grounding 2 vì các câu trả lời chính vẫn đủ. B đưa cùng evidence đầy đủ lên rank 2. Cả B/C vẫn sai top-1 q19 vì rank 1 nói về authorization server xác thực client/resource owner credentials, khác vai trò resource server trong câu hỏi.

Một ví dụ coherence là đơn vị 5: A cắt giữa định nghĩa `client_secret`, làm mất ngoại lệ secret rỗng. B giữ được ngoại lệ và quy định không đưa credential vào URI. Ngược lại, B ở đơn vị 1 vẫn cắt danh sách SHALL sau item đầu, nên chia theo đoạn chưa bảo đảm giữ nguyên mọi cấu trúc danh sách.

**Chiến lược chọn, đánh đổi, điều kiện áp dụng:**

Chọn **B trong phạm vi thí nghiệm hiện tại** theo dev và quy tắc hòa định trước. C phù hợp khi ứng dụng cung cấp phạm vi mục rõ ràng, nhưng chưa có lợi thế về Hit@3 trên mẫu này.

**Hạn chế của dữ liệu, nhãn, test nhỏ, đo thời gian/chi phí:**

Model có giới hạn 256 token. Có **2 chunk của B/C**, tối đa 271 token, bị cắt khi embedding; A không có chunk vượt giới hạn. Text lưu trong vector store/trace vẫn đầy đủ và metric so trên text đầy đủ. Do đó Hit@3 không chứng minh embedding đã đọc toàn bộ evidence. Kiểm tra ở `results/token_audit_dev.json` và `results/token_audit_test.json`. Chưa làm thí nghiệm loại truncation; không quy kết chính xác lỗi nào do truncation nếu chưa có đối chứng.

Tập test chỉ 5 câu, mỗi câu tương đương 20 điểm phần trăm. Không tuyên bố B/C tốt nhất tổng quát hoặc có khác biệt có ý nghĩa thống kê. Các nhãn AI có nguy cơ thiên lệch, nhất là cùng công cụ đã tạo benchmark và triển khai pipeline; chưa có người chấm độc lập. Nguồn corpus chỉ một tài liệu, phần lớn câu hỏi truy xuất một đoạn, chưa kiểm tra tổng hợp nhiều nguồn hoặc câu không có đáp án.

**Nếu làm lại hoặc mở rộng, cải tiến gì?**

Nếu mở rộng: thiết kế chunk theo token và cấu trúc danh sách, ghim cấu hình mới thành thí nghiệm bổ sung; tạo tập test mới chưa dùng để chỉnh; thêm tài liệu và câu khó có nhiều phạm vi. Giữ kết quả hiện tại làm baseline, không thay test sau khi nhìn kết quả rồi gọi đó là đánh giá độc lập.

**Ghi nhận công cụ hỗ trợ:**

AI hỗ trợ chọn phạm vi, viết code, soạn benchmark, chạy thí nghiệm và dự thảo phân tích. Kiểm tra đã làm: offset/text khớp nguồn, gold quote tồn tại, giới hạn số đơn vị/câu hỏi, vector store integration, filter, số trace và chấm evidence có alternative gold. Các bước này chưa thay thế việc học viên hiểu code và giải thích bài.
