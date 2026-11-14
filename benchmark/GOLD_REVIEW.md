# Kiểm chứng bộ câu hỏi

**Học viên: Đào Văn Hiệp — 2A202603813. Có sử dụng AI hỗ trợ kiểm chứng.**

Đã đọc và đối chiếu 20 câu, đáp án và evidence với corpus local. Người kiểm chứng: **AI**, hỗ trợ theo yêu cầu của học viên; không đại diện cho việc học viên đã tự xác nhận. Thực hiện sau khi chạy benchmark. Chi tiết từng câu và offset đã kiểm tra nằm tại `results/gold_ai_review.json`.

**Học viên ghi nhận kết quả: Đào Văn Hiệp — 2A202603813**, ngày 14/11/2026. Học viên đồng ý với bản kiểm chứng AI và các phát hiện nêu dưới đây qua trao đổi. Ghi nhận này không khẳng định đã có một lượt audit độc lập từng nguồn do học viên thực hiện. Chi tiết tại `benchmark/student_acknowledgment.json`.

Kết quả: **20/20 đáp án chính có cơ sở trong nguồn**. Có 4 điểm cần cải thiện annotation:

| Câu | Vấn đề | Xử lý trong hồ sơ hiện tại |
|---|---|---|
| q05 | Alternative mục 4.3.2 nói về mật khẩu resource owner; câu hỏi nói client-password authentication ở 2.3.1 | Giữ benchmark gốc; phân tích bổ sung loại alternative sai ngữ cảnh |
| q06 | Alternatives 3.1.2 và 3.2 nói redirect/token endpoint; câu hỏi nói authorization endpoint ở 3.1 | Giữ benchmark gốc; phân tích bổ sung chỉ chấp nhận 3.1 |
| q08 | Khuyến nghị 10 phút có đủ trong quote, nhưng câu tiếp theo bị cắt do ngắt trang của TXT gốc | Ghi hạn chế, không chỉnh quote sau khi nhìn test và gọi kết quả mới là holdout |
| q17 | Alternative 3.2 nói token endpoint; câu hỏi nói authorization request ở 3.1 | Giữ benchmark gốc; phân tích bổ sung chỉ chấp nhận 3.1 |

Sau khi bỏ alternative không đúng ngữ cảnh ở q05/q06/q17, tính lại **trên cùng trace đã có** cho Hit@1/Hit@3 không đổi ở mọi cấu hình và split. Điều này không loại bỏ các hạn chế khác của metric toàn bộ quote hoặc gold chưa bao quát mọi evidence tương đương. Không chỉnh cấu hình, chạy lại embedding hay thay tập test trong bước kiểm chứng này.

Chạy lại kiểm chứng từ thư mục gốc:

```powershell
python -m scripts.review_gold
```
