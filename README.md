# AI Decision Assistant (Audit-First)

Audit-first decision system that enforces deterministic decisions around uncertainty and refusal.
Every interaction produces an audit_id and is logged.

## Run
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Open: http://127.0.0.1:8000/docs
