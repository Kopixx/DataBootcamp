#Import in the csv file
import os
import csv
import pandas as pd

csvpath = os.path.join("Absent", "Absenteeism_at_work.csv")

with open(csvpath, errors = "ignore") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Define Headings
    Headings = ["Reason_for_Absence", "Distance_from_Work", "Service_Time", "Age", "Absenteeism_Time_in_Hours", "Percent_of_Work"]

    #Define Lists
    Reason_for_Absence = []
    Distance_from_Work = []
    Service_Time = []
    Age = []
    Absenteeism_Time_in_Hours = []
    Percent_of_Work = []

    #Add contents to python lists
    for row in csvreader:
        Reason_for_Absence.append(row[0])
        Distance_from_Work.append(row[5])
        Service_Time.append(row[6])
        Age.append(row[7])
        Absenteeism_Time_in_Hours.append(row[20])
        percentofwork = (int(row[20])/8)*100
        Percent_of_Work.append(str(percentofwork) + "%")

    print(Reason_for_Absence)
    print("------------------------------")
    print(Distance_from_Work)
    print("------------------------------")
    print(Service_Time)
    print("------------------------------")
    print(Age)
    print("------------------------------")
    print(Absenteeism_Time_in_Hours)
    print("------------------------------")
    print(Percent_of_Work)
    
    #zip all the lists into one tuple stack
    Absences = zip(Reason_for_Absence, Distance_from_Work, Service_Time, Age, Absenteeism_Time_in_Hours, Percent_of_Work)

#Write the tuple to a csv file
df = pd.DataFrame(Absences)
df.to_csv("Absences_Solved.csv", index=False, header=Headings)