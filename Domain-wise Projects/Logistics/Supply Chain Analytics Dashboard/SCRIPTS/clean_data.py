import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/amazon_delivery.csv')

print("BEFORE CLEANING:")
print(f"Total rows: {len(df)}")
print(f"Missing values:\n{df.isnull().sum()}\n")

# 1. Remove extra spaces from categorical columns
df['Traffic'] = df['Traffic'].str.strip()
df['Vehicle'] = df['Vehicle'].str.strip()
df['Weather'] = df['Weather'].str.strip()
df['Order_Time'] = df['Order_Time'].str.strip()
df['Pickup_Time'] = df['Pickup_Time'].str.strip()

# 2. Replace 'NaN' string with actual NaN
df['Traffic'] = df['Traffic'].replace('NaN', np.nan)
df['Order_Time'] = df['Order_Time'].replace('NaN', np.nan)
df['Pickup_Time'] = df['Pickup_Time'].replace('NaN', np.nan)

# 3. Fill missing Agent_Rating with median
df['Agent_Rating'] = df['Agent_Rating'].fillna(df['Agent_Rating'].median())

# 4. Fill missing Weather with mode (most common)
df['Weather'] = df['Weather'].fillna(df['Weather'].mode()[0])

# 5. Fill missing Traffic with mode
df['Traffic'] = df['Traffic'].fillna(df['Traffic'].mode()[0])

# 6. Fill missing Order_Time with mode (most common time)
df['Order_Time'] = df['Order_Time'].fillna(df['Order_Time'].mode()[0])

# 7. Convert date column
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# 8. Create new useful columns
df['Order_Day'] = df['Order_Date'].dt.day_name()
df['Order_Month'] = df['Order_Date'].dt.month_name()
df['Order_Hour'] = df['Order_Time'].str.split(':').str[0].astype(int)

print("\nAFTER CLEANING:")
print(f"Total rows: {len(df)}")
print(f"Missing values:\n{df.isnull().sum()}\n")

print("\nCleaned categorical values:")
print(f"Traffic: {df['Traffic'].unique()}")
print(f"Vehicle: {df['Vehicle'].unique()}")
print(f"Weather: {df['Weather'].unique()}")

# Save cleaned data
df.to_csv('data/processed/cleaned_data.csv', index=False)
print("\n✅ Cleaned data saved to: data/processed/cleaned_data.csv")