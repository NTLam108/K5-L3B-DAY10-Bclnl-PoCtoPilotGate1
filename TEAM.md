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
câu 3.1 phần riêng của thẻ, 3.3, 3.7 (Phiếu C mục C3.4, C4, C5, C9, C10, C11, runbook 4–5); `submission/submission.json`.
File: `config/operating_gates.json` mục `operations`, `legal`.

### Đóng góp cụ thể

(Hiếu tự viết.)

### Bằng chứng

(Hiếu tự viết: mã commit, mã lần chạy, dòng trong phiếu.)

### Exit ticket

(Hiếu tự viết.)
