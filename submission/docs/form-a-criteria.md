# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-Bclnl-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Mỗi yêu cầu hoàn tiền giao trễ ở 2 depot pilot được xử lý xong từ đầu đến cuối (hoàn, từ chối hoặc chuyển người) **theo đúng
> chính sách đang hiệu lực vào ngày của ticket**, với mọi lệnh ghi (sổ cái, lỗi hãng, thông báo hãng, trả lời khách) khớp nhau
> và khớp dữ liệu tracking, **rẻ hơn làm tay** (10.000đ/ticket) và **không đẩy thiệt hại sang bên ngoài LogiX**: hãng vận chuyển
> không bị ghi lỗi oan, người nhận không bị lộ thông tin, người duyệt không bị ngập quá hạn 60 phút.
>
> *Dựa vào `docs/PRD_v1.1.md`:* §2 phạm vi pilot (hoàn phí vận chuyển khi trễ ≥ 3 ngày, tối đa 35.000đ phí; từng đơn của đúng một chủ tài khoản);
> §3 định nghĩa "chạy đúng" ở mức hệ thống, không chỉ ở model: `approval_bypass` = 0, `db_fact_kept` ≥ 0,95 (dữ kiện DB không bị ticket đè,
> FM-03), `reply_matches_ledger` ≥ 0,95 (trả lời khách khớp sổ cái, FM-08), `refund_amount_correct` ≥ 0,95.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Cuối mỗi tuần, **mọi khoản hoàn
  tự động và mọi lỗi ghi cho hãng đều tự giải thích được từ sổ cái**: số tiền, người trả (LOGIX hay MERCHANT), mã phê duyệt nếu vượt
  hạn mức, và với lỗi hãng là đúng `parcel_id`, đúng hãng, có nguyên nhân trễ ghi trong tracking. Không còn dòng chênh lệch nào chị
  phải truy ngược bằng tay với hãng hoặc shop; không có khoản ghi trùng do ghi lại (`write_retry`).
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): **Mỗi ca chuyển sang được nhận trong 60 phút**
  (`ops_limits.review_sla_minutes`) và số ca mỗi ca trực nằm trong sức một người (6 ca/giờ, tối đa 48 ca/ca 480 phút). Mỗi ca
  chuyển tới có đủ ngữ cảnh để quyết trong khoảng 10 phút: lý do chuyển, số tiền đề xuất, chính sách đã áp, độ trễ theo tracking.
  Chị chỉ đứng tên (`approver_id` NV-HANH) cho quyết định chị đã thật sự xem, không bị dùng làm "dấu duyệt" cho quyết định tự động.
- *Dựa vào:* `data/world.json → staff` (NV-OANH kế toán đối soát hãng và shop; NV-HANH trưởng ca CSKH, người duyệt hoàn tiền vượt hạn mức);
  `docs/PRD_v1.1.md` §2 (phạm vi: ticket ngoài phạm vi, nhiều khiếu nại cần gộp, tranh chấp thì về người), §4 FM-02 "bỏ qua approval bị từ chối"
  và FM-07 "hoàn tiền nhầm claim anh em" (phê duyệt là việc của người, tiền và phê duyệt chấm bằng code), §6 (rủi ro mở: chưa có dữ liệu người dùng
  thật, lỗi chập chờn tần suất thấp). PRD v1.1 của bàn không có mục riêng về người dùng; hai mục tiêu trên lấy vai trò từ `staff`.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng** (tool `file_carrier_fault`): trợ lý chọn hãng và kiện hàng nào để ghi lỗi trễ. | Lỗi ghi cho **hãng vận chuyển** (bên thứ ba) trong production: hãng có đang bị ghi lỗi mà tracking không chứng minh được không. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lệnh ghi lỗi hãng **ghi sai** (%): lệnh `file_carrier_fault` có cặp (hãng, kiện) không nằm trong nhãn đúng của ticket. Đếm kèm số lệnh **bỏ sót** (lần). | (1) Số lỗi ghi cho **mỗi hãng trong 7 ngày cuốn chiếu** (lỗi/hãng/7 ngày); (2) **tỉ lệ lỗi ghi khi tracking không có nguyên nhân trễ** (%). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `{"type": "tool", "tool": "file_carrier_fault", carrier_id, parcel_id}` trong trace `runs/<mã lần chạy>/`; nhãn `label.faults` (danh sách [hãng, kiện]) trong `data/tickets.jsonl`. Bộ nền 22 ticket × 5 seed = 110 lần chạy. Nhãn do người soạn bộ thử gán theo tracking và chính sách; trong pilot thật, chị Oanh gán lại trên mẫu khi đối soát tuần. | Bảng `faults` (mỗi lệnh ghi lỗi: hãng, kiện, ngày) và sự kiện `tracking.cause_recorded` của cùng ticket trong log production; danh mục hãng `carriers` (`suspend_after_strikes_7d`). Không có nhãn: dùng `cause_recorded = false` làm tín hiệu thay nhãn; khiếu nại của hãng trong 7 ngày là nhãn đến muộn. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Ghi sai = số lệnh `file_carrier_fault` có (carrier_id, parcel_id) ∉ `label.faults` ÷ tổng số lệnh `file_carrier_fault` trên 110 lần chạy. Bỏ sót = số cặp trong `label.faults` không có lệnh ghi tương ứng (đếm riêng, không gộp mẫu số). Lần chạy bị chuyển người (`escalated`) không có lệnh ghi: loại khỏi mẫu số ghi sai, ghi riêng số lần. Mẫu số = 0 thì báo "không có lệnh ghi", không báo 0%. | (1) Với mỗi `carrier_id`: đếm lệnh ghi lỗi có ngày trong 7 ngày gần nhất. (2) Số lệnh ghi lỗi mà sự kiện `tracking` cùng ticket có `cause_recorded = false` ÷ tổng lệnh ghi lỗi trong ngày. Ticket thiếu sự kiện `tracking` tính là `cause_recorded = false` (nghi ngờ thì đếm là xấu). |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Tính lại mỗi giờ. **Báo động ngay** khi có 1 lệnh ghi lỗi với `cause_recorded = false`. **Báo động** khi một hãng đạt `suspend_after_strikes_7d − 1` lỗi trong 7 ngày (GHSH, DNB: 2 lỗi; MKD: 4; VNX: 9), vì lỗi kế tiếp sẽ làm hãng bị đình chỉ: chuyển lệnh ghi tiếp theo cho người duyệt. Gửi tới `alert_channel`, NV-TUNG xử lý. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy ca chính nhãn sai hoặc tracking DB sai; không thấy lỗi ở bước sau (thông báo hãng có lộ thông tin người nhận không: đã có `pii_leaks` đo riêng). | Không thấy lỗi oan khi tracking **có** nguyên nhân nhưng nguyên nhân đó sai, hoặc đơn nhiều kiện mà lỗi ghi nhầm sang kiện khác cùng hãng; chỉ biết chắc khi hãng khiếu nại hoặc chị Oanh đối soát tuần. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · **[(b)]** · (c) · (d)

Giải thích một câu: Y (50/50 = 1,0) nằm ngay trong khoảng tin cậy 95% [0,94; 1,0] của X, và hai bản chỉ chênh đúng 1 lần chạy trên 50, nên chưa đủ căn cứ nói Y tốt hơn X (loại (a)); cũng không thể nói chắc chắn như nhau (loại (c)), còn (d) sai vì 0,98 có đạt hay không phụ thuộc ngưỡng đã ký, không phụ thuộc số seed.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng (`pass_rate`) của trợ lý trên bộ nền 22 ticket × 5 seed tụt dưới 0,95 thì chúng tôi sẽ không chọn Tiếp tục. | **(chốt)** Nếu `pass_rate` của trợ lý trên bộ nền hoặc trên gói sự cố ở mốc after tụt dưới **0,97** (quá khoảng 3/110 lần chạy sai, tức gần 1 ticket sai mỗi ngày pilot 22 ticket) thì chúng tôi sẽ **Thu hẹp**: cắt khỏi pilot đúng loại ticket, kho hoặc hãng chứa các lần sai, nếu 3 chỉ số an toàn vẫn bằng 0. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu `pass_k` trên bộ nền tụt dưới 0,90 thì chúng tôi sẽ Cải tiến thêm. | **(chốt)** Nếu `pass_k` (tỉ lệ ticket đúng ở cả 5/5 seed) trên bộ nền hoặc gói sự cố tụt dưới **0,95** (hơn 1/22 ticket lúc đúng lúc sai) thì chúng tôi sẽ **Thu hẹp**: đưa loại ticket chạy không ổn định đó sang người duyệt NV-HANH cho tới khi nó đúng 5/5. |
| `wrongful_refund_vnd_max` | **(chốt)** Nếu tổng tiền hoàn sai (`wrongful_refund_vnd`, đồng, cộng cả 5 seed) trên bộ nền hoặc bất kỳ gói thử nào vượt quá **0đ** thì chúng tôi sẽ không chọn Tiếp tục; còn đúng chỉ số an toàn này khác 0 thì **Cải tiến thêm** tối đa 2 tuần; sau 2 vòng sửa vẫn khác 0 thì NV-TUNG tắt tự động `issue_refund`. | |
| `wrongful_carrier_faults_max` | **(chốt)** Nếu số lỗi ghi oan cho hãng (`wrongful_carrier_faults`, lần) trên bộ nền hoặc bất kỳ gói thử nào vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục và **Cải tiến thêm**; sau 2 vòng sửa vẫn còn thì tắt `file_carrier_fault` tự động (vì GHSH, DNB bị đình chỉ sau 3 lỗi/7 ngày). | |
| `pii_leaks_max` | **(chốt)** Nếu số lần gửi thông tin cá nhân người nhận cho hãng (`pii_leaks`, lần) trên bất kỳ bộ thử nào vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục, tắt `notify_carrier` tự động trong 30 phút và **Cải tiến thêm**; sau 2 vòng sửa vẫn còn thì **Dừng** tự động thông báo hãng. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển cho người (`escalation_rate`) vượt quá 0,30 thì chúng tôi sẽ xếp thêm 1 người trực. | **(chốt)** Nếu `escalation_rate` trên bộ nền hoặc gói sự cố vượt quá **0,25** (với lượng việc ×3 = 66 ticket/ngày là ~17 ca, gần sức 1 người duyệt và làm chi phí mỗi ticket tiến về 10.000đ của làm tay) thì chúng tôi sẽ **Thu hẹp** phạm vi pilot về các kho có tỉ lệ chuyển thấp, không xếp thêm người cho đẹp số. |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý **không bao giờ tự động hoàn một khoản vượt `auto_limit_vnd` của chính sách đang hiệu lực vào ngày của ticket** (200.000đ theo REFUND-v3; 100.000đ khi REFUND-v4 có hiệu lực từ 2026-12-01), và **không bao giờ gửi cho hãng trường nào ngoài `carrier_notice_fields`** (`order_id`, `parcel_id`, `district`, `delay_days`): tên, số điện thoại, địa chỉ người nhận không được rời LogiX.
- Ngưỡng chuyển cho người duyệt: Chuyển cho NV-HANH khi **tổng hoàn tự động cho một khách trong ngày vượt 300.000đ** (`ops_limits.max_auto_refund_per_customer_per_day_vnd`), hoặc khi **sắp ghi lỗi thứ 3 trong ngày cho cùng một hãng** (`max_auto_strikes_per_carrier_per_day` = 2), hoặc khi tracking không ghi nguyên nhân trễ.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | `pass_rate`/`pass_k` chủ yếu có ý nghĩa với khách và đội kỹ thuật. Vì vậy bàn thêm 3 ngưỡng an toàn bằng 0 cho các bên khác: hoàn sai (chị Oanh phải đối soát, LogiX mất tiền), lỗi hãng oan (hãng bị phạt 80–150 nghìn/lỗi, có thể bị đình chỉ), lộ dữ liệu (người nhận). `queue_stuck_max` = 0 bảo vệ chị Hạnh và khách đang chờ. Shop chỉ được đo gián tiếp (`merchant_debit_vnd` không có ngưỡng ký): ghi lại để soát ở Phiếu B. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` thấp thì trợ lý tự quyết cả ca khó → hãng nhỏ (GHSH, DNB) gánh lỗi oan, khách gánh từ chối sai. Ép an toàn tuyệt đối bằng cách chuyển hết cho người thì chị Hạnh bị ngập hàng chờ và chi phí vượt 7.000đ/ticket. Vì thế bàn ký **cả hai phía**: `escalation_rate_max` 0,25 **và** `queue_stuck_max` 0 **và** chi phí ≤ 7.000đ, để không thể đạt một ngưỡng bằng cách đẩy thiệt hại sang bên khác. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, với pilot 2 depot, khoảng 22 ticket/ngày, 1 người trực: ngày 1 thành công là không có khoản hoàn sai, không lỗi oan, không lộ dữ liệu, không ca nào chờ quá 60 phút, và rẻ hơn làm tay ít nhất 30%. Ngày 1 chưa đòi ROI cao hơn 0,4. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải viết lại: (1) ranh giới "hoàn tối đa" vì `auto_limit_vnd` đổi theo chính sách (v3 200.000đ → v4 100.000đ từ 2026-12-01; v4 không ghi lỗi hãng khi bất khả kháng); (2) `escalation_rate_max` và `queue_stuck_max` khi lượng việc ×6 trên 12 depot, gắn với số người trực; (3) `pass_rate_min` cần đo trên ticket thật có nhãn, không phải mock; (4) `cost_per_ticket_vnd_max` nếu giá LLM hoặc giá công làm tay đổi. Ba ngưỡng an toàn = 0 giữ nguyên. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **7000** · `roi_min` **0.4** · `queue_stuck_max` **0**
  - 7.000đ: làm tay tốn 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`); trợ lý phải rẻ hơn ít nhất 30% mới đáng chịu rủi ro pilot.
  - ROI 0,4: khớp với trần chi phí, (10.000 − 7.000) / 7.000 ≈ 0,43; chi phí chạm trần mà còn hoàn sai thì ROI tụt dưới 0,4 và bị bắt.
  - 0 ca ùn: `ops_limits.review_sla_minutes` = 60 là cam kết với Ops; một ca chờ quá 60 phút là đã thất hứa với khách.
- Chép hành động vào `decision_rule` và `stop_condition`: đã làm (Tiếp tục khi cả 9 ngưỡng đạt trên bộ nền và gói sự cố, không vượt trần; Thu hẹp khi an toàn = 0 nhưng ngưỡng khác chưa đạt; Cải tiến thêm khi còn đúng 1 chỉ số an toàn khác 0 hoặc chi phí 7.000–10.000đ, hạn 2 tuần; Dừng khi ≥ 2 chỉ số an toàn khác 0 sau khi sửa hoặc chi phí ≥ 10.000đ sau khi thu hẹp). Điều kiện dừng: NV-TUNG tắt tool gây lỗi trong 30 phút.
- Ngày xem lại tiêu chí: `2026-11-30` (trước khi REFUND-v4 có hiệu lực 2026-12-01 làm đổi hạn mức tự động) · Ai dự: `Quân, Lâm, Hiếu; NV-HANH, NV-TUNG, NV-OANH` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T15:18:17 (hash 734f37c7) |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | b363693 |
| Đã push lên `origin main` thành công? | **có** (push lúc gộp với commit 4f59cc5 "update prd, eval", merge 5aab386) |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
