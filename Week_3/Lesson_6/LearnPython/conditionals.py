#This is a tutorial on how to use if, else, and other conditionals

#Define 2 integer variables
x = 1
y = 10

#Check if a variable is equal to a value
if x == 1:
    print("x is equal to 1")

#Check if a variable is NOT equal to a value
if y != 1:
    print("y is not equal to 1")

#Check if one variable is less than another
if x < y:
    print("x is less than y")

#Check if one variable is more than another
if y > x:
    print("y is greater than x")

#Check if a variable is greater than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

#Check if two conditions are met using 'and'
if x == 1 and y == 10:
    print("Both values returned true")

#Check if either of two conditions are met using 'or'
if x == 1 or y == 10:
    print("One or more of the statements are true")

#Nested Statements using 'elif' and 'else' 
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")