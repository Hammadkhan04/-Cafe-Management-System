# Define the menu of the restaurant
menu = {
    "Pizza": 200,
    "Burger": 300,
    "Broast": 400,
    "Salad": 100,
    "Coffee": 250,
}

# Greet the customer and display the menu
print("Welcome to PYTHON Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

# Take order
item_1 = input("\nEnter the name of the item you want to order: ").strip().capitalize()

if item_1 in menu:
    print(f"Your {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available.")

# Optionally, ask for another order or confirmation
another_order = input("\nWould you like to order anything else? (yes/no): ").strip().lower()

if another_order == "yes":
    item_2 = input("Enter the name of the next item you want to order: ").strip().capitalize()
    if item_2 in menu:
        print(f"Your {item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available.")
else:
    print("\nEnjoy your meal at PYTHON Restaurant!")
