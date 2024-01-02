import pandas as pd
import matplotlib.pyplot as plt
file_path= "CO2Emissions.csv"
df=pd.read_csv(file_path)

plt.figure(figsize=(9,4))

for index, row in df.iterrows():
	country=row["Country Name"]
	years = ["1990", "2000", "2010", "2020"]
	emissions= [row[year] for year in years]
	plt.plot(years,emissions, label=country)


plt.xlabel("Year", fontsize=20)
plt.ylabel("Carbon Emissions", fontsize=20)
plt.title("Carbon Emissions Over Time for All Countries", fontsize=30)
plt.legend(loc=(1,0.295), fontsize=14.5)
plt.subplots_adjust(left=0.1, right=0.8)
plt.grid(True)

plt.show()
