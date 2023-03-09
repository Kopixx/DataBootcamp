#The list of lollies in the shop
lolly_list = ["Fantales", "Snakes Alive", "Minties", "Liquorice Allsorts", "Strawberries & Cream", "Life Savers", "Banana Lollies", "Fruit Pastilles", "Sherbies"]

#Print the list of lollies and the indexes they're stored within

for x, item in enumerate(lolly_list):
    print(x, item)

#Set an allowance for how many lollies the user can choose
allowance = 5

#Create a list that the user's lollies will be stored within
lolly_cart = []

#Let the user choose their lollies

while ((len(lolly_cart)) < 5):
    chosen_lolly = int(input("Which lolly would you like from the numbered list? "))
    try:
        lolly_cart.append(lolly_list[chosen_lolly])
    except IndexError:
        print("Sorry that isn't a number on the list. Try again.")

#Print the user's cart contents
print("Your lolly cart is full. Here is your cart contents:")

for i in range(len(lolly_cart)):
    print(lolly_cart[i])
