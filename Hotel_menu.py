menu = {
    'Pizza' : 100,
    'Pasta' : 40,
    'Momos' : 50,
    'Coffee' : 30,
    'Tea' : 20,
}
#Greet
print("welcome to My Restaurant")
print("Pizza: Rs100\nPasta: Rs40\nMomos: Rs50\nCoffee: Rs30\nTea: Rs20")
order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")
another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added")
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of item is {order_total} to pay")
