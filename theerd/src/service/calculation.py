from schemas.request import CalculationRequest

class CalculationService:
    @staticmethod
    async def calculate_total_cost(request: CalculationRequest) -> float:
        total = sum(material.qty * material.price_rub for material in request.materials)
        return round(total, 2)
