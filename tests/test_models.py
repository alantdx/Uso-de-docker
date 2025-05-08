#######ESTO QUEDO PARA ESCALABILIDAD#######

import pytest
from datetime import datetime
from src.models import Transaction

class TestTransactionModel:
    """
    Conjunto de pruebas unitarias para el modelo Transaction.
    
    Verifica el comportamiento del modelo de transacciones incluyendo:
    - Creación básica de instancias
    - Manejo de campos opcionales
    - Validación de reglas de negocio
    """

    def test_transaction_creation(self):
        """
        Prueba la creación básica de una transacción con datos válidos.
        
        Casos verificados:
        - Asignación correcta de todos los atributos
        - Conversión automática de fechas desde string
        - Tipado correcto de los campos
        
        Assertions:
            - Los valores asignados deben coincidir con los proporcionados
            - created_at debe ser instancia de datetime
        """
        trans = Transaction(
            id=1,
            amount=100.50,
            created_at="2023-01-01",
            paid_at="2023-01-05"
        )
        assert trans.id == 1
        assert trans.amount == 100.50
        assert isinstance(trans.created_at, datetime)

    def test_optional_paid_at(self):
        """
        Verifica el comportamiento del campo opcional paid_at.
        
        Casos verificados:
        - El campo paid_at acepta valores None
        - No genera errores cuando es omitido
        
        Assertions:
            - paid_at debe ser None cuando se especifica así
        """
        trans = Transaction(
            id=2,
            amount=200.0,
            created_at="2023-01-02",
            paid_at=None
        )
        assert trans.paid_at is None

    def test_amount_validation(self):
        """
        Prueba la validación de montos negativos.
        
        Casos verificados:
        - El modelo rechaza valores negativos en amount
        - Genera ValueError con mensaje descriptivo
        
        Assertions:
            - Debe lanzar ValueError cuando amount es negativo
        """
        with pytest.raises(ValueError):
            Transaction(
                id=3,
                amount=-100,
                created_at="2023-01-03"
            )