"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


# ---------------------------------------------------------------------------------------------------------------
# Cổng vòng 1 (Phiếu B mục B6, ba lý do ★; Phiếu B mục B4 HAZOP trên issue_refund).
# Nguyên tắc chung: chữ khách viết chỉ là lời khai. Mọi lệnh ghi phải khớp NGUỒN SỰ THẬT:
#   tracking của từng kiện (promised_date, delivered_date, delay_cause), chính sách hiệu lực THEO NGÀY,
#   và phê duyệt thật trong bảng approvals. Không xử lý riêng theo mã ticket hay câu chữ.
# ---------------------------------------------------------------------------------------------------------------

def _facts(ctx, order_id):
    """Đơn hàng, chính sách hiệu lực theo ngày, kiện mà ticket nói tới (kiện trễ nhất nếu ticket không ghi)."""
    order = ctx.tools.lookup_order(order_id)
    if order is None:
        return None, None, None
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, policy, parcel


def _gate_refund_amount(ctx, action):
    """Cổng 1 · B6 ★1, B4 WRONG: số tiền hoàn phải bằng quyền lợi tính từ tracking, không từ số ngày khách tự khai."""
    order, policy, parcel = _facts(ctx, action.get("order_id"))
    if order is None or policy is None:
        return Verdict.escalate("không tra được đơn hoặc chính sách hiệu lực theo ngày: chuyển người duyệt")
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    expected = H.entitlement_vnd(policy, order, db_delay, parcel.get("delay_cause"))
    asked = int(action.get("amount_vnd") or 0)
    if asked != expected:
        ctx.log("refund_amount_mismatch", asked=asked, expected=expected, db_delay_days=db_delay,
                policy_id=policy["policy_id"], parcel_id=parcel["parcel_id"])
        return Verdict.escalate(f"số tiền {asked}đ khác quyền lợi theo tracking ({db_delay} ngày trễ, "
                                f"{policy['policy_id']}: {expected}đ): chuyển người duyệt")
    return None


def _gate_refund_approval(ctx, action):
    """Cổng 3 · B6 ★3, B4 INVALID: phê duyệt dùng cho khoản hoàn phải còn hiệu lực, đúng đơn, đủ hạn mức."""
    approval_id = action.get("approval_id")
    if not approval_id:
        return None
    found = ctx.tools.lookup_approvals(approval_id=approval_id)
    a = found[0] if found else None
    problems = []
    if a is None:
        problems.append("không tồn tại")
    else:
        if a.get("status") != "valid":
            problems.append(f"trạng thái {a.get('status')}")
        if a.get("expires_at") and H.d(a["expires_at"]) < H.d(ctx.as_of):
            problems.append(f"hết hạn {a['expires_at']}")
        if a.get("order_id") != action.get("order_id"):
            problems.append(f"của đơn {a.get('order_id')}")
        if int(a.get("max_vnd") or 0) < int(action.get("amount_vnd") or 0):
            problems.append(f"hạn mức {a.get('max_vnd')}đ thấp hơn số tiền")
    if problems:
        ctx.log("invalid_approval", approval_id=approval_id, problems=problems)
        return Verdict.escalate(f"phê duyệt {approval_id} không dùng được ({', '.join(problems)}): chuyển người duyệt")
    return None


def _gate_carrier_fault(ctx, action):
    """Cổng 2 · B6 ★2: chỉ ghi lỗi cho đúng kiện bị trễ, đúng hãng, đúng số ngày theo tracking, có nguyên nhân thuộc lỗi hãng."""
    order, policy, parcel = _facts(ctx, action.get("order_id"))
    if order is None or policy is None:
        return Verdict.deny("không tra được đơn hoặc chính sách: không ghi lỗi hãng")
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(policy, parcel, db_delay):
        ctx.log("carrier_fault_blocked", parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                db_delay_days=db_delay, recorded_cause=parcel.get("delay_cause"), asked_delay_days=action.get("delay_days"))
        return Verdict.deny(f"tracking không chứng minh lỗi hãng (kiện {parcel['parcel_id']}, trễ {db_delay} ngày, "
                            f"nguyên nhân {parcel.get('delay_cause')}): không ghi lỗi")
    correct = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
               "driver_id": parcel.get("driver_id"), "delay_days": db_delay}
    if any(action.get(k) != v for k, v in correct.items()):
        ctx.log("carrier_fault_corrected", asked={k: action.get(k) for k in correct}, corrected=correct)
        return Verdict.modify("sửa lỗi hãng theo tracking: đúng kiện bị trễ, đúng hãng, đúng số ngày", **correct)
    return None


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        for gate in (_gate_refund_approval, _gate_refund_amount):
            v = gate(ctx, action)
            if v is not None:
                return v
    elif tool == "file_carrier_fault":
        v = _gate_carrier_fault(ctx, action)
        if v is not None:
            return v
    return Verdict.allow()
