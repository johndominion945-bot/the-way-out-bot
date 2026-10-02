import os
import json
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


def load_day():
    with open("content/day01.json", "r", encoding="utf-8") as file:
        return json.load(file)


day = load_day()

message = f"""☀️ <b>THE WAY OUT — DAY {day["day"]}</b>

<b>{day["title"]}</b>

📖 <b>Scripture</b>
{day["scripture"]}

{day["devotional"]}

🧠 <b>MIND CHECK</b>
{day["mind_check"]}

🏃 <b>BODY MOVE</b>
{day["body_move"]}

✝️ <b>SPIRIT MOVE</b>
{day["spirit_move"]}

🚪 <b>YOUR WAY OUT</b>
{day["way_out"]}

🙏 <b>PRAYER</b>
{day["prayer"]}

🔥 <b>TODAY'S ACTION</b>
{day["action"]}

—
<b>FAITH & FITNESS HOME</b>
TRAIN YOUR BODY. STRENGTHEN YOUR MIND. GLORIFY GOD.
"""

send_message(message)
