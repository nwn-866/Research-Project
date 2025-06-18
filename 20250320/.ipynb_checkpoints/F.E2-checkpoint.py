import os
import pandas as pd

# Define the directory where the CSV files are stored
directory = "./"  # Change this to your actual path

# Initialize an empty list to store individual DataFrames
dfs = []

# Loop through all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path, parse_dates=["Trading_date"])
        dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Ensure the data is sorted by Trading_date
merged_df.sort_values(by="Trading_date", inplace=True)

# Filter data within the specified date range
start_date = "2015-01-01"
end_date = "2024-12-31"
merged_df = merged_df[(merged_df["Trading_date"] >= start_date) & (merged_df["Trading_date"] <= end_date)]

# Save the merged DataFrame to a new CSV file
output_file = "merged_data.csv"
merged_df.to_csv(output_file, index=False)

print(f"Merged CSV file saved as {output_file}")