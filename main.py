from fastapi import FastAPI, Request
from pagamento import gerar_link_pagamento
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def gerar_link():
    link = gerar_link_pagamento()
    return {"link_pagamento": link}

@app.post("/webhook")
async def receber_webhook(request: Request):
    body = await request.json()
    logging.info(f"📩 Webhook recebido: {body}")
    return {"status": "ok"}
