#Have the numbers begin at the end of the previous chain

#Ask for the user to input a number
num = int(input("How many numbers? "))

#Print the user-input number
for x in range(0, (num + 1)):
    print(x)

#Would the user like to continue?
run = input("Would you like to continue? (Y/N) ")

while run == "Y" or run == "y":
    num2 = int(input("How many numbers? "))
    for x in range(num, (num2 + 1)):
        print(x)
        num = num2
    run = input("Would you like to continue? (Y/N) ")