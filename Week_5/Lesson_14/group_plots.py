#Import required packages
import pandas as pd
import matplotlib.pyplot as plt

#Save the filepath
filepath = "~/Documents/PythonProjects/DataBootcamp/Lesson_14/accidents.csv"

#Read in the CSV file
accidents_df = pd.read_csv(filepath)

#Create a grouped dataframe based on the FUNC_SYSNAME column
accidents_type_df = accidents_df.groupby("FUNC_SYSNAME")

#Count the number of times each road type appears
count_type_df = accidents_type_df["FUNC_SYSNAME"].count()

#Create a bar chart based on the group count data
count_chart = count_type_df.plot(kind="bar", figsize=(8,10), title="Number of Accidents per Road Type")

#Set x and y labels
count_chart.set_xlabel("Road Type")
count_chart.set_ylabel("Number of Accidents")

#Display plot
plt.tight_layout()
plt.show()