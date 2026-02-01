import uuid
from typing import Dict, Any, Optional

CONFIDENCE_MIN_ANSWER = 0.55
BLOCKLIST = ["návod na podvod", "ukrást", "vyrobit bombu"]  # demo placeholder

def policy_check(text: str) -> list[str]:
    lowered = text.lower()
    return [w for w in BLOCKLIST if w in lowered]

def required_info_missing(text: str) -> list[str]:
    if len(text.strip()) < 20:
        return ["More context is required (goal, constraints, details)."]
    return []

def decide(user_input: str, context: Optional[str] = None) -> Dict[str, Any]:
    audit_id = str(uuid.uuid4())
    full_text = user_input if not context else f"{user_input}\n\nContext: {context}"

    policy_hits = policy_check(full_text)
    if policy_hits:
        return {
            "decision": "refuse",
            "confidence": 1.0,
            "reasoning_summary": "Request falls into a disallowed or high-risk category.",
            "assumptions": [],
            "risks": policy_hits,
            "missing_information": [],
            "audit_id": audit_id,
        }

    missing = required_info_missing(full_text)
    if missing:
        return {
            "decision": "need_more_info",
            "confidence": 0.35,
            "reasoning_summary": "I need more information to answer reliably.",
            "assumptions": [],
            "risks": ["insufficient context"],
            "missing_information": missing,
            "audit_id": audit_id,
        }

    return {
        "decision": "answer",
        "confidence": CONFIDENCE_MIN_ANSWER,
        "reasoning_summary": "Sufficient context provided; returning a bounded response.",
        "assumptions": ["User provided adequate details."],
        "risks": [],
        "missing_information": [],
        "audit_id": audit_id,
    }
