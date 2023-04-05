#Import required packages
import numpy as np
import matplotlib.pyplot as plt

#Provided dataset 1
gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
members = [49, 92, 84, 53]

#Build a plot for dataset 1
plt.bar(gyms, members, align="center", color="red", alpha=0.5)
for index,data in enumerate(members):
    plt.text(x=index-0.05, y=data+1, s=f"{data}")
plt.ylim(0, 100)
plt.title("Total Memberships per Gym", fontweight="bold")
plt.xlabel("Gyms")
plt.ylabel("Number of Members")
plt.show()
