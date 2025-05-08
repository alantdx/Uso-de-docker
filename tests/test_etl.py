#######ESTO QUEDO PARA ESCALABILIDAD#######

import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
import sqlalchemy

def test_etl_flow_with_mocking():
    """Prueba TODO el flujo de tu ETL original sin modificarlo"""
    
    # 1. Mock del engine de SQLAlchemy
    mock_engine = MagicMock(spec=sqlalchemy.engine.Engine)
    
    # 2. Mock de pandas
    mock_df = MagicMock(spec=pd.DataFrame)
    mock_df.columns = ['id', 'amount', 'created_at', 'paid_at']
    
    # 3. Simula tu código exacto
    with patch('pandas.read_csv', return_value=mock_df), \
         patch('sqlalchemy.create_engine', return_value=mock_engine):
        
        # Importa TU código original (no modificado)
        from src.etl import df, engine
        
        # Verifica transformaciones
        mock_df.columns.str.strip.str.lower.str.replace.assert_called_once_with(" ", "_")
        pd.to_datetime.assert_any_call(mock_df['created_at'], dayfirst=True, errors='coerce')
        pd.to_datetime.assert_any_call(mock_df['paid_at'], dayfirst=True, errors='coerce')
        pd.to_numeric.assert_called_once_with(mock_df['amount'], errors='coerce')
        mock_df.dropna.assert_called_once_with(subset=['id', 'amount'])
        
        # Verifica carga a PostgreSQL
        mock_df.to_sql.assert_called_once_with(
            "transacciones",
            mock_engine,
            if_exists="replace",
            index=False
        )