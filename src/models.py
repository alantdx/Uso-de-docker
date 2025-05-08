
"""
from sqlalchemy import Table, Column, String, DECIMAL, TIMESTAMP, ForeignKey
from .database import metadata

companies = Table(
    "companies", metadata,
    Column("id", String(24), primary_key=True),
    Column("name", String(130), nullable=False)
)

charges = Table(
    "charges", metadata,
    Column("id", String(24), primary_key=True),
    Column("company_id", String(24), ForeignKey("companies.id")),
    Column("amount", DECIMAL(16, 2), nullable=False),
    Column("status", String(30), nullable=False),
    Column("created_at", TIMESTAMP, nullable=False),
    Column("updated_at", TIMESTAMP, nullable=True)
) 
"""

# ======================================================================
# MODELO PYDANTIC PARA VALIDACIÓN DE TRANSACCIONES (Complementario a las tablas SQLAlchemy)
# ======================================================================

from datetime import datetime
from pydantic import BaseModel, validator

class Transaction(BaseModel):
    """
    Modelo de validación para transacciones financieras.
    
    Atributos:
        id (int): ID único de la transacción (debe ser positivo)
        amount (float): Monto monetario (validado como positivo)
        created_at (datetime): Fecha de creación en formato YYYY-MM-DD
        paid_at (datetime | None): Fecha de pago (opcional)

    Relación con tablas SQLAlchemy:
        - Campos compatibles con la estructura de la tabla 'charges'
        - Puede usarse para validar datos antes de insertar en la BD

    Ejemplo básico:
        >>> trans = Transaction(
        ...     id=1,
        ...     amount=150.99,
        ...     created_at="2023-01-01",
        ...     paid_at=None
        ... )
    """
    id: int
    amount: float
    created_at: datetime
    paid_at: datetime | None = None

    @validator('amount')
    def amount_must_be_positive(cls, value: float) -> float:
        """
        Garantiza que los montos sean valores positivos.
        
        Parámetros:
            value: Monto a validar
            
        Excepciones:
            ValueError: Si el monto es negativo
            
        Retorna:
            float: El mismo valor si pasa la validación

        Ejemplo:
            >>> Transaction(id=1, amount=100, created_at="2023-01-01")  # Válido
            >>> Transaction(id=2, amount=-50, created_at="2023-01-01")  # Lanza ValueError
        """
        if value < 0:
            raise ValueError("El monto debe ser positivo")
        return value

    @validator('created_at', 'paid_at', pre=True)
    def parse_dates(cls, value: str | None) -> datetime | None:
        """
        Convierte strings de fecha a objetos datetime.
        
        Parámetros:
            value: Cadena en formato YYYY-MM-DD o None
            
        Retorna:
            datetime: Objeto convertido
            None: Si el valor de entrada es None o no convertible

        Notas:
            - Formato esperado: ISO 8601 (YYYY-MM-DD)
            - Maneja valores nulos para campos opcionales
        """
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                return None
        return value
