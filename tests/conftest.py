import pytest

@pytest.fixture
def docker_db_config():
    """Configuración de la DB idéntica a tu docker-compose.yml"""
    return {
        'user': 'postgres',
        'password': 'maya31416',
        'host': 'db',
        'port': '5432',
        'database': 'proyecto'
    }