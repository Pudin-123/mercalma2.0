import requests
from django.conf import settings

def enviar_a_telegram(texto, chat_id=None, buttons=None):
    token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    if not token:
        print("⚠️ TELEGRAM_BOT_TOKEN no está configurado.")
        return

    if not chat_id:
        chat_id = getattr(settings, "TELEGRAM_CHAT_ID", None)
        if not chat_id:
            print("⚠️ No se pasó chat_id y no hay TELEGRAM_CHAT_ID.")
            return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "HTML",
    }

    if buttons:
        payload["reply_markup"] = {"inline_keyboard": buttons}

    try:
        response = requests.post(url, json=payload, timeout=10)
        print("🔍 Payload enviado a Telegram:", payload)
        print("📬 Respuesta de Telegram:", response.status_code, response.text)

        if response.status_code != 200:
            print("⚠️ Error enviando a Telegram:", response.text)
        else:
            print(f"✅ Mensaje enviado a Telegram ({chat_id})")

    except requests.RequestException as e:
        print("❌ Error al conectar con Telegram:", e)
    except Exception as e:
        print("❌ Error inesperado al enviar a Telegram:", e)