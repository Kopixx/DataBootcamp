#Import required packages
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

#Save the filepath
filepath = "~/Documents/PythonProjects/DataBootcamp/Lesson_14/union_settlements_1995.csv"

#Read in CSV
settlements_df = pd.read_csv(filepath)

#Refine to a series of number of settlements made by each union
unions = settlements_df["UNION"].value_counts()

#Plot the data
figure_1 = unions.plot(kind="bar", facecolor="red", title="Major Collective Bargaining Settlements (1995)", figsize=(8,6))
figure_1.set_xticklabels(unions.index, rotation=45)
figure_1.set_xlabel("Union Name")
figure_1.set_ylabel("Number of Settlements")

#Display the data
plt.tight_layout()
plt.show()
