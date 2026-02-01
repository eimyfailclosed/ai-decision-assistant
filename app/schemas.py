from pydantic import BaseModel, Field
from typing import List, Literal, Optional

DecisionType = Literal["answer", "refuse", "need_more_info"]

class DecideRequest(BaseModel):
    user_input: str = Field(..., min_length=1)
    context: Optional[str] = None

class DecideResponse(BaseModel):
    decision: DecisionType
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning_summary: str
    assumptions: List[str] = []
    risks: List[str] = []
    missing_information: List[str] = []
    audit_id: str
