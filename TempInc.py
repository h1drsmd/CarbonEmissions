import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path= "TempInc.csv"
data=pd.read_csv(file_path)

x=np.array(data["Year"])
y=np.array(data["Temperature Increase"])
plt.figure(figsize=(9,4))
plt.plot(x,y,marker="o")
plt.title("Temperature Increase Over Years", fontsize=30)
plt.xlabel("Year", fontsize=20)
plt.ylabel("Temperature Increase in °C", fontsize=20)
plt.grid(True)
plt.show()
