#create an order form that displays a list of available pies
#Make a lst of pies
pie_list = ["Aussie Beef", "Steak and Kidney", "Chicken", "Sheperd's", "Spinach and Feta", "Curry", "Lamb and Rosemary", "Steak and Mushroom", "Apple", "Lemon Meringue"]

#Print a welcome message & menu

print("Welcome to the House of Pies! Here are our pies:")
print("--------------------------------------------------")

for num, pie in enumerate(pie_list):
    print((num+1), pie)

order_again = "Yes"
final_order = []

while order_again == "Yes":
    #Ask the user which pie they would like to order:
    order = int(input("What pie would you like to order? "))
    final_order.append(pie_list[order - 1])

    #Print a reply
    print("Great! We'll have your " + pie_list[(order - 1)] + " pie right out for you.")
    order_again = input("Would you like to make another order? Yes or No. ")

#Print the final order
print("You purchased:")
for i in range(0, len(pie_list)):
    print(f"{final_order.count(pie_list[i])} {pie_list[i]}")



