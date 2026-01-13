from app.services.forecast_service import predict_national_load
from app.services.weather_service import get_weather
from app.advisory import compute_risk

def generate_advisory(city):
    last_24 = get_last_24_loads(city)
    if len(last_24) < 24:
        raise ValueError("Not enough history")

    load = predict_next_load(last_24)
    weather = get_weather(city)
    risk, reason = compute_risk(load, weather["temp"], weather["condition"])
    return {"predicted_load": load, "risk": risk, "reason": reason}
