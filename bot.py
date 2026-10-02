import os
import requests


TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

API_URL = "https://api.telegram.org/bot" + TOKEN


def send_message(text):
    url = API_URL + "/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=data, timeout=30)

    if not response.ok:
        print("Telegram error:")
        print(response.text)
        response.raise_for_status()

    print("Message sent successfully.")


message = """☀️ <b>THE WAY OUT</b>

Welcome to your 30-Day Christian Morning Journey.

This is more than a book.

For the next 30 days, we're going to build your:

🧠 MIND
🏃 BODY
✝️ SPIRIT

<b>DAY 1 is coming.</b>

Prepare your heart.
Prepare your mind.
Turn toward God.

— FAITH & FITNESS HOME
"""

send_message(message)
