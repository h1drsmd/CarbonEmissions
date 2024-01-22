import pandas as pd
import csv

file_path = 'SurfaceTemp.csv'
df = pd.read_csv(file_path, index_col=0)

df_transposed = df.transpose()

transposed_file_path = 'ProcessedSurfaceTemp.csv'
df_transposed.to_csv(transposed_file_path)

file_path = 'ProcessedSurfaceTemp.csv'
df = pd.read_csv(file_path, index_col=0)

with open(file_path,"r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    data= list(reader)

data[0][0] = "Year"

with open(file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
