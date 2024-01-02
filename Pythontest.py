import pandas as pd
import matplotlib.pyplot as plt
file_path= "/home/CarbonEmissions/CO2Emissions.csv"
df=pd.read_csv(file_path)

plt.figure(figsize=(9,4))

for index, row in df.iterrows():
	country=row["Country Name"]
	years = ["1990", "2000", "2010", "2020"]
	emissions= [row[year] for year in years]
	plt.plot(years,emissions, label=country)


plt.xlabel("Year")
plt.ylabel("Carbon Emissions")
plt.title("Carbon Emissions Over Time for All Countries")
plt.legend(loc=(1,0.295))
plt.subplots_adjust(left=0.15, right=0.85)
plt.grid(True)

plt.show()
