#Define a function that prints 'Hello!' when called
def print_hello():
    print(f"Hello!")

#Call the function to run
print_hello()

#Define a function that takes in the parameter 'name'
def print_name(name):
    print("Hello " + str(name) + "!")

#Call the function to run
print_name("Bob Smith")

#Create two lists
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_two = [11, 12, 13, 14, 15]

#Define a function that takes in list information and prints its values
def list_information(simple_list):
    print(f"The values within the list are...")
    for value in simple_list:
        print(value)
    print("The length of this list is " + str(len(simple_list)))

#Use the function 'list_information'
list_information(list_one)
list_information(list_two)