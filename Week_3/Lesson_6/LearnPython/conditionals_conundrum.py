#Ask for the participent's height and age
height = int(input("How tall are you in centimeters? Round up. "))
age = int(input("How old are you in years? Round down. "))

#Provide the restrictions back to the rider dependent on their inputs
if (height > 70) and (age >= 18):
    print("You can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("You can ride all the moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("You can ride all the light roller coasters")
elif ((height > 50) and (age >= 18)):
    print("You can ride bumper cars")
elif (height > 50):
    permission = input("Do you have parental permission to ride the bumper cars? Yes or No. ")
    if (permission == "Yes"):
        print("You can ride the bumper cars")
    else:
        print("You can only ride the Lazy River ride.")
else:
    print("You can only ride the Lazy River ride.")

