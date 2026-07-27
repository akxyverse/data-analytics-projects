"""
ESPORTS & GAMING REVENUE ANALYTICS
Script 02: Data Cleaning
"""

import pandas as pd
import numpy as np

# Load data
print("Loading data...")
df = pd.read_csv("D:\Internship\Project-Esports & Gaming Revenue Analytics System\Raw_Data\global_gaming_esports_2010_2025.csv")

print("✅ Data loaded!")
print(f"Original shape: {df.shape}")

# ========================================
# 1. Check for Missing Values
# ========================================
print("\n--- Missing Values Check ---")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "✅ No missing values!")

# ========================================
# 2. Check for Duplicates
# ========================================
print("\n--- Duplicate Check ---")
duplicates = df.duplicated().sum()
print(f"Duplicate rows: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print(f"✅ Removed {duplicates} duplicates")

# ========================================
# 3. Data Type Validation
# ========================================
print("\n--- Data Types ---")
print(df.dtypes)

# ========================================
# 4. Remove Extra Spaces from Strings
# ========================================
print("\n--- Cleaning String Columns ---")
string_cols = df.select_dtypes(include=['object']).columns

for col in string_cols:
    df[col] = df[col].str.strip()
    
print(f"✅ Cleaned {len(string_cols)} string columns")

# ========================================
# 5. Check for Outliers (Basic)
# ========================================
print("\n--- Outlier Detection (Revenue) ---")
print(f"Gaming Revenue - Min: ${df['Gaming_Revenue_BillionUSD'].min():.2f}B, Max: ${df['Gaming_Revenue_BillionUSD'].max():.2f}B")
print(f"Esports Revenue - Min: ${df['Esports_Revenue_MillionUSD'].min():.2f}M, Max: ${df['Esports_Revenue_MillionUSD'].max():.2f}M")

# ========================================
# 6. Save Cleaned Data
# ========================================
print("\n--- Saving Cleaned Data ---")
output_path = r"D:\Internship\Project-Esports & Gaming Revenue Analytics System\Processed_Data\cleaned_gaming_data.csv"
df.to_csv(output_path, index=False)

print(f"✅ Cleaned data saved!")
print(f"Final shape: {df.shape}")
print("\n🎉 Data Cleaning Complete!")