import pandas as pd

# Load the dataset
df = pd.read_csv("merged_data.csv")

# Filter data for Hydro and Wind
hydro_df = df[df["Fuel_Code"] == "Hydro"]
wind_df = df[df["Fuel_Code"] == "Wind"]

# Save to separate CSV files
hydro_df.to_csv("hydro_data.csv", index=False)
wind_df.to_csv("wind_data.csv", index=False)

print("Hydro and Wind data have been successfully saved to separate CSV files.")
