# 1. environment with python pre-installed
FROM python:3.12-slim

WORKDIR /app

# 2. install
# fastapi: library for create API of easy form
# uvicorn: Server that expose our API created with fastapi
RUN pip install fastapi uvicorn

# 3. Copi main file to docker
COPY main.py .

# 4. power on to Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]