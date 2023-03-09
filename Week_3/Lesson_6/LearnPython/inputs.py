#Collect a name input and store it in a variable
name = input("What is your name? ")

#Collect the user input for age and store it in an integer variable
age = int(input("What is your age? "))

#Collect the use input for 'truthness' and store it in a boolean integer
trueOrfalse = bool(input("is this input truthful? "))

#Create 3 print statements to display these inputs
print("My name is " + name)
print("I will be " + str(age + 1) + " next year.")
print("Have you been honest? " + str(trueOrfalse))