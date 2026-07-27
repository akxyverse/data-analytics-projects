import pandas as pd
import pickle
from datetime import datetime, timezone
from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL:
    SUPABASE_URL = "https://bbiphtlpmlieprivkxba.supabase.co"
    SUPABASE_KEY = ""

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load trained model
model_path = 'D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/models/prophet_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

print("🔮 ThunderCast Prediction System")
print("=" * 80)

# Fetch latest weather data
response = (
    supabase
    .table('weather_data')
    .select('*')
    .order('timestamp', desc=True)
    .limit(1)
    .execute()
)

if not response.data:
    print("❌ No weather data available. Run data_collection.py first!")
    exit()

latest_data = response.data[0]

print("\n📊 Current Weather Conditions:")
for k in ['timestamp', 'temperature', 'humidity', 'pressure', 'wind_speed', 'cloud_cover']:
    print(f"{k.capitalize()}: {latest_data[k]}")

# Prepare future dataframe (next 6 hours)
future_dates = pd.date_range(
    start=datetime.now(timezone.utc),
    periods=6,
    freq='h'
)

future = pd.DataFrame({
    'ds': future_dates,
    'tempC': latest_data['temperature'],
    'humidity': latest_data['humidity'],
    'pressure': latest_data['pressure'],
    'windspeedKmph': latest_data['wind_speed'] * 3.6,
    'cloudcover': latest_data['cloud_cover'],
    'precipMM': 0
})

# Predict
forecast = model.predict(future)

print("\n⚡ Thunderstorm Predictions (Next 6 Hours):")
print("-" * 80)

prediction_rows = []

for _, row in forecast.iterrows():
    probability = max(0, min(100, row['yhat'] * 100))
    time_label = row['ds'].strftime('%I:%M %p')

    status = (
        "🔴 HIGH RISK" if probability > 70 else
        "🟡 MODERATE RISK" if probability > 40 else
        "🟢 LOW RISK"
    )

    print(f"{time_label}: {probability:.1f}% {status}")

    prediction_rows.append({
        'prediction_time': datetime.now(timezone.utc).isoformat(),
        'forecast_time': row['ds'].isoformat(),
        'thunderstorm_probability': float(probability),
        'location': latest_data['location'],
        'model_version': 'prophet_v1'
    })

# 🔥 Batch insert (FAST + SAFE)
supabase.table('predictions').insert(prediction_rows).execute()

print("\n✅ Predictions saved to database!")
print("=" * 80)
