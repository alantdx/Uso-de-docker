
# Sistema ETL para Procesamiento Financiero

## 📋 Descripción
Pipeline ETL completo para procesamiento de datos transaccionales que:

1. Extrae datos desde archivos CSV
2. Valida y transforma los registros
3. Carga los resultados en PostgreSQL
4. Proporciona monitoreo via PgAdmin

Tecnologías clave:
- 🐍 Python 3.10
- 🐘 PostgreSQL 14
- 🐳 Docker + Docker Compose
- 🧪 Pytest (100% cobertura)

## 🚀 Requisitos Mínimos
| Componente       | Versión  |
|------------------|----------|
| Docker           | 20.10+   |
| Docker Compose   | 2.15+    |
| RAM disponible   | 4GB      |

## 🛠 Instalación Paso a Paso

### 1. Clonar repositorio
```bash
git clone https://github.com/tu-usuario/etl-financiero.git
cd etl-financiero
