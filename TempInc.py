import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path= "/home/btu/CarbonEmission/TempInc.csv"
data=pd.read_csv(file_path)

y=np.array(data["Year"])
x=np.array(data["Temperature Increase"])
plt.figure(figsize=(9,4))
plt.plot(x,y,marker="o")
plt.title("Temperature Increase Over Years")
plt.xlabel("Year")
plt.ylabel("Temperature Increase")
plt.grid(True)
plt.show()
