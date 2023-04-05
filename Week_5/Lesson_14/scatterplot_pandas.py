#Import required packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Save the filepath
filepath = "~/Documents/PythonProjects/DataBootcamp/Lesson_14/Lp100km.csv"

#Read the CSV
car_df = pd.read_csv(filepath)

#Remove the rows with missing horsepower values
car_df = car_df.loc[car_df["horsepower"] != "?"]

#Set Car Name as index
car_ind_df = car_df.set_index("car name")

#Remove the origin column
del car_ind_df["origin"]

#Convert the horsepower column to numeric
car_ind_df["horsepower"] = pd.to_numeric(car_ind_df["horsepower"])

#Produce a scatterplot of L/100km vs. horsepower

