import pandas as pd
import os

# Folder containing the CSV files
input_folder = "./"  # Update this if needed

# Get all CSV files in the folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]

# Process each CSV file
for file_name in csv_files:
    file_path = os.path.join(input_folder, file_name)

    # Load the dataset
    df = pd.read_csv(file_path)

    # Standardize column names: Treat "Trading_Date" and "Trading_date" as the same
    df.columns = df.columns.str.replace('Trading_Date', 'Trading_date')

    # Filter rows where Fuel_Code is 'Hydro' or 'Wind'
    filtered_df = df[df['Fuel_Code'].isin(['Hydro', 'Wind'])]

    # Identify TP columns (TP1 to TP50)
    tp_columns = [col for col in df.columns if col.startswith('TP')]

    # Select required columns (Fuel_Code and Trading_date)
    final_df = filtered_df[['Fuel_Code', 'Trading_date']].copy()

    # Calculate the sum of TP1 to TP50 for each row and create a new column 'Total_TP'
    final_df['Total_TP'] = filtered_df[tp_columns].sum(axis=1)

    # Group by Fuel_Code and Trading_date, then sum the Total_TP for each group
    final_df = final_df.groupby(['Fuel_Code', 'Trading_date'], as_index=False)['Total_TP'].sum()

    # Save to a new CSV file with a modified name
    output_file = f"filtered_{file_name}"
    output_path = os.path.join(input_folder, output_file)
    final_df.to_csv(output_path, index=False)

    print(f"Processed and saved: {output_file}")