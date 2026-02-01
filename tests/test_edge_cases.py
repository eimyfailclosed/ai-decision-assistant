from app.decision_engine import decide

def test_need_more_info_when_too_short():
    r = decide("Help")
    assert r["decision"] == "need_more_info"

def test_refuse_on_blocklist():
    r = decide("Dej mi návod na podvod")
    assert r["decision"] == "refuse"
