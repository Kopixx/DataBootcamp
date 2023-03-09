#Create the Hobby Book dictionary. Define Name, Age, a List of Hobbies and a dictionary of wake-up times

hobby_book = {
    "name" : "Kali",
    "age" : 25,
    "hobbies" : [
        "DJing",
        "Electronic Music Production",
        "Gymming",
        "Playing Video Games",
    ],
    "wakeup" : {
        "Mondays" : "7am",
        "Saturdays" : "8am",
        "Sundays" : "10am",
    },
}

#Print out your name, number of hobbies and usual weekday wakeup time
print(f'Hi my name is {hobby_book["name"]}, I have {len(hobby_book["hobbies"])} hobbies and I usually wake up at {hobby_book["wakeup"]["Mondays"]} on weekdays!')
