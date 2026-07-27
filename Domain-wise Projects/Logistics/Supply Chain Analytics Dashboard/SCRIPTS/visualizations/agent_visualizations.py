import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Create separate output folder for agent charts
os.makedirs('reports/visualizations/agent_performance', exist_ok=True)

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_data.csv')

print("Creating Agent Performance Visualizations...")

# 1. Agent Rating Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Agent_Rating', bins=25, kde=True, color='green')
plt.title('Distribution of Agent Ratings', fontsize=16, fontweight='bold')
plt.xlabel('Agent Rating', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.axvline(df['Agent_Rating'].mean(), color='red', linestyle='--', 
            label=f'Mean: {df["Agent_Rating"].mean():.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/01_agent_rating_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 1: Agent Rating Distribution")

# 2. Agent Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Agent_Age', bins=20, kde=True, color='coral')
plt.title('Distribution of Agent Ages', fontsize=16, fontweight='bold')
plt.xlabel('Agent Age (years)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.axvline(df['Agent_Age'].mean(), color='blue', linestyle='--', 
            label=f'Mean: {df["Agent_Age"].mean():.1f}')
plt.legend()
plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/02_agent_age_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 2: Agent Age Distribution")

# 3. Age vs Rating Scatter Plot
plt.figure(figsize=(12, 6))
age_rating = df.groupby('Agent_Age').agg({
    'Agent_Rating': 'mean',
    'Order_ID': 'count'
}).reset_index()

plt.scatter(age_rating['Agent_Age'], age_rating['Agent_Rating'], 
           s=age_rating['Order_ID']*0.5, alpha=0.6, c=age_rating['Agent_Rating'],
           cmap='RdYlGn', edgecolors='black', linewidth=0.5)
plt.colorbar(label='Rating')
plt.title('Agent Age vs Average Rating (Size = Order Count)', fontsize=16, fontweight='bold')
plt.xlabel('Agent Age', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/03_age_vs_rating.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 3: Age vs Rating")

# 4. Rating vs Delivery Time
plt.figure(figsize=(12, 6))
rating_delivery = df.groupby('Agent_Rating')['Delivery_Time'].mean().reset_index()
plt.plot(rating_delivery['Agent_Rating'], rating_delivery['Delivery_Time'], 
         marker='o', linewidth=2, markersize=8, color='purple')
plt.title('Agent Rating vs Average Delivery Time', fontsize=16, fontweight='bold')
plt.xlabel('Agent Rating', fontsize=12)
plt.ylabel('Average Delivery Time (minutes)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/04_rating_vs_delivery_time.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 4: Rating vs Delivery Time")

# 5. Agent Performance by Age Group
df['Age_Group'] = pd.cut(df['Agent_Age'], 
                          bins=[15, 25, 35, 45, 50], 
                          labels=['15-25', '26-35', '36-45', '46-50'])

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Rating by Age Group
age_group_rating = df.groupby('Age_Group')['Agent_Rating'].mean()
sns.barplot(x=age_group_rating.index, y=age_group_rating.values, 
            palette='Blues_d', ax=axes[0])
axes[0].set_title('Average Rating by Age Group', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Age Group', fontsize=12)
axes[0].set_ylabel('Average Rating', fontsize=12)
for i, v in enumerate(age_group_rating.values):
    axes[0].text(i, v + 0.02, f'{v:.2f}', ha='center')

# Delivery Time by Age Group
age_group_delivery = df.groupby('Age_Group')['Delivery_Time'].mean()
sns.barplot(x=age_group_delivery.index, y=age_group_delivery.values, 
            palette='Reds_d', ax=axes[1])
axes[1].set_title('Average Delivery Time by Age Group', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Age Group', fontsize=12)
axes[1].set_ylabel('Average Delivery Time (min)', fontsize=12)
for i, v in enumerate(age_group_delivery.values):
    axes[1].text(i, v + 1, f'{v:.1f}', ha='center')

plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/05_age_group_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 5: Age Group Performance")

# 6. Agent Ratings by Vehicle Type
plt.figure(figsize=(10, 6))
vehicle_rating = df.groupby('Vehicle')['Agent_Rating'].mean().sort_values(ascending=False)
sns.barplot(x=vehicle_rating.index, y=vehicle_rating.values, palette='Greens_d')
plt.title('Average Agent Rating by Vehicle Type', fontsize=16, fontweight='bold')
plt.xlabel('Vehicle Type', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
for i, v in enumerate(vehicle_rating.values):
    plt.text(i, v + 0.02, f'{v:.2f}', ha='center')
plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/06_rating_by_vehicle.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 6: Rating by Vehicle")

# 7. High vs Low Rated Agents Comparison
high_rated = df[df['Agent_Rating'] >= 4.5]
low_rated = df[df['Agent_Rating'] < 4.0]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Count Comparison
categories = ['High Rated\n(≥4.5)', 'Low Rated\n(<4.0)']
counts = [len(high_rated), len(low_rated)]
colors_bar = ['green', 'red']
axes[0].bar(categories, counts, color=colors_bar, alpha=0.7, edgecolor='black')
axes[0].set_title('Agent Count Comparison', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Number of Orders', fontsize=12)
for i, v in enumerate(counts):
    axes[0].text(i, v + 100, str(v), ha='center', fontweight='bold')

# Delivery Time Comparison
delivery_times = [high_rated['Delivery_Time'].mean(), low_rated['Delivery_Time'].mean()]
axes[1].bar(categories, delivery_times, color=colors_bar, alpha=0.7, edgecolor='black')
axes[1].set_title('Average Delivery Time Comparison', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Average Delivery Time (minutes)', fontsize=12)
for i, v in enumerate(delivery_times):
    axes[1].text(i, v + 1, f'{v:.1f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('reports/visualizations/agent_performance/07_high_vs_low_rated.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Chart 7: High vs Low Rated Comparison")

print("\n" + "="*60)
print("✅ All Agent Visualizations Created!")
print("📁 Location: reports/visualizations/agent_performance/")
print("="*60)