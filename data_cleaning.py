import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data_raw.csv")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Sales Amount"] = df["Sales Amount"].fillna(df["Sales Amount"].mean())
df["Customer Name"] = df["Customer Name"].fillna("Unknown")
df["Region"] = df["Region"].fillna("Unknown")

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\nCleaned Data:")
print(df)

# Save cleaned dataset
df.to_csv("sales_data_cleaned.csv", index=False)

print("\nCleaned data saved as sales_data_cleaned.csv")
