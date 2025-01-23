from pydantic import BaseModel,Field

class AIRequest(BaseModel):
    """Request schema for ai endpoint"""
    question: str = Field(..., title="Question", description="The question to be answered")
