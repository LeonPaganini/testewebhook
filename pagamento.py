import mercadopago
import os

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

sdk = mercadopago.SDK(ACCESS_TOKEN)

def gerar_link_pagamento():
    preference_data = {
        "items": [
            {
                "title": "Teste Simples",
                "quantity": 1,
                "unit_price": 0.50
            }
        ],
        "notification_url": "https://webhook-nutri.onrender.com/webhook",
        "external_reference": "teste123",
        "binary_mode": True
    }

    result = sdk.preference().create(preference_data)
    return result["response"]["init_point"]
