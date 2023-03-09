#Import the csv file
import os
import csv 
import pandas as pd

#Create a function that calculates the usage rates for each type of time off & prints the results

def print_percentages(employee_data):
    """This activity inputs the variable 'employee_data'"""
    pto_hours = (int(employee_data[2])/int(employee_data[1]))*100
    voting_hours = (int(employee_data[6])/int(employee_data[5]))*100

    if (int(employee_data[3]) == 0):
        sick_hours = 0.0
    else:
        sick_hours = (int(employee_data[4])/int(employee_data[3]))*100

    overall_hours = (pto_hours + voting_hours + sick_hours)

    print(f'Percentage of PTO Hours taken = {pto_hours}%')
    print(f'Percentage of Sick Hours taken = {sick_hours}%')
    print(f'Percentage of Voting Hours taken = {voting_hours}%')

    if (overall_hours > 50):
        print("Adequate time off has been taken.")
    else:
        print("Encourage this employee to take some time off.")

    return

csvpath = os.path.join("pto_hours.csv")

with open(csvpath, errors = "ignore") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Define the Headings
    csv_header = next(csvreader)
    #print(csv_header)

    #Ask for the employee the user wants data for
    employee_id = input("Which employee would you like to look for? ")
    employee_data = []

    #Create a loop to optain this data
    for row in csvreader:
        if (row[0] == employee_id):
            for i in row:
                employee_data.append(i)
    
    # #Utilise the print percentages function
    print_percentages(employee_data)