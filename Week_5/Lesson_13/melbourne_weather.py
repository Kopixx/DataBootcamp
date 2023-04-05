#Import the required packages
import numpy as np
import matplotlib.pyplot as plt 

#Create a list of the monthly average temperatures
celsius = [26.1, 25.3, 22.5, 20.6, 17.3, 14.5, 13.5, 15.8, 17.9, 19.2, 20.3, 24.7]
# print(len(celsius))

#Create an array that numerically represents the months of the year
months_num = np.arange(1, 13, 1)
# print(months_num)

#Create a plot of temperatures per month
# plt.plot(months_num, celsius)
# plt.show()

#Use a list comprehension to convert the temperatures to Fahrenheit
f_temp = []

for i in celsius:
    f_temp.append(int(i) * 9/5 + 32)

#Create a plot of f_temp per month
# plt.plot(months_num, f_temp)
# plt.show()

#Create a plot with both degrees points
plt.plot(months_num, celsius, color='r', label='Celsius')
plt.plot(months_num, f_temp, color='g', label='Fahrenheit')
plt.xlabel("Months of the Year")
plt.ylabel("Temperature (Degrees)")
plt.title("Average Temperatures at Melbourne Airport (2021)")
plt.show()