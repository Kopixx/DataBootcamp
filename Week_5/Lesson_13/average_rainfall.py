#Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import the data (CSV file)
filepath = "~/Documents/PythonProjects/DataBootcamp/Lesson_13/avg_rain_cities.csv"
rainfall_df = pd.read_csv(filepath)

#X axis data & Y axis data; location series & annual rainfall
locations = rainfall_df["LOCATION"]
rainfall = rainfall_df["ANNUAL (mm)"]

x_axis = locations.tolist()
y_axis = rainfall.tolist()

#Plot parameters
plt.bar(x_axis, y_axis, color="red", align="center", alpha=0.50)
tick_locations = [i for i in x_axis]
plt.xticks(tick_locations, x_axis, rotation=90)

#Titles
plt.title("Average Rain in Major Citites", fontweight="bold")
plt.xlabel("City", fontweight="bold")
plt.ylabel("Average Amount of Rainfall in Millimetres", fontweight="bold")

#Save and display graph
plt.tight_layout()
plt.savefig("Average_Rainfall_Output.png")
plt.show()