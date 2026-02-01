from fastapi import FastAPI
from app.schemas import DecideRequest, DecideResponse
from app.decision_engine import decide
from app.audit_logger import init_db, audit_log

app = FastAPI(title="AI Decision Assistant", version="0.1.0")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/decide", response_model=DecideResponse)
def decide_endpoint(payload: DecideRequest):
    result = decide(payload.user_input, payload.context)
    audit_log(result["audit_id"], payload.model_dump(), result)
    return result
