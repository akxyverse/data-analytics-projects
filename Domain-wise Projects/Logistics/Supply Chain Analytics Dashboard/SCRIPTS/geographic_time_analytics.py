import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_data.csv')

print("="*60)
print("GEOGRAPHIC & TIME-BASED ANALYTICS")
print("="*60)

# 1. Area-wise Performance
print("\n1. AREA-WISE DETAILED ANALYSIS:")
area_stats = df.groupby('Area').agg({
    'Order_ID': 'count',
    'Delivery_Time': ['mean', 'min', 'max'],
    'Agent_Rating': 'mean'
}).round(2)
area_stats.columns = ['Total_Orders', 'Avg_Delivery', 'Min_Delivery', 'Max_Delivery', 'Avg_Rating']
print(area_stats)

# 2. Day of Week Analysis
print("\n2. ORDERS BY DAY OF WEEK:")
day_orders = df['Order_Day'].value_counts()
print(day_orders)
print(f"\n   Busiest Day: {day_orders.idxmax()} ({day_orders.max()} orders)")
print(f"   Slowest Day: {day_orders.idxmin()} ({day_orders.min()} orders)")

# 3. Delivery Time by Day
print("\n3. AVERAGE DELIVERY TIME BY DAY:")
day_delivery = df.groupby('Order_Day')['Delivery_Time'].mean().round(2).sort_values()
print(day_delivery)

# 4. Monthly Analysis
print("\n4. ORDERS BY MONTH:")
month_orders = df['Order_Month'].value_counts()
print(month_orders)

# 5. Hourly Patterns
print("\n5. PEAK HOURS ANALYSIS:")
hourly_stats = df.groupby('Order_Hour').agg({
    'Order_ID': 'count',
    'Delivery_Time': 'mean'
}).round(2)
hourly_stats.columns = ['Order_Count', 'Avg_Delivery_Time']
hourly_stats = hourly_stats.sort_values('Order_Count', ascending=False)
print("\nTop 10 Busiest Hours:")
print(hourly_stats.head(10))

# 6. Category Performance by Area
print("\n6. TOP CATEGORIES BY AREA:")
for area in df['Area'].unique():
    area_data = df[df['Area'] == area]
    top_categories = area_data['Category'].value_counts().head(3)
    print(f"\n   {area}:")
    for cat, count in top_categories.items():
        print(f"   - {cat}: {count} orders")

# 7. Weather-Traffic Combination Analysis
print("\n7. WEATHER + TRAFFIC IMPACT:")
weather_traffic = df.groupby(['Weather', 'Traffic'])['Delivery_Time'].mean().round(2)
print(weather_traffic.sort_values(ascending=False).head(10))

# 8. Distance Analysis (using coordinates)
print("\n8. DELIVERY DISTANCE ANALYSIS:")
# Calculate approximate distance using latitude/longitude
df['Distance'] = np.sqrt(
    (df['Drop_Latitude'] - df['Store_Latitude'])**2 + 
    (df['Drop_Longitude'] - df['Store_Longitude'])**2
) * 111  # Rough conversion to km

distance_stats = df['Distance'].describe().round(2)
print(distance_stats)

print(f"\n   Average Distance: {df['Distance'].mean():.2f} km")
print(f"   Correlation with Delivery Time: {df['Distance'].corr(df['Delivery_Time']):.4f}")

# 9. Vehicle Efficiency by Distance
print("\n9. VEHICLE EFFICIENCY BY DISTANCE:")
vehicle_distance = df.groupby('Vehicle').agg({
    'Distance': 'mean',
    'Delivery_Time': 'mean'
}).round(2)
vehicle_distance['Efficiency'] = (vehicle_distance['Distance'] / vehicle_distance['Delivery_Time'] * 60).round(2)
vehicle_distance.columns = ['Avg_Distance_km', 'Avg_Time_min', 'Speed_km/h']
print(vehicle_distance)

print("\n" + "="*60)
print("✅ Geographic & Time Analytics Complete!")
print("="*60)