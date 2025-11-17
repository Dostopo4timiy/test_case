from sqlalchemy import Column, Integer, Numeric, DateTime, text
from datetime import datetime
from db.database import Base

class CalculationResult(Base):
    __tablename__ = "calc_results"
    
    id = Column(Integer, primary_key=True, index=True)
    total_cost_rub = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('NOW()'))
