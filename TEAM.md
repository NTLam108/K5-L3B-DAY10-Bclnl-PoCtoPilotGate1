# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Bclnl
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Bclnl-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S8

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Trọng Lâm | 2A202603817 | Kỹ sư cổng | ✓ |
|   2 | Nguyễn Mạnh Quân | 2A202603776 | Sản phẩm và kinh doanh | |
|   3 | Nguyễn Đức Hiếu | 2A202603772 | Vận hành và pháp lý | |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenTrongLam-2A202603817

### Phần việc phụ trách

Kỹ sư cổng, trưởng nhóm (giữ repo, nhận thẻ). Câu 1.3, 1.5 (Phiếu A mục A2, A3); câu 2.1, 2.2, 2.6, 2.7 (Phiếu B mục B0, B1, B2, B7.1, B7.2);
câu 3.1 phần trace, 3.5 phần code, 3.6 (Phiếu C mục C0, C2, C7, C8). File: `lab10/guards.py`, `lab10/monitors.py`; chạy các lệnh
`lab10.eval`, `lab10.trace`, `lab10.gate`, `lab10.checkpoint`, `lab10.grade`.

### Đóng góp cụ thể

- Vòng 1: ba cổng trong `lab10/guards.py`: số tiền hoàn theo tracking (bắt `T-002@55`), lỗi hãng theo tracking, phê duyệt phải hợp lệ;
  bộ nền 0,9909 → 1,0, không ca nào hỏng thêm; chốt vòng 1 (`cf42ac1e`).
- Vòng 2 (thẻ S8): cổng 4 trần hoàn tự động 300.000đ/khách/ngày; cổng 3 thêm kiểm ticket, người cấp, mã đã dùng; hai chỉ số
  `approval_misuse_rate`, `customer_daily_auto_refund_max_vnd`; gói S8 0,8654 → 1,0, hoàn sai 6.845.000đ → 0.
- Sửa lỗi xuống dòng CRLF làm lệch hash bản chụp vòng 1 (`.gitattributes`).
- Có dùng trợ lý AI (Claude) để đọc code agent, gợi ý cổng, soạn nháp phiếu và chạy lệnh; mọi con số và quyết định đã được cả bàn xem lại.

### Bằng chứng

Commit: `b363693` (ký tiêu chí), `8c6ed49` (khối 2B), `6fa313b` (chốt vòng 1, v1), `dd5ad60` (giữ nguyên byte), `f4007da` (vòng 2 S8).
Lần chạy: `R-base-before-20261119-152440-bde05c`, `R-base-prepared-20261119-160843-bbddc5`, `R-S8-grade-20261119-170736-272069`.
Phiếu B mục B0, B1, B2, B7.1–B7.3; Phiếu C mục C0, C2, C7, C8.

### Exit ticket

- **Một điều học được:** cổng tốt đặt ở lệnh ghi và so với nguồn sự thật, không đặt ở model hay chữ khách viết.
  Nhờ vậy cổng 3 viết ở vòng 1 từ việc đọc code đã đỡ 5/7 ticket hỏng của thẻ S8 trước khi bàn biết sự cố, và lòng tin
  của người duyệt hồi lại từ hai con số trong config (ghi chú giải thích, kiểm mẫu 10%) chứ không phải từ thêm code.
- **Một điều còn chưa chắc:** các cổng có bị bài kiểm tra ẩn lách không, nhất là khi một người dùng nhiều tài khoản để chia nhỏ khoản hoàn, hoặc khi bảng `approvals` ghi sai; với dữ liệu mock, tôi chưa biết cổng chuyển người có làm hàng chờ
  ngập khi lượng ticket thật lớn hơn 52 ticket/ngày hay không.

## NguyenManhQuan-2A202603776
### Phần việc phụ trách
Sản phẩm và kinh doanh. T02; Câu 1.1, 1.6 (Phiếu A mục A1, A4, trực tiếp chạy lệnh ký tiêu chí A5);
câu 2.3, 2.5 (cầm bút phiên Pre-mortem 4 lăng kính, viết góc nhìn kinh doanh), 2.8 (behavioral test), 2.9 (Phiếu B mục B3, B6, B7.3, B7.4);
quyết định v1 (Phiếu B mục B8) và v2 (Phiếu C mục C12, `submission/submission.json`); câu 3.0, 3.2, 3.4 (cầm bút vẽ Fault tree), 3.5 (sửa con số kinh doanh và phân loại giảm hay ngăn ở C7) .
### Đóng góp cụ thể
- **Khối 0 & 1:** Chuẩn bị PRD v1.1 và Eval Card làm tài liệu chung cho cả bàn; soạn mục tiêu cấp hệ thống gắn với bài toán kinh doanh và an toàn tài chính; xây dựng bản tiêu chí thành công với 5 ngưỡng an toàn tuyệt đối và các ngưỡng vận hành; trực tiếp chạy lệnh 1 `python -m lab10.criteria sign` và đẩy cam kết lên Git trước lần chạy `eval` đầu tiên.
- **Khối 2A & 2B:** Lập bản đồ dữ liệu 7 luồng và phân tích nguy cơ trôi dạt (drift); chủ trì phiên Pre-mortem 4 lăng kính (nhận diện nguy cơ trục lợi qua chia nhỏ đơn và lạm dụng mã duyệt); thiết lập các tham số cổng kinh doanh trong `operating_gates.json` (`daily_refund_cap_vnd: 2.000.000`, `cost_budget: 1.500`, `roi_min: 0.2`, `pilot_scope: all`); viết 2 ticket kiểm thử biên (chia nhỏ tiền và khai khống ngày); đưa ra quyết định v1 **Tiếp tục** với đầy đủ chứng cứ mốc prepared.
- **Khối Sự cố S8 & Quyết định v2:** Phân tích sự cố S8; xây dựng đặc tả vi phạm và chủ trì vẽ cây lỗi Fault Tree 3 tầng (kỹ thuật, con người, quy trình vận hành); cùng Lâm & Hiếu thống nhất giải pháp siết chặt thẩm định mã duyệt và áp trần tự động 300.000đ/khách/ngày (giảm hoàn sai từ 6.845.000đ về 0đ, ROI tăng lên 2,39); viết quyết định v2 **Tiếp tục** kèm 3 dòng bắt buộc chứng minh tính vững chắc của giải pháp.
- Có sử dụng trợ lý AI để hỗ trợ tra cứu dữ liệu, tổng hợp PRD, kiểm tra logic Fault Tree và hoàn thiện biểu mẫu; toàn bộ số liệu, phân tích và quyết định đã được nhóm đối chiếu và kiểm chứng trực tiếp trên báo cáo máy chấm.
### Bằng chứng
- Commit: `b363693`, `e439866`, `2c88451`, `8c6ed49`, `6fa313b`, `b801e11`, `7c275e4`, `9749a43`.
- Lần chạy: `R-base-before-20261119-152440-bde05c`, `R-base-prepared-20261119-160843-bbddc5`, `R-S8-before-20261119-170737-272069`, `R-S8-prepared-20261119-170737-272069`, `R-S8-after-20261119-171938-272069`, `R-S8-grade-20261119-171937-272069`.
- Phiếu A mục A1, A4, A5; Phiếu B mục B3, B6, B7.3, B7.4, B8; Phiếu C mục C1, C5, C6, C7, C12; `config/acceptance_criteria.json`, `config/operating_gates.json` (mục `business`).
### Exit ticket
- **Một điều học được:** Bản tiêu chí chấp nhận được ký trước khi đo (Pre-committed acceptance criteria) là chốt chặn quan trọng nhất của tư duy Product/Engineering: nếu không "khóa cứng" các ngưỡng an toàn và quy tắc hành động trước khi chạy thực nghiệm, nhóm phát triển sẽ rất dễ tự biện minh và dời cột gôn (move the goalposts) để hợp thức hóa kết quả khi đối mặt với áp lực tiến độ.
- **Một điều còn chưa chắc:** Trong môi trường vận hành thực tế (production), khi người dùng cố tình đối kháng thông qua các mạng lưới tài khoản phân tán (nhiều SIM, nhiều tài khoản nhận tiền cùng một địa chỉ), cơ chế trần 300.000đ/khách/ngày dựa trên `customer_id` có thể bị vượt qua nếu chưa có hệ thống phân tích đồ thị liên kết thực thể (Entity Resolution/KYC) ở tầng nền tảng.

## NguyenDucHieu-2A202603772

### Phần việc phụ trách

Vận hành và pháp lý. Câu 1.2, 1.4 (Phiếu A mục A1, A2); câu 2.4, 2.10 (Phiếu B mục B4, B5, B7.5, B7.6, runbook 1–3);
câu 3.1 phần riêng của thẻ S8, 3.3, 3.7 (Phiếu C mục C3.1, C3.4, C4, C5 câu 3.3, C9, C10, C11, runbook 4–5); `submission/submission.json`.
File: `config/operating_gates.json` mục `operations`, `legal`.

### Đóng góp cụ thể

- Vòng 1: phân tích mục tiêu của kế toán đối soát và trưởng ca CSKH; xây dựng telemetry để phát hiện tác hại với bên thứ ba. Phụ trách HAZOP trên `issue_refund`, các rủi ro ngoài kỹ thuật và checklist go-live 9 nhóm có PIC.
- Phụ trách phương án vận hành và pháp lý: NV-TUNG chịu trách nhiệm vận hành, NV-HANH duyệt hoàn vượt hạn mức; 1 người trực, công suất 6 ca/giờ, hạn chờ 60 phút. Runbook quy định điều kiện dừng, người tắt công tắc, thời hạn xử lý và phương án giờ cao điểm.
- Đối chiếu cấu hình `operations` và `legal` với runbook: ghi chú giải thích quyết định, kiểm mẫu 10%; chặn `recipient_contact`, `customer_note` khi gửi hãng; chỉ ghi lỗi hãng khi có nguyên nhân được ghi nhận.
- Vòng 2 thẻ S8: phân tích quyền kiểm soát của người duyệt, việc chị Hạnh bị đứng tên cho khoản chưa duyệt và ảnh hưởng tới lòng tin; HAZOP của thẻ, giả định môi trường, fault tree sau sửa, risk register và runbook 4–5. Nêu rủi ro còn lại khi bảng phê duyệt cập nhật chậm hoặc một người dùng nhiều tài khoản.
- Phối hợp với Lâm và Quân đối chiếu kết quả ba mốc: S8 từ 36 ca ùn, chờ lâu nhất 216 phút ở base xuống 0 ca ùn, chờ lâu nhất 5 phút ở after; vẫn giữ 1 người trực, kiểm lại 10%. Phần code cổng và chỉ số theo dõi do Lâm phụ trách.
- Phụ trách rà thông tin thành viên, thẻ S8, quyết định và ba dòng bắt buộc trong `submission/submission.json` để khớp Phiếu C mục C12 và `TEAM.md`.
- Có sử dụng ChatGPT/Codex để đọc đề, đối chiếu phân công và dữ liệu vận hành, hỗ trợ thao tác Git và soạn mục cá nhân này.

### Bằng chứng

Các commit lưu sản phẩm chung liên quan đến phần việc: `2c88451` (Phiếu B B3–B6), `8c6ed49` (cấu hình vận hành/pháp lý và B7.5–B7.6), `7c275e4` (phân tích thẻ S8, HAZOP, giả định môi trường), `f4007da` (Phiếu C C9–C11), `9749a43` (hồ sơ nộp bài), `5623129` (rà soát C3.4 sau vòng 2).

Báo cáo chung: `submission/runs/grade-report.md`, mã `R-S8-grade-20261119-171937-272069`; ba mốc `R-S8-before-20261119-171938-272069`, `R-S8-prepared-20261119-171938-272069`, `R-S8-after-20261119-171938-272069`. Kết quả `PASS-VISIBLE`, chưa chạy test ẩn; after không lộ dữ liệu cá nhân, không ghi oan cho hãng, không có ca ùn.

Vị trí đối chiếu: Phiếu A A1 câu 1.2, A2 cột telemetry; Phiếu B B4, B5, B7.5, B7.6; Phiếu C C3.1, C3.4, C4, C5 câu 3.3, C9, C10, C11; `config/operating_gates.json` mục `operations`, `legal`.

### Exit ticket

- Một điều học được: an toàn của trợ lý hoàn tiền phụ thuộc cả quyền phê duyệt, dữ liệu đối soát và khả năng xử lý của người trực. Ghi chú giải thích và kiểm mẫu có thể giảm tải cho người duyệt, nhưng phải đi cùng cổng kiểm phê duyệt và điều kiện dừng rõ ràng.
- Một điều còn chưa chắc: cấu hình 1 người trực, kiểm mẫu 10% có giữ được thời hạn 60 phút khi lượng ticket thật tăng đột biến hay không; cần đo lại tải giờ cao điểm, thời gian chờ và độ trễ cập nhật mã phê duyệt trong pilot thật.
