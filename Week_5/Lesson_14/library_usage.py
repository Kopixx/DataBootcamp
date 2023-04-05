#Import the required packages
import pandas as pd
import matplotlib.pyplot as plt

#Save the filepath
filepath = "~/Documents/PythonProjects/DataBootcamp/Lesson_14/library_usage.csv"

#Read the file
lib_df = pd.read_csv(filepath)

#Filter out patrons with 0 checkouts
lib_filter_df = lib_df.loc[lib_df["Total Checkouts"] > 0, :]

#Group the data by patron type
grouped_lib_df = lib_filter_df.groupby(["Patron Type Definition"]).sum()

#How many of each patron type has borrowed before?
patrons = lib_filter_df["Patron Type Definition"].value_counts()

#Plot the data
figure_1 = patrons.plot(kind="bar", figsize=(8,6), title="Library Usage by Patron Type")
figure_1.set_xlabel("Patron Type")
figure_1.set_ylabel("Number of Users")

#Display the plot
plt.tight_layout()
plt.show()


#BONUS
#Set a value for minimum checkouts
home_lib = input("Which library do you want to look up? ")
min_checkouts = int(input("Do you have a minimum number of checkouts per patron type? "))

#Group the library by Home Library and Patron Type
home_lib_df = lib_filter_df.loc[lib_filter_df["Home Library Definition"] == home_lib, :]
grouped_home_df = home_lib_df[["Patron Type Definition", "Total Checkouts"]].groupby(["Patron Type Definition"]).sum()
filtered_grouped_home_df = grouped_home_df.loc[grouped_home_df["Total Checkouts"] > min_checkouts, :]
print(filtered_grouped_home_df)

#Plot the data on a pie chart
filtered_grouped_home_df.plot(kind="pie", y="Total Checkouts", title=f"Loans of {home_lib} Branch for Patron Types with over {min_checkouts} Loaned Items")

#Display the plot
plt.axis("equal")
plt.show()