import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/processed/pune_clean.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

print("=" * 80)
print("📊 EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 80)

# 1. BASIC STATISTICS
print("\n1️⃣ DESCRIPTIVE STATISTICS")
print("-" * 80)
print(df.describe())

# 2. DATA DISTRIBUTION
print("\n2️⃣ DATA DISTRIBUTION")
print("-" * 80)
print(f"Mean Temperature: {df['tempC'].mean():.2f}°C")
print(f"Median Temperature: {df['tempC'].median():.2f}°C")
print(f"Std Dev Temperature: {df['tempC'].std():.2f}°C")
print(f"\nMean Humidity: {df['humidity'].mean():.2f}%")
print(f"Median Humidity: {df['humidity'].median():.2f}%")
print(f"Std Dev Humidity: {df['humidity'].std():.2f}%")

# 3. OUTLIER DETECTION
print("\n3️⃣ OUTLIER DETECTION (IQR Method)")
print("-" * 80)

def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return len(outliers), lower_bound, upper_bound

for col in ['tempC', 'humidity', 'pressure', 'windspeedKmph']:
    outlier_count, lower, upper = detect_outliers(df, col)
    print(f"{col}: {outlier_count} outliers (Range: {lower:.2f} to {upper:.2f})")

# 4. CORRELATION ANALYSIS
print("\n4️⃣ CORRELATION WITH THUNDERSTORM")
print("-" * 80)
correlation = df[['tempC', 'humidity', 'pressure', 'windspeedKmph', 'cloudcover', 'precipMM']].corrwith(df['thunderstorm'])
print(correlation.sort_values(ascending=False))

# 5. TEMPORAL PATTERNS
print("\n5️⃣ TEMPORAL PATTERNS")
print("-" * 80)
df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month
df['hour'] = df['date_time'].dt.hour

print("\nThunderstorms by Year:")
print(df.groupby('year')['thunderstorm'].sum())

print("\nThunderstorms by Month:")
print(df.groupby('month')['thunderstorm'].sum())

print("\nThunderstorms by Hour of Day:")
print(df.groupby('hour')['thunderstorm'].sum().sort_values(ascending=False).head(5))

# 6. THUNDERSTORM CONDITIONS
print("\n6️⃣ AVERAGE CONDITIONS DURING THUNDERSTORMS")
print("-" * 80)
storm_data = df[df['thunderstorm'] == 1]
no_storm_data = df[df['thunderstorm'] == 0]

print(f"\n{'Parameter':<20} {'Thunderstorm':>15} {'No Thunderstorm':>18} {'Difference':>15}")
print("-" * 70)

params = ['tempC', 'humidity', 'pressure', 'windspeedKmph', 'cloudcover', 'precipMM']
for param in params:
    storm_mean = storm_data[param].mean()
    no_storm_mean = no_storm_data[param].mean()
    diff = storm_mean - no_storm_mean
    print(f"{param:<20} {storm_mean:>15.2f} {no_storm_mean:>18.2f} {diff:>15.2f}")

# 7. DATA QUALITY CHECK
print("\n7️⃣ DATA QUALITY METRICS")
print("-" * 80)
print(f"Total Records: {len(df)}")
print(f"Duplicate Records: {df.duplicated().sum()}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Data Completeness: {((1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100):.2f}%")

print("\n" + "=" * 80)
print("✅ EDA COMPLETE!")
print("=" * 80)