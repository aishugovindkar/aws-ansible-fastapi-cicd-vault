from fastapi import FastAPI
import hvac
import os

app = FastAPI()

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://127.0.0.1:8200")
VAULT_TOKEN = os.getenv("VAULT_TOKEN", "devtoken")
VAULT_SECRET_PATH = "myapp"

@app.get("/")
def home():
    return {"message": "🚀 FastAPI with Vault running on AWS!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/secrets")
def get_secret():
    try:
        client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
        secret = client.secrets.kv.v2.read_secret_version(path=VAULT_SECRET_PATH)
        value = secret['data']['data']['MY_SECRET']
        return {"MY_SECRET": value}
    except Exception as e:
        return {"error": str(e)}
