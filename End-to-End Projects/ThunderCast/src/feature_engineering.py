import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/processed/pune_clean.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

print("🔧 Starting Feature Engineering...")

# 1. TIME-BASED FEATURES
df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month
df['day'] = df['date_time'].dt.day
df['hour'] = df['date_time'].dt.hour
df['day_of_week'] = df['date_time'].dt.dayofweek  # 0=Monday, 6=Sunday
df['day_of_year'] = df['date_time'].dt.dayofyear

# Season mapping
def get_season(month):
    if month in [3, 4, 5]:
        return 'summer'
    elif month in [6, 7, 8, 9]:
        return 'monsoon'
    elif month in [10, 11]:
        return 'post_monsoon'
    else:
        return 'winter'

df['season'] = df['month'].apply(get_season)

print("✅ Time-based features created")

# 2. INTERACTION FEATURES
df['temp_humidity'] = df['tempC'] * df['humidity']
df['pressure_wind'] = df['pressure'] * df['windspeedKmph']
df['humidity_pressure_ratio'] = df['humidity'] / df['pressure']

print("✅ Interaction features created")

# 3. LAG FEATURES (Previous hour values)
df['temp_lag_1h'] = df['tempC'].shift(1)
df['humidity_lag_1h'] = df['humidity'].shift(1)
df['pressure_lag_1h'] = df['pressure'].shift(1)

# Change features
df['temp_change'] = df['tempC'] - df['temp_lag_1h']
df['pressure_change'] = df['pressure'] - df['pressure_lag_1h']

print("✅ Lag and change features created")

# 4. ROLLING STATISTICS (Moving averages)
df['temp_rolling_3h'] = df['tempC'].rolling(window=3, min_periods=1).mean()
df['humidity_rolling_3h'] = df['humidity'].rolling(window=3, min_periods=1).mean()
df['pressure_rolling_6h'] = df['pressure'].rolling(window=6, min_periods=1).mean()

df['temp_rolling_std_3h'] = df['tempC'].rolling(window=3, min_periods=1).std()

print("✅ Rolling statistics features created")

# 5. CYCLICAL FEATURES (for hour and month)
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

print("✅ Cyclical features created")

# 6. DROP NaN rows created by lag/rolling features
df = df.dropna()

print(f"\n📊 Feature Engineering Summary:")
print(f"Total features: {df.shape[1]}")
print(f"Total rows after cleaning: {df.shape[0]}")
print(f"\nNew features added:")
new_features = [col for col in df.columns if col not in ['date_time', 'tempC', 'humidity', 'pressure', 
                                                           'windspeedKmph', 'cloudcover', 'precipMM', 'thunderstorm']]
for i, feat in enumerate(new_features, 1):
    print(f"{i}. {feat}")

# Save engineered data
df.to_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/processed/pune_featured.csv', index=False)

print("\n✅ Feature-engineered data saved to data/processed/pune_featured.csv")