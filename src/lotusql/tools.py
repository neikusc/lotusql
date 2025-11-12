import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('../.env')
API_KEY = os.getenv("OPENWEATHER_API_KEY")

from datetime import datetime

def get_current_datetime() -> str:
    """
    Returns the current date and time from the computer system.

    This function uses the system clock to retrieve the current local date and time,
    and formats it as a human-readable string in the format 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        str: The current date and time as a formatted string.

    Example:
        >>> get_current_datetime()
        '2025-04-18 14:42:30'
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_today_weather(city: str) -> str:
    """
    Fetches today's weather for a given city using the OpenWeatherMap API.

    Args:
        city (str): Name of the city to query weather for.

    Returns:
        str: A human-readable summary of the current weather.

    Example:
        >>> get_today_weather("San Diego")
        'The current weather in San Diego is 19°C with clear sky.'
    """

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The current weather in {city} is {temp:.1f}°C with {weather}."
    elif response.status_code == 404:
        return f"City '{city}' not found."
    else:
        return f"Failed to fetch weather: {response.status_code} — {response.text}"
    

if __name__ == "__main__":
    city = "San Diego"
    print(get_today_weather(city))
    print(get_current_datetime())