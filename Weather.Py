import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Use .env or set manually
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"📍 Weather in {city}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬️ Wind: {data['wind']['speed']} m/s")
        print(f"☁️ Description: {data['weather'][0]['description']}")
    else:
        print("❌ Error:", data.get("message", "Failed to retrieve data"))

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
