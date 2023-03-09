#Import the csv file
import os
import csv

csvpath = os.path.join("Comic_Books", "comic_books.csv")


with open(csvpath, errors = "ignore") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #for row in csvreader:
        #print(row)

#Ask the user what book title they would like to find
    book_title = input("What is the title of the book you are looking for? ")

#Set a 'found' variable
    found = "False"

#Search for the book title
    while found == "False":
        for row in csvreader:
            if (row[0] == book_title):
                print("Your book has been found!")
                print(row[0] + " was published by " + row[8] + " in the year " + row[9])
                found = "True"

    if (found == "False"):
        print("Sorry, we don't seem to have the book you are looking for.")
    