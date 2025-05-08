import pytest
from unittest.mock import patch
import pandas as pd

def test_data_quality_checks():
    """Prueba que los datos cumplan con lo esperado"""
    
    # Datos que imitan tu CSV exacto
    test_data = {
        'id': [1, None, 3],
        'amount': ['100.50', 'invalid', '200.75'],
        'created_at': ['01-01-2023', '02-01-2023', None],
        'paid_at': ['05-01-2023', '', None]
    }
    
    with patch('pandas.read_csv', return_value=pd.DataFrame(test_data)):
        from src.etl import df
        
        # Verifica limpieza
        assert df['id'].notna().all()
        assert pd.api.types.is_numeric_dtype(df['amount'])
        assert pd.api.types.is_datetime64_any_dtype(df['created_at'])
        assert len(df) == 1  # Solo 1 fila debería pasar todos los filtros