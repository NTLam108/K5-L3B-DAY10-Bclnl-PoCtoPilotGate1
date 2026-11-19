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

(Lâm tự viết: một điều học được, một điều còn chưa chắc.)

## NguyenManhQuan-2A202603776

### Phần việc phụ trách

Sản phẩm và kinh doanh. Câu 1.1, 1.6 (Phiếu A mục A1, A4, ký tiêu chí A5); câu 2.3, 2.5, 2.8, 2.9 (Phiếu B mục B3, B6, B7.3, B7.4);
quyết định v1 (Phiếu B mục B8) và v2 (Phiếu C mục C12); câu 3.2, 3.4 (Phiếu C mục C5, C6). File: `config/acceptance_criteria.json`,
`config/operating_gates.json` mục `business`.

### Đóng góp cụ thể

(Quân tự viết.)

### Bằng chứng

(Quân tự viết: mã commit, mã lần chạy, dòng trong phiếu.)

### Exit ticket

(Quân tự viết.)

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
