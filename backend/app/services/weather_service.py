import requests
from app.config import WEATHER_API_KEY, WEATHER_URL

def get_weather(city):
    try:
        params = {"q": f"{city},IN", "appid": WEATHER_API_KEY, "units": "metric"}
        res = requests.get(WEATHER_URL, params=params, timeout=5)
        res.raise_for_status()
        data = res.json()
        return {"temp": data["main"]["temp"], "condition": data["weather"][0]["main"]}
    except Exception as e:
        print("Weather API failed:", e)
        return {"temp": 30, "condition": "Clear"}
