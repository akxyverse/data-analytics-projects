import requests
from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

DEFAULT_LOCATION = {
    "city": "Pimpri-Chinchwad",
    "lat": 18.6298,
    "lon": 73.7997
}

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_weather_data():
    """Fetch current weather data from OpenWeatherMap API"""
    
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': DEFAULT_LOCATION['lat'],
        'lon': DEFAULT_LOCATION['lon'],
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract weather parameters
        weather_record = {
            'timestamp': datetime.now().isoformat(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'cloud_cover': data['clouds']['all'],
            'location': DEFAULT_LOCATION['city'],
            'latitude': DEFAULT_LOCATION['lat'],
            'longitude': DEFAULT_LOCATION['lon']
        }
        
        # Insert into Supabase
        result = supabase.table('weather_data').insert(weather_record).execute()
        print(f"✅ Weather data saved successfully at {weather_record['timestamp']}")
        print(f"Temperature: {weather_record['temperature']}°C, Humidity: {weather_record['humidity']}%")
        
        return weather_record
        
    except Exception as e:
        print(f"❌ Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    fetch_weather_data()