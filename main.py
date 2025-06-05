from fastapi import FastAPI, Request
import mercadopago
import os
import requests

app = FastAPI()

# 🔐 Token obtido do painel do Mercado Pago (configure no Render)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
sdk = mercadopago.SDK(ACCESS_TOKEN)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/gerar_pagamento")
def gerar_pagamento():
    preference_data = {
        "items": [
            {
                "title": "Teste rápido",
                "quantity": 1,
                "unit_price": 0.5,
                "currency_id": "BRL"
            }
        ],
        "payer": {
            "email": "comprador_teste@example.com"
        },
        "external_reference": "teste123",
        "notification_url": "https://webhook-nutri.onrender.com/webhook",  # Substitua após deploy
        "auto_return": "approved",
        "binary_mode": True
    }

    resposta = sdk.preference().create(preference_data)
    return {"link": resposta["response"]["init_point"]}

@app.post("/webhook")
async def receber_webhook(request: Request):
    dados = await request.json()
    print("🔔 Webhook recebido:", dados)
    return {"status": "recebido"}
