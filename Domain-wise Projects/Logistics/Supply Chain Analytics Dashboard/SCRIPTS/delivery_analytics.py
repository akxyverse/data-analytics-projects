import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_data.csv')

print("="*60)
print("DELIVERY PERFORMANCE ANALYTICS")
print("="*60)

# 1. Overall Delivery Metrics
print("\n1. OVERALL DELIVERY METRICS:")
print(f"   Total Orders: {len(df):,}")
print(f"   Average Delivery Time: {df['Delivery_Time'].mean():.2f} minutes")
print(f"   Median Delivery Time: {df['Delivery_Time'].median():.2f} minutes")
print(f"   Min Delivery Time: {df['Delivery_Time'].min()} minutes")
print(f"   Max Delivery Time: {df['Delivery_Time'].max()} minutes")
print(f"   Std Deviation: {df['Delivery_Time'].std():.2f} minutes")

# 2. Delivery Time by Vehicle Type
print("\n2. DELIVERY TIME BY VEHICLE TYPE:")
vehicle_analysis = df.groupby('Vehicle')['Delivery_Time'].agg([
    ('Count', 'count'),
    ('Avg_Time', 'mean'),
    ('Min_Time', 'min'),
    ('Max_Time', 'max')
]).round(2)
print(vehicle_analysis)

# 3. Delivery Time by Weather Condition
print("\n3. DELIVERY TIME BY WEATHER CONDITION:")
weather_analysis = df.groupby('Weather')['Delivery_Time'].agg([
    ('Count', 'count'),
    ('Avg_Time', 'mean')
]).sort_values('Avg_Time', ascending=False).round(2)
print(weather_analysis)

# 4. Delivery Time by Traffic Condition
print("\n4. DELIVERY TIME BY TRAFFIC CONDITION:")
traffic_analysis = df.groupby('Traffic')['Delivery_Time'].agg([
    ('Count', 'count'),
    ('Avg_Time', 'mean')
]).sort_values('Avg_Time', ascending=False).round(2)
print(traffic_analysis)

# 5. Delivery Time by Area
print("\n5. DELIVERY TIME BY AREA:")
area_analysis = df.groupby('Area')['Delivery_Time'].agg([
    ('Count', 'count'),
    ('Avg_Time', 'mean'),
    ('Min_Time', 'min'),
    ('Max_Time', 'max')
]).round(2)
print(area_analysis)

# 6. Delivery Time by Product Category
print("\n6. TOP 5 FASTEST & SLOWEST CATEGORIES:")
category_analysis = df.groupby('Category')['Delivery_Time'].mean().round(2)
print("\nFastest Deliveries:")
print(category_analysis.nsmallest(5))
print("\nSlowest Deliveries:")
print(category_analysis.nlargest(5))

# 7. Peak Delivery Hours
print("\n7. BUSIEST DELIVERY HOURS:")
hour_analysis = df.groupby('Order_Hour')['Order_ID'].count().sort_values(ascending=False).head(5)
print(hour_analysis)

print("\n" + "="*60)
print("✅ Delivery Analytics Complete!")
print("="*60)