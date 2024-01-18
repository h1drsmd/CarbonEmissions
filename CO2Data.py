import pandas as pd
import csv

# Read the CSV file
file_path = 'CO2Emissions.csv'
df = pd.read_csv(file_path, index_col=0)

# Transpose the DataFrame
df_transposed = df.transpose()

# Save the transposed data to a new CSV file
transposed_file_path = 'ProcessedDataTransposed.csv'
df_transposed.to_csv(transposed_file_path)
  
file_path = 'ProcessedDataTransposed.csv'
df = pd.read_csv(file_path, index_col=0)
  
with open(file_path,"r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    data= list(reader)

data[0][0] = "Year"

with open(file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

