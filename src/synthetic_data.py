import pandas as pd
import numpy as np

np.random.seed(42)
CURRENT_YEAR = 2025

# load the dataset
df = pd.read_csv('../data/Mobiles_2025.csv', encoding='latin1')

#1. Clean and prepare the base dataset
#convert the usd price column to numeric
df['Launched Price (USA)'] = (
    df['Launched Price (USA)']
    .str.replace('USD', '')
    .str.replace(',', '')  # delete commas for thousands
    .str.strip()           # delete spaces
    .astype(float)
)

# Generate the actual condition of the phones
conditions = ['Excellent', 'Good', 'regular']
df['Condition'] = np.random.choice(conditions, size=len(df), p=[0.20, 0.60, 0.20])

#Generate the years of use for the phones
df['age_years'] = (CURRENT_YEAR - df['Launched Year'] + 1).astype(int)
df['age_years'] = df['age_years'].clip(lower=1)  # Ensure age is minimum 1

#2. Calculate the price depreciation based on the condition and age of the phone
#discount
condition_discount = {
    'Excellent': 0.15,
    'Good': 0.30,
    'regular': 0.45
}

#Add 5% discount for each year of use
df['price_drop'] = df['Condition'].map(condition_discount) + (df['age_years'] * 0.05)
df['price_drop'] = np.clip(df['price_drop'], 0, 0.70)  # Ensure max discount is 70%

# Calculate the depreciated price
df['refurbished_price'] = df['Launched Price (USA)'] * (1 - df['price_drop'])

#Add realistic noise to the refurbished price
noise = np.random.normal(-0.015, 0.015, size=len(df))
df['refurbished_price'] = df['refurbished_price'] * (1 + noise)
df['refurbished_price'] = df['refurbished_price'].round(2)

#3. Clean and remove unnecessary columns
#delete the columns that are not needed
df = df.drop(columns=[
    "Launched Price (Pakistan)", "Launched Price (India)", 
    "Launched Price (China)", "Launched Price (Dubai)"
])

#convert RAM to numeric
df['RAM'] = df['RAM'].str.replace('GB', '').astype(int)

#clean battery and screen size columns
df["Battery Capacity"] = df["Battery Capacity"].str.replace("mAh", "").str.replace(",", "").astype(int)
df["Screen Size"] = df["Screen Size"].str.replace(" inches", "").astype(float)

#4. Select and order the final columns
final_columns = [
    "Company Name", "Model Name", "RAM", "Processor", 
    "Battery Capacity", "Screen Size", "Launched Year",
    "Condition", "age_years", "Launched Price (USA)", 
    "price_drop", "refurbished_price"
]
df = df[final_columns]

#5. Save the final dataset
df.to_csv('../data/refurbished_phones.csv', index=False)
print("Synthetic data generated and saved to 'refurbished_phones.csv'")
print(df.head())