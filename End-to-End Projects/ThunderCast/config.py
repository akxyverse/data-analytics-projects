import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase credentials
SUPABASE_URL = os.getenv("https://bbiphtlpmlieprivkxba.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJiaXBodGxwbWxpZXByaXZreGJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzAxOTY3OTEsImV4cCI6MjA4NTc3Mjc5MX0.r5-fcB1urDsthv66dZ8h3LRiksr4fe84ScpszkDfLPM")

# OpenWeatherMap API
OPENWEATHER_API_KEY = os.getenv("875905302d9005efdc2ea64f1e06c5ed")

# Default location (you can change this)
DEFAULT_LOCATION = {
    "city": "Pimpri-Chinchwad",
    "lat": 18.6298,
    "lon": 73.7997
}

