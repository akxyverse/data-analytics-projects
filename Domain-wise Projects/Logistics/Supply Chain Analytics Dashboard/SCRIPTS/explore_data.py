import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('data/amazon_delivery.csv')

# Basic Information
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print("\nColumn Names:")
print(df.columns.tolist())

print("\n" + "=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)
print(df.dtypes)

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("BASIC STATISTICS")
print("=" * 50)
print(df.describe())

print("\n" + "=" * 50)
print("UNIQUE VALUES IN CATEGORICAL COLUMNS")
print("=" * 50)
print(f"Weather Types: {df['Weather'].unique()}")
print(f"Traffic Conditions: {df['Traffic'].unique()}")
print(f"Vehicle Types: {df['Vehicle'].unique()}")
print(f"Areas: {df['Area'].nunique()} unique areas")
print(f"Categories: {df['Category'].unique()}")