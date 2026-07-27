import pandas as pd

# Load the CSV file
df = pd.read_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/raw/pune.csv')
# Check first few rows
print("📊 Dataset Preview:")
print(df.head())

print("\n📋 Dataset Info:")
print(df.info())

print("\n📈 Dataset Shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n🔤 Column Names:")
print(df.columns.tolist())