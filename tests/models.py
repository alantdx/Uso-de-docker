
from datetime import datetime
from pydantic import BaseModel, validator

class Transaction(BaseModel):
    """Modelo Pydantic para transacciones"""
    id: int
    amount: float
    created_at: datetime
    paid_at: datetime | None = None  # Campo opcional

    @validator('amount')
    def amount_must_be_positive(cls, value):
        """Valida que el monto sea positivo"""
        if value < 0:
            raise ValueError("El monto debe ser positivo")
        return value

    @validator('created_at', 'paid_at', pre=True)
    def parse_dates(cls, value):
        """Convierte strings a datetime"""
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d')  # Ajusta el formato según tu CSV
            except ValueError:
                return None
        return value