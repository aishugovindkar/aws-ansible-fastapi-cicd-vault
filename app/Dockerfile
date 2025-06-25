FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

ENV VAULT_ADDR=http://127.0.0.1:8200
ENV VAULT_TOKEN=devtoken

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
