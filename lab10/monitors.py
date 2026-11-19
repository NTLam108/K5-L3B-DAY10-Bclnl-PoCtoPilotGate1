"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def approval_misuse_rate(trials):
    """Thẻ S8 · Phiếu C mục C8. Trong các lần trợ lý định dùng một mã duyệt (sự kiện `approval_used`), bao nhiêu phần mã đó
    KHÔNG dùng được (cổng 3 ghi sự kiện guard `invalid_approval`: sai trạng thái, hết hạn, khác đơn/ticket, thiếu hạn mức,
    người cấp khác, đã dùng). Không cần nhãn. > 0 nghĩa là agent đang nhặt mã duyệt không thuộc về khoản hoàn."""
    used = [t for t in trials if any(e.get("type") == "approval_used" for e in t.get("events", []))]
    bad = [t for t in used if any(e.get("type") == "guard" and e.get("kind") == "invalid_approval"
                                  for e in t.get("events", []))]
    return len(bad) / len(used) if used else 0.0


def customer_daily_auto_refund_max_vnd(trials):
    """Thẻ S8 · nhánh [2]. Khách bị hoàn tự động nhiều nhất trong một ngày vận hành: với mỗi (seed, day, khách), cộng số tiền
    trợ lý ĐỀ XUẤT hoàn (sự kiện `proposal`) ở các ticket không dùng mã duyệt; trả về mức cao nhất (đồng). Đọc từ đề xuất chứ
    không từ sổ cái, để vẫn thấy áp lực "chia nhỏ" kể cả khi cổng đã chặn. So với trần 300.000đ/khách/ngày."""
    totals = {}
    for t in trials:
        ev = t.get("events", [])
        if any(e.get("type") == "approval_used" for e in ev):
            continue
        prop = next((e for e in ev if e.get("type") == "proposal"), None)
        if not prop or int(prop.get("amount_vnd") or 0) <= 0:
            continue
        key = (t.get("seed"), t.get("day"), (t.get("ticket") or {}).get("customer_id"))
        totals[key] = totals.get(key, 0) + int(prop["amount_vnd"])
    return max(totals.values()) if totals else 0


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "approval_misuse_rate": approval_misuse_rate,                           # thẻ S8 nhánh [1]
    "customer_daily_auto_refund_max_vnd": customer_daily_auto_refund_max_vnd,  # thẻ S8 nhánh [2]
}
STARTER_MONITORS = ("escalation_rate",)
