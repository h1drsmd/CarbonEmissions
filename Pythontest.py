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


plt.xlabel("Year", fontsize=25)
plt.ylabel("CO2 Emissions", fontsize=25)
plt.title("Carbon Emissions Of The 10 Most CO2 Emitting Countries", fontsize=35, fontweight="bold")
plt.legend(loc=(1,0.295), fontsize=15)
plt.subplots_adjust(left=0.1, right=0.8)
plt.grid(True)

plt.show()
