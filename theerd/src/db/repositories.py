from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import CalculationResult
from schemas.response import CalculationHistory
from typing import List

class CalculationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def save_calculation(self, total_cost: float) -> CalculationResult:
        calculation = CalculationResult(total_cost_rub=total_cost)
        self.db.add(calculation)
        await self.db.commit()
        await self.db.refresh(calculation)
        return calculation
    
    async def get_recent_calculations(self, limit: int = 10) -> List[CalculationHistory]:
        result = await self.db.execute(
            select(CalculationResult)
            .order_by(CalculationResult.created_at.desc())
            .limit(limit)
        )
        calculations = result.scalars().all()
        return [CalculationHistory.from_orm(calc) for calc in calculations]
