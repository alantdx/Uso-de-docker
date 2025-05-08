import os
import pandas as pd
from sqlalchemy import create_engine

# Configuración de la base de datos (usa tu contraseña)
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "maya31416")  # <-- Tu contraseña
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "proyecto")  # <-- Cambiar a 'proyecto'

# Crear la URL de conexión
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Cargar el archivo CSV (con delimitador por defecto ",")
csv_path = "data/data_prueba_tecnica.csv"
df = pd.read_csv(csv_path)

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convertir fechas
df['created_at'] = pd.to_datetime(df['created_at'], dayfirst=True, errors='coerce')
df['paid_at'] = pd.to_datetime(df['paid_at'], dayfirst=True, errors='coerce')

# Convertir amount a numérico
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Eliminar filas que no tengan ID o amount
df = df.dropna(subset=['id', 'amount'])

# Cargar en PostgreSQL
df.to_sql("transacciones", engine, if_exists="replace", index=False)

print("✅ Datos cargados exitosamente en la tabla 'transacciones'")

# ============== ADICIONES PARA TESTING ============== #

"""
### 🛠️ (BLOQUE PARA PRUEBAS UNITARIAS - DESCOMENTAR SOLO PARA TESTING)

def get_database_url():
    # Versión modular de la configuración de la DB
    return f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:{os.getenv('POSTGRES_PASSWORD', 'maya31416')}@{os.getenv('POSTGRES_HOST', 'db')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB', 'proyecto')}"

def load_data_from_csv(filepath):
    # Versión testeable del procesamiento de datos
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df['created_at'] = pd.to_datetime(df['created_at'], dayfirst=True, errors='coerce')
    df['paid_at'] = pd.to_datetime(df['paid_at'], dayfirst=True, errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    return df.dropna(subset=['id', 'amount'])

def main():
    # Punto de entrada alternativo para pruebas
    engine = create_engine(get_database_url())
    df = load_data_from_csv("data/data_prueba_tecnica.csv")
    df.to_sql("transacciones", engine, if_exists="replace", index=False)
    print("✅ Datos cargados (desde función main())")

if __name__ == "__main__":
    # Permite ejecutar python etl.py para testing
    main()
"""


