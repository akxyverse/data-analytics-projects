import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_data.csv')

print("="*60)
print("AGENT PERFORMANCE ANALYTICS")
print("="*60)

# 1. Agent Rating Distribution
print("\n1. AGENT RATING DISTRIBUTION:")
print(f"   Average Rating: {df['Agent_Rating'].mean():.2f}")
print(f"   Median Rating: {df['Agent_Rating'].median():.2f}")
print(f"   Highest Rating: {df['Agent_Rating'].max()}")
print(f"   Lowest Rating: {df['Agent_Rating'].min()}")
print("\n   Rating Distribution:")
rating_dist = df['Agent_Rating'].value_counts().sort_index()
for rating, count in rating_dist.items():
    print(f"   {rating}: {count} agents ({count/len(df)*100:.1f}%)")

# 2. Age Groups Analysis
print("\n2. AGENT PERFORMANCE BY AGE GROUP:")
# Create age groups
df['Age_Group'] = pd.cut(df['Agent_Age'], 
                          bins=[15, 25, 35, 45, 50], 
                          labels=['15-25', '26-35', '36-45', '46-50'])

age_performance = df.groupby('Age_Group').agg({
    'Agent_Rating': 'mean',
    'Delivery_Time': 'mean',
    'Order_ID': 'count'
}).round(2)
age_performance.columns = ['Avg_Rating', 'Avg_Delivery_Time', 'Total_Orders']
print(age_performance)

# 3. Rating vs Delivery Time Correlation
print("\n3. RATING vs DELIVERY TIME:")
rating_delivery = df.groupby('Agent_Rating')['Delivery_Time'].mean().round(2)
print(rating_delivery)
print(f"\n   Correlation: {df['Agent_Rating'].corr(df['Delivery_Time']):.4f}")
if df['Agent_Rating'].corr(df['Delivery_Time']) < 0:
    print("   → Higher ratings = Faster deliveries ✅")
else:
    print("   → Higher ratings = Slower deliveries ⚠️")

# 4. Best Performing Agents (by rating groups)
print("\n4. HIGH vs LOW RATED AGENTS COMPARISON:")
high_rated = df[df['Agent_Rating'] >= 4.5]
low_rated = df[df['Agent_Rating'] < 4.0]

print(f"\n   High Rated Agents (≥4.5):")
print(f"   - Count: {len(high_rated)}")
print(f"   - Avg Delivery Time: {high_rated['Delivery_Time'].mean():.2f} min")
print(f"   - Avg Age: {high_rated['Agent_Age'].mean():.1f} years")

print(f"\n   Low Rated Agents (<4.0):")
print(f"   - Count: {len(low_rated)}")
print(f"   - Avg Delivery Time: {low_rated['Delivery_Time'].mean():.2f} min")
print(f"   - Avg Age: {low_rated['Agent_Age'].mean():.1f} years")

# 5. Agent Performance by Vehicle
print("\n5. AGENT RATINGS BY VEHICLE TYPE:")
vehicle_ratings = df.groupby('Vehicle')['Agent_Rating'].agg([
    ('Avg_Rating', 'mean'),
    ('Count', 'count')
]).round(2)
print(vehicle_ratings)

# 6. Weather Impact on Agent Performance
print("\n6. AGENT PERFORMANCE IN DIFFERENT WEATHER:")
weather_agent = df.groupby('Weather').agg({
    'Agent_Rating': 'mean',
    'Delivery_Time': 'mean'
}).round(2)
weather_agent.columns = ['Avg_Rating', 'Avg_Delivery_Time']
print(weather_agent)

print("\n" + "="*60)
print("✅ Agent Analytics Complete!")
print("="*60)