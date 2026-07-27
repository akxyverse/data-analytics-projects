"""
ESPORTS & GAMING REVENUE ANALYTICS
Script 01: Data Loading & Basic Info
"""

import pandas as pd
import numpy as np

# Load CSV file
print("Loading data...")
df = pd.read_csv("D:\Internship\Project-Esports & Gaming Revenue Analytics System\Raw_Data\global_gaming_esports_2010_2025.csv")

print("\n✅ Data loaded successfully!")
print(f"📊 Total Rows: {df.shape[0]}")
print(f"📊 Total Columns: {df.shape[1]}")

# Display first 5 rows
print("\n--- First 5 Rows ---")
print(df.head())

# Display column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# Basic info
print("\n--- Dataset Info ---")
print(df.info())