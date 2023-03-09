#Create a list with a range of data types
myList = ["Kirra", 25, "Ahmed", 80]
print(myList)

#Add an element to the end of a list
myList.append("Matt")
print(myList)

#Returns the index of the object with the matching value
print(myList.index("Matt"))

#Change the specified element within a list using indexing
myList[3] = 85
print(myList)

#Return the length of the list
print(len(myList))

#Remove a specific object from the list
myList.remove("Matt")
print(myList)

#Remove the object at the index specified
myList.pop(0)
print(myList)

#Create a tuple
myTuple = ("Python", 100, "VBA", False)
print(myTuple)
