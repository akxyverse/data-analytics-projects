import pandas as pd
import numpy as np
from prophet import Prophet
import pickle
import os

# Load featured data
df = pd.read_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/processed/pune_featured.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

print("🤖 Starting Prophet Model Training...")

# Prepare data for Prophet
# Prophet needs columns named 'ds' (datetime) and 'y' (target variable)
prophet_df = pd.DataFrame({
    'ds': df['date_time'],
    'y': df['thunderstorm']  # Target: thunderstorm probability
})

# Add regressors (extra features)
prophet_df['tempC'] = df['tempC']
prophet_df['humidity'] = df['humidity']
prophet_df['pressure'] = df['pressure']
prophet_df['windspeedKmph'] = df['windspeedKmph']
prophet_df['cloudcover'] = df['cloudcover']
prophet_df['precipMM'] = df['precipMM']

print(f"📊 Training data shape: {prophet_df.shape}")
print(f"Date range: {prophet_df['ds'].min()} to {prophet_df['ds'].max()}")

# Initialize Prophet model
model = Prophet(
    daily_seasonality=True,
    weekly_seasonality=True,
    yearly_seasonality=True,
    changepoint_prior_scale=0.05,
    interval_width=0.95
)

# Add regressors
model.add_regressor('tempC')
model.add_regressor('humidity')
model.add_regressor('pressure')
model.add_regressor('windspeedKmph')
model.add_regressor('cloudcover')
model.add_regressor('precipMM')

print("\n🔧 Model configuration:")
print(f"- Daily seasonality: Enabled")
print(f"- Weekly seasonality: Enabled")
print(f"- Yearly seasonality: Enabled")
print(f"- Regressors: 6 weather parameters")

# Train the model
print("\n⏳ Training model... (this may take 2-3 minutes)")
model.fit(prophet_df)

print("✅ Model training complete!")

# Create models directory
os.makedirs('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/models', exist_ok=True)

# Save the trained model
model_path = 'D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/models/prophet_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"\n💾 Model saved to: {model_path}")

# Make sample prediction
print("\n🔮 Testing model with sample prediction...")
future = model.make_future_dataframe(periods=24, freq='H')  # Next 24 hours

# Add regressor values for future (using last known values as example)
last_values = prophet_df.iloc[-1]
for col in ['tempC', 'humidity', 'pressure', 'windspeedKmph', 'cloudcover', 'precipMM']:
    future[col] = last_values[col]

forecast = model.predict(future)

print("\n📈 Sample predictions (next 6 hours):")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(6))

print("\n" + "="*80)
print("✅ MODEL TRAINING COMPLETE!")
print("="*80)