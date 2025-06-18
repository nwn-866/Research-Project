import pandas as pd

# Load your dataset
df = pd.read_csv("PRECTOTCORR.csv")

# Convert DOY to a proper date format
df["DATE"] = pd.to_datetime(df["YEAR"].astype(str) + df["DOY"].astype(str), format="%Y%j")

# Replace DOY with the formatted date
df["DOY"] = df["DATE"].dt.strftime("%Y-%m-%d")

# Drop the auxiliary DATE column
df = df.drop(columns=["DATE"])

# Save the cleaned dataset
df.to_csv("PRECTOTCORR_CLEANED.csv", index=False)

print(df.head())  # Display the first few rows
