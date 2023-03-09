#Ask for the user to input a number
num = int(input("How many numbers? "))

#Print the user-input number
for x in range(0, (num + 1)):
    print(x)

#Would the user like to continue?
run = input("Would you like to continue? (Y/N) ")

while run == "Y" or run == "y":
    num = int(input("How many numbers? "))
    for x in range(0, (num + 1)):
        print(x)
    run = input("Would you like to continue? (Y/N) ")



