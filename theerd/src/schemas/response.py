from pydantic import BaseModel
from datetime import datetime

class CalculationResponse(BaseModel):
    total_cost_rub: float

class CalculationHistory(BaseModel):
    id: int
    total_cost_rub: float
    created_at: datetime
    
    class Config:
        from_attributes = True
