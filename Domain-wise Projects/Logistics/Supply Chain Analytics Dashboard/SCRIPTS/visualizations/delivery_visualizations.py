import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Create separate output folder for delivery charts
os.makedirs('reports/visualizations/delivery_performance', exist_ok=True)

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_data.csv')

print("Creating Delivery Performance Visualizations...")

# 1. Delivery Time Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Delivery_Time', bins=30, kde=True, color='steelblue')
plt.title('Distribution of Delivery Times', fontsize=16, fontweight='bold')
plt.xlabel('Delivery Time (minutes)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/01_delivery_time_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 1: Delivery Time Distribution")

# 2. Delivery Time by Vehicle Type
plt.figure(figsize=(10, 6))
vehicle_avg = df.groupby('Vehicle')['Delivery_Time'].mean().sort_values()
sns.barplot(x=vehicle_avg.values, y=vehicle_avg.index, palette='viridis')
plt.title('Average Delivery Time by Vehicle Type', fontsize=16, fontweight='bold')
plt.xlabel('Average Delivery Time (minutes)', fontsize=12)
plt.ylabel('Vehicle Type', fontsize=12)
for i, v in enumerate(vehicle_avg.values):
    plt.text(v + 1, i, f'{v:.1f}', va='center')
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/02_delivery_by_vehicle.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 2: Delivery by Vehicle")

# 3. Weather Impact on Delivery Time
plt.figure(figsize=(10, 6))
weather_avg = df.groupby('Weather')['Delivery_Time'].mean().sort_values(ascending=False)
sns.barplot(x=weather_avg.index, y=weather_avg.values, palette='coolwarm')
plt.title('Impact of Weather on Delivery Time', fontsize=16, fontweight='bold')
plt.xlabel('Weather Condition', fontsize=12)
plt.ylabel('Average Delivery Time (minutes)', fontsize=12)
plt.xticks(rotation=45)
for i, v in enumerate(weather_avg.values):
    plt.text(i, v + 1, f'{v:.1f}', ha='center')
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/03_weather_impact.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 3: Weather Impact")

# 4. Traffic Impact on Delivery Time
plt.figure(figsize=(10, 6))
traffic_avg = df.groupby('Traffic')['Delivery_Time'].mean().sort_values(ascending=False)
sns.barplot(x=traffic_avg.index, y=traffic_avg.values, palette='Reds_r')
plt.title('Impact of Traffic on Delivery Time', fontsize=16, fontweight='bold')
plt.xlabel('Traffic Condition', fontsize=12)
plt.ylabel('Average Delivery Time (minutes)', fontsize=12)
for i, v in enumerate(traffic_avg.values):
    plt.text(i, v + 1, f'{v:.1f}', ha='center')
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/04_traffic_impact.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 4: Traffic Impact")

# 5. Orders by Area (Pie Chart)
plt.figure(figsize=(10, 8))
area_counts = df['Area'].value_counts()
colors = sns.color_palette('pastel')[0:len(area_counts)]
plt.pie(area_counts.values, labels=area_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('Order Distribution by Area', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/05_orders_by_area.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 5: Orders by Area")

# 6. Top 10 Categories
plt.figure(figsize=(12, 8))
category_counts = df['Category'].value_counts().head(10)
sns.barplot(y=category_counts.index, x=category_counts.values, palette='mako')
plt.title('Top 10 Product Categories', fontsize=16, fontweight='bold')
plt.xlabel('Number of Orders', fontsize=12)
plt.ylabel('Category', fontsize=12)
for i, v in enumerate(category_counts.values):
    plt.text(v + 50, i, str(v), va='center')
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/06_top_categories.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 6: Top Categories")

# 7. Hourly Order Pattern
plt.figure(figsize=(14, 6))
hourly_orders = df.groupby('Order_Hour')['Order_ID'].count()
plt.plot(hourly_orders.index, hourly_orders.values, marker='o', linewidth=2, 
         markersize=8, color='darkblue')
plt.fill_between(hourly_orders.index, hourly_orders.values, alpha=0.3)
plt.title('Order Volume by Hour of Day', fontsize=16, fontweight='bold')
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/07_hourly_pattern.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 7: Hourly Pattern")

# 8. Weather + Traffic Heatmap
plt.figure(figsize=(10, 8))
weather_traffic = df.groupby(['Weather', 'Traffic'])['Delivery_Time'].mean().unstack()
sns.heatmap(weather_traffic, annot=True, fmt='.1f', cmap='RdYlGn_r', 
            cbar_kws={'label': 'Avg Delivery Time (min)'})
plt.title('Delivery Time: Weather vs Traffic', fontsize=16, fontweight='bold')
plt.xlabel('Traffic Condition', fontsize=12)
plt.ylabel('Weather Condition', fontsize=12)
plt.tight_layout()
plt.savefig('reports/visualizations/delivery_performance/08_weather_traffic_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 8: Weather-Traffic Heatmap")

print("\n" + "="*60)
print("✅ All Delivery Visualizations Created!")
print("📁 Location: reports/visualizations/delivery_performance/")
print("="*60)