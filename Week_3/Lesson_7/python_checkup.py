#Print Hello User!
print("Hello User!")

#Ask for the user's name
name = input("What is your name? ")

#Respond to their name
print("Hello " + name)

#Ask for their favourite number
favenum = int(input("What is your favourite number? "))

myfavenum = 7

#Compare our favourite numbers

if (favenum == myfavenum):
    print("Your favourite number is the same as mine!")
elif (favenum < myfavenum):
    print("Your favourite number is lower than mine.")
elif (favenum > 20):
    print("Your favourite number is stupid Lucas.")
else:
    print("Your favourite number is higher than mine.")
