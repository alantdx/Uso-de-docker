FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# Instala dependencias de producción + testing
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install pytest pytest-mock pytest-cov

COPY . .