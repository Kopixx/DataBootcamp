#Name input loop
names = []
for i in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
#lowercased = [i.lower() for i in names]
#print(lowercased)

# @TODO: Use a list comprehension to create a list of title cased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [i.title() for i in names]
print(titlecased)

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
