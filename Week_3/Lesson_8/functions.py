#Create a simple function with no parameters
def hello():
    print(f"Hello!")

hello()

#Create a simple function with one parameter
def show(message):
    print(message)

show("Howdy!")

#Create a function with two parameters
def cooking(protein, topping):
    quesadilla = f"Here is a {protein} quesadilla with {topping} for toppings."
    print(quesadilla)

cooking("chicken", "sour cream")

#Create a function that specifies default values for its parameters
def chef(protein="chicken", topping="cheese"):
    quesadilla = f"Here is a {protein} quesadilla with {topping} for toppings."
    print(quesadilla)

chef()

#Functions can also return values dependent on the inputted parameters
def square(number):
    return (number * number)

#Using the return function will require you to save it somewhere
square_number = square(2)
print(square_number)

#You can also print the return value, but it will not be saved anywhere
print(square(3))
