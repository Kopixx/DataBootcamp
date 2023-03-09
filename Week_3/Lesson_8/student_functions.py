#Create a function 'average()' that accepts a list of numbers & returns the mean.

def average(numbers):
    """My function only accepts lists"""
    return (sum(numbers)/len(numbers))

number_list = [3, 6, 235, 6, 8, 12]
print(average(number_list))
