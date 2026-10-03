import os
import json
from datetime import date, datetime
from zoneinfo import ZoneInfo
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


def load_journey():
    with open("journey.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_day(day_number):
    filename = "content/day" + str(day_number).zfill(2) + ".json"

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


journey = load_journey()

start_date = date.fromisoformat(journey["start_date"])

today = datetime.now(
    ZoneInfo("Africa/Lagos")
).date()

day_number = (today - start_date).days + 1


if day_number < 1:
    print("The Way Out journey has not started yet.")
    raise SystemExit


if day_number > 30:
    print("The 30-day journey is complete.")
    raise SystemExit


day = load_day(day_number)


message = f"""☀️ <b>THE WAY OUT — DAY {day["day"]}</b>

<b>{day["title"]}</
