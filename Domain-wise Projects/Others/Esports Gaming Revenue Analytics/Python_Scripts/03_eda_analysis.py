"""
ESPORTS & GAMING REVENUE ANALYTICS
Script 03: Exploratory Data Analysis (EDA)
"""

import pandas as pd
import numpy as np

# Load cleaned data
print("Loading cleaned data...")
df = pd.read_csv(r"D:\Internship\Project-Esports & Gaming Revenue Analytics System\Processed_Data\cleaned_gaming_data.csv")

print("✅ Data loaded!")
print(f"Shape: {df.shape}\n")

# ========================================
# 1. BASIC STATISTICS
# ========================================
print("="*60)
print("BASIC STATISTICS")
print("="*60)
print(df.describe())

# ========================================
# 2. YEAR-WISE ANALYSIS
# ========================================
print("\n" + "="*60)
print("YEAR-WISE REVENUE ANALYSIS")
print("="*60)

yearly_analysis = df.groupby('Year').agg({
    'Gaming_Revenue_BillionUSD': 'sum',
    'Esports_Revenue_MillionUSD': 'sum',
    'Active_Players_Million': 'sum',
    'Esports_Viewers_Million': 'sum'
}).round(2)

print(yearly_analysis)

# Year-over-Year Growth
print("\n--- Year-over-Year Growth (Gaming Revenue) ---")
yearly_analysis['YoY_Growth_%'] = yearly_analysis['Gaming_Revenue_BillionUSD'].pct_change() * 100
print(yearly_analysis[['Gaming_Revenue_BillionUSD', 'YoY_Growth_%']])

# ========================================
# 3. COUNTRY-WISE ANALYSIS
# ========================================
print("\n" + "="*60)
print("TOP 10 COUNTRIES BY GAMING REVENUE")
print("="*60)

country_revenue = df.groupby('Country')['Gaming_Revenue_BillionUSD'].sum().sort_values(ascending=False).head(10)
print(country_revenue)

# ========================================
# 4. REGION-WISE ANALYSIS
# ========================================
print("\n" + "="*60)
print("REGION-WISE PERFORMANCE")
print("="*60)

region_analysis = df.groupby('Region').agg({
    'Gaming_Revenue_BillionUSD': 'sum',
    'Esports_Revenue_MillionUSD': 'sum',
    'Active_Players_Million': 'mean',
    'Country': 'count'
}).round(2)

region_analysis.columns = ['Total_Gaming_Revenue_B', 'Total_Esports_Revenue_M', 'Avg_Active_Players_M', 'Country_Count']
print(region_analysis.sort_values('Total_Gaming_Revenue_B', ascending=False))

# ========================================
# 5. GENRE ANALYSIS
# ========================================
print("\n" + "="*60)
print("TOP GENRES ANALYSIS")
print("="*60)

genre_counts = df['Top_Genre'].value_counts()
print(genre_counts)

# ========================================
# 6. PLATFORM ANALYSIS
# ========================================
print("\n" + "="*60)
print("TOP PLATFORMS ANALYSIS")
print("="*60)

platform_counts = df['Top_Platform'].value_counts()
print(platform_counts)

# ========================================
# 7. ESPORTS ANALYSIS
# ========================================
print("\n" + "="*60)
print("ESPORTS METRICS ANALYSIS")
print("="*60)

esports_summary = df[['Esports_Tournaments_Count', 'Pro_Players_Count', 
                       'Esports_Viewers_Million', 'Esports_PrizePool_MillionUSD']].describe()
print(esports_summary)

# ========================================
# 8. CORRELATION ANALYSIS
# ========================================
print("\n" + "="*60)
print("CORRELATION ANALYSIS (Top 5 Relationships)")
print("="*60)

# Select numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()

# Get top correlations
correlation_pairs = correlation_matrix.unstack()
correlation_pairs = correlation_pairs[correlation_pairs < 1]  # Remove self-correlation
top_correlations = correlation_pairs.abs().sort_values(ascending=False).head(10)

print("Top 10 Correlations:")
for idx, value in top_correlations.items():
    print(f"{idx[0]} <-> {idx[1]}: {correlation_pairs[idx]:.3f}")

# ========================================
# 9. COVID IMPACT ANALYSIS
# ========================================
print("\n" + "="*60)
print("COVID IMPACT ANALYSIS (2019-2022)")
print("="*60)

covid_years = df[df['Year'].between(2019, 2022)]
covid_impact = covid_years.groupby('Year').agg({
    'Gaming_Revenue_BillionUSD': 'sum',
    'Active_Players_Million': 'sum',
    'Covid_Impact_Index': 'mean'
}).round(2)

print(covid_impact)

# ========================================
# 10. DEMOGRAPHICS ANALYSIS
# ========================================
print("\n" + "="*60)
print("DEMOGRAPHICS ANALYSIS")
print("="*60)

demographics = df[['Female_Gamer_Percent', 'Mobile_Gaming_Share']].describe()
print(demographics)

print(f"\nAverage Female Gamer Percentage: {df['Female_Gamer_Percent'].mean():.2f}%")
print(f"Average Mobile Gaming Share: {df['Mobile_Gaming_Share'].mean():.2f}%")

# ========================================
# 11. SAVE KEY INSIGHTS
# ========================================
print("\n" + "="*60)
print("SAVING KEY INSIGHTS")
print("="*60)

# Create insights summary
insights = {
    'Total_Gaming_Revenue_Billion': df['Gaming_Revenue_BillionUSD'].sum(),
    'Total_Esports_Revenue_Million': df['Esports_Revenue_MillionUSD'].sum(),
    'Top_Country_by_Revenue': df.groupby('Country')['Gaming_Revenue_BillionUSD'].sum().idxmax(),
    'Top_Region_by_Revenue': df.groupby('Region')['Gaming_Revenue_BillionUSD'].sum().idxmax(),
    'Most_Popular_Genre': df['Top_Genre'].mode()[0],
    'Most_Popular_Platform': df['Top_Platform'].mode()[0],
    'Avg_Female_Gamer_Percent': df['Female_Gamer_Percent'].mean(),
    'Avg_Mobile_Gaming_Share': df['Mobile_Gaming_Share'].mean()
}

insights_df = pd.DataFrame([insights])
insights_df.to_csv(r"D:\Internship\Project-Esports & Gaming Revenue Analytics System\Processed_Data\key_insights.csv", index=False)

print("✅ Key insights saved!")
print("\n🎉 EDA Complete!")