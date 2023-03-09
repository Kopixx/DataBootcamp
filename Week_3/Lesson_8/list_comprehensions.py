#Creating a list of letters using for loops
fish = "halibut"

letters = []
for i in fish:
    letters.append(i)
print(letters)

#Create a list comprehension version of this process
letters = [i for i in fish]
print(letters)

#The result is the same but the code is much more concise!

#Create a list of capital letters using for loops
capital_letters = []
for i in fish:
    capital_letters.append(i.upper())
print(capital_letters)

#Create a list comprehension version of this process
capital_letters = [i.upper() for i in fish]
print(capital_letters)

#Create a list using conditional logic (if statements)
jan_temperatures = [30, 29, 33, 26, 41]
hot_days = []
for i in jan_temperatures:
    if i > 32:
        hot_days.append(i)
print(hot_days)

#Create a list comprehension version of this process
hot_days = [i for i in jan_temperatures if i > 32]
print(hot_days)

