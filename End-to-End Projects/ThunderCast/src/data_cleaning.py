import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/raw/pune.csv')

print("🧹 Starting data cleaning...")

# Convert date_time to datetime
df['date_time'] = pd.to_datetime(df['date_time'])

# Select relevant columns for thunderstorm prediction
columns_needed = ['date_time', 'tempC', 'humidity', 'pressure', 
                  'windspeedKmph', 'cloudcover', 'precipMM']

df_clean = df[columns_needed].copy()

# Create target variable: Thunderstorm indicator
# High precipitation + high humidity + low pressure = likely thunderstorm
df_clean['thunderstorm'] = (
    (df_clean['precipMM'] > 5) & 
    (df_clean['humidity'] > 70) & 
    (df_clean['pressure'] < 1010)
).astype(int)

# Check for missing values
print("\n📊 Missing values:")
print(df_clean.isnull().sum())

# Basic statistics
print("\n📈 Dataset Statistics:")
print(df_clean.describe())


# Save cleaned data
df_clean.to_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/processed/pune_clean.csv', index=False)

print("\n✅ Cleaned data saved to data/processed/pune_clean.csv")
print(f"Total rows: {len(df_clean)}")
print(f"Thunderstorm cases: {df_clean['thunderstorm'].sum()}")
print(f"Thunderstorm percentage: {(df_clean['thunderstorm'].sum() / len(df_clean) * 100):.2f}%")