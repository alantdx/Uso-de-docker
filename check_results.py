import pandas as pd
from sqlalchemy import create_engine

# Usa la misma conexión que en etl.py
engine = create_engine("postgresql://postgres:maya31416@db:5432/proyecto")

# Leer datos de la tabla
df = pd.read_sql("SELECT * FROM transacciones", engine)
print(df.head())
print(f"\nTotal de registros: {len(df)}")