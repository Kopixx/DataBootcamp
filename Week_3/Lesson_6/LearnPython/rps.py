#Import the required package
import random

#Take the player's input
player = input("What would you like to play? Rock, Paper or Scissors? (R/P/S) ")

#Take the computer's input
rpslist = ["R", "P", "S"]
computer = random.choice(rpslist)

#Find our winner and declare the champion!
if (player == computer):
    print("You've tied! You both picked " + player + ". Try again!")
elif (player == "S"):
    if (computer == "R"):
        print("The computer has won! You picked " + player + " but the computer picked " + computer + ". Better luck next time!")
    else:
        print("You have won! You picked " + player + " but the computer picked " + computer + ". Congratulations!")
elif (player == "R"):
    if (computer == "P"):
        print("The computer has won! You picked " + player + " but the computer picked " + computer + ". Better luck next time!")
    else:
        print("You have won! You picked " + player + " but the computer picked " + computer + ". Congratulations!")
elif (player == "P"):
    if (computer == "S"):
        print("The computer has won! You picked " + player + " but the computer picked " + computer + ". Better luck next time!")
    else:
        print("You have won! You picked " + player + " but the computer picked " + computer + ". Congratulations!")
else:
    print("There's been an error computing your turn. Please check your input and try again.")


