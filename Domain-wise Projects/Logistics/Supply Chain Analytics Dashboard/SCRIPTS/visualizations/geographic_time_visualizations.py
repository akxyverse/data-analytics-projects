import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Create separate output folder for geographic/time charts
os.makedirs('reports/visualizations/geographic_time_analysis', exist_ok=True)

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_data.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("Creating Geographic & Time-Based Visualizations...")

# 1. Area-wise Performance Comparison
plt.figure(figsize=(12, 6))
area_stats = df.groupby('Area').agg({
    'Order_ID': 'count',
    'Delivery_Time': 'mean'
}).sort_values('Order_ID', ascending=False)

fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

x_pos = np.arange(len(area_stats))
bar1 = ax1.bar(x_pos - 0.2, area_stats['Order_ID'], 0.4, label='Order Count', color='skyblue', alpha=0.8)
bar2 = ax2.bar(x_pos + 0.2, area_stats['Delivery_Time'], 0.4, label='Avg Delivery Time', color='coral', alpha=0.8)

ax1.set_xlabel('Area', fontsize=12)
ax1.set_ylabel('Order Count', fontsize=12, color='skyblue')
ax2.set_ylabel('Average Delivery Time (min)', fontsize=12, color='coral')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(area_stats.index)
ax1.tick_params(axis='y', labelcolor='skyblue')
ax2.tick_params(axis='y', labelcolor='coral')

plt.title('Area-wise Orders and Delivery Performance', fontsize=16, fontweight='bold')
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/01_area_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 1: Area Performance")

# 2. Day of Week Analysis
plt.figure(figsize=(12, 6))
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_stats = df.groupby('Order_Day')['Order_ID'].count().reindex(day_order)

colors_days = plt.cm.viridis(np.linspace(0, 1, len(day_stats)))
bars = plt.bar(day_stats.index, day_stats.values, color=colors_days, edgecolor='black')
plt.title('Orders by Day of Week', fontsize=16, fontweight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(rotation=45)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/02_orders_by_day.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 2: Orders by Day")

# 3. Average Delivery Time by Day
plt.figure(figsize=(12, 6))
day_delivery = df.groupby('Order_Day')['Delivery_Time'].mean().reindex(day_order)
plt.plot(day_delivery.index, day_delivery.values, marker='o', linewidth=3, markersize=10, color='darkgreen')
plt.fill_between(range(len(day_delivery)), day_delivery.values, alpha=0.3, color='lightgreen')
plt.title('Average Delivery Time by Day of Week', fontsize=16, fontweight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Average Delivery Time (minutes)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/03_delivery_time_by_day.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 3: Delivery Time by Day")

# 4. Hourly Order Volume
plt.figure(figsize=(14, 6))
hourly_orders = df.groupby('Order_Hour')['Order_ID'].count().sort_index()
colors_hour = ['red' if x >= hourly_orders.mean() else 'lightblue' for x in hourly_orders.values]
plt.bar(hourly_orders.index, hourly_orders.values, color=colors_hour, edgecolor='black')
plt.axhline(y=hourly_orders.mean(), color='red', linestyle='--', linewidth=2, label=f'Average: {hourly_orders.mean():.0f}')
plt.title('Order Volume by Hour of Day', fontsize=16, fontweight='bold')
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/04_hourly_order_volume.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 4: Hourly Order Volume")

# 5. Top Categories by Area
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
areas = df['Area'].unique()

for idx, area in enumerate(areas):
    row = idx // 2
    col = idx % 2
    area_data = df[df['Area'] == area]
    top_categories = area_data['Category'].value_counts().head(5)
    
    axes[row, col].barh(top_categories.index, top_categories.values, color='teal', alpha=0.7)
    axes[row, col].set_title(f'Top 5 Categories in {area}', fontsize=14, fontweight='bold')
    axes[row, col].set_xlabel('Number of Orders', fontsize=11)
    for i, v in enumerate(top_categories.values):
        axes[row, col].text(v + 20, i, str(v), va='center')

plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/05_categories_by_area.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 5: Categories by Area")

# 6. Distance vs Delivery Time
df['Distance'] = np.sqrt(
    (df['Drop_Latitude'] - df['Store_Latitude'])**2 + 
    (df['Drop_Longitude'] - df['Store_Longitude'])**2
) * 111

plt.figure(figsize=(12, 6))
plt.hexbin(df['Distance'], df['Delivery_Time'], gridsize=30, cmap='YlOrRd', mincnt=1)
plt.colorbar(label='Number of Orders')
plt.title('Distance vs Delivery Time', fontsize=16, fontweight='bold')
plt.xlabel('Distance (km)', fontsize=12)
plt.ylabel('Delivery Time (minutes)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/06_distance_vs_time.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 6: Distance vs Delivery Time")

# 7. Vehicle Efficiency
plt.figure(figsize=(12, 6))
vehicle_efficiency = df.groupby('Vehicle').agg({
    'Distance': 'mean',
    'Delivery_Time': 'mean'
}).reset_index()
vehicle_efficiency['Speed_km_h'] = (vehicle_efficiency['Distance'] / vehicle_efficiency['Delivery_Time'] * 60).round(2)

sns.barplot(data=vehicle_efficiency, x='Vehicle', y='Speed_km_h', palette='rocket')
plt.title('Average Vehicle Speed (km/h)', fontsize=16, fontweight='bold')
plt.xlabel('Vehicle Type', fontsize=12)
plt.ylabel('Average Speed (km/h)', fontsize=12)
for i, row in vehicle_efficiency.iterrows():
    plt.text(i, row['Speed_km_h'] + 0.5, f"{row['Speed_km_h']:.1f}", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/07_vehicle_efficiency.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 7: Vehicle Efficiency")

# 8. Monthly Trend
plt.figure(figsize=(14, 6))
df['Month'] = df['Order_Date'].dt.month
monthly_orders = df.groupby('Month')['Order_ID'].count()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_labels = [month_names[i-1] for i in monthly_orders.index]

plt.plot(month_labels, monthly_orders.values, marker='o', linewidth=3, markersize=12, color='purple')
plt.fill_between(range(len(monthly_orders)), monthly_orders.values, alpha=0.3, color='lavender')
plt.title('Monthly Order Trends', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/visualizations/geographic_time_analysis/08_monthly_trends.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 8: Monthly Trends")

print("\n" + "="*60)
print("✅ All Geographic & Time Visualizations Created!")
print("📁 Location: reports/visualizations/geographic_time_analysis/")
print("="*60)