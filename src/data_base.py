
"""
Configuración centralizada de la base de datos

Variables:
    engine: Conexión SQLAlchemy a PostgreSQL
    metadata: Objeto para definir esquemas de tablas
"""
from sqlalchemy import create_engine, MetaData
import os

# Configuración desde variables de entorno (seguro para Docker)
DB_CONFIG = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'password': os.getenv('POSTGRES_PASSWORD', 'maya31416'),
    'host': os.getenv('POSTGRES_HOST', 'db'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
    'database': os.getenv('POSTGRES_DB', 'proyecto')
}

DATABASE_URL = (
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
metadata = MetaData()