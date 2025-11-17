from pydantic import BaseModel, Field
from typing import List

class Material(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    qty: float = Field(..., gt=0)
    price_rub: float = Field(..., gt=0)

class CalculationRequest(BaseModel):
    materials: List[Material] = Field(..., min_items=1)
