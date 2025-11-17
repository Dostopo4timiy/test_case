from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from db.repositories import CalculationRepository
from schemas.request import CalculationRequest
from schemas.response import CalculationResponse, CalculationHistory
from services.calculation import CalculationService

router = APIRouter()

@router.post("/", response_model=CalculationResponse)
async def calculate_cost(
    request: CalculationRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        # Calculate total cost
        total_cost = await CalculationService.calculate_total_cost(request)
        
        # Save to database
        repo = CalculationRepository(db)
        await repo.save_calculation(total_cost)
        
        return CalculationResponse(total_cost_rub=total_cost)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Calculation error: {str(e)}")

@router.get("/history", response_model=list[CalculationHistory])
async def get_calculation_history(
    db: AsyncSession = Depends(get_db)
):
    repo = CalculationRepository(db)
    calculations = await repo.get_recent_calculations(limit=10)
    return calculations
