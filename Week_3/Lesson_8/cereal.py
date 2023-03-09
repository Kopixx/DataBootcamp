#Import the cereal csv file
import os
import csv
import pandas as pd

csvpath = os.path.join("cereal.csv")

with open(csvpath, errors = "ignore") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Define Headings
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Define list for storing cereal brands
    fibrous_cereal = []

    #Loop through the fibre column and store the cereals with more than 5 grams of fibre. 
    for row in csvreader:
        if float(row[7]) >= 5:
            fibrous_cereal.append(row[0])
    
    #Print the list of fibrous cereals
    print("The cereal brands that contain more than 5 grams of fibre are:")
    for i in range(0, len(fibrous_cereal)):
        print(f"{fibrous_cereal[i]}")
