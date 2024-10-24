class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

class User:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self,item):
        self.cart.append(item)


# Creat restaurants
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Add menu items to restaurants
restaurant1.add_item(MenuItem("Burger", 5))
restaurant1.add_item(MenuItem("Pizza", 8))
restaurant2.add_item(MenuItem("Sushi", 10))
restaurant2.add_item(MenuItem("Pasta", 7))

# simulate user interaction
print("Welcome to the Foddie")
user_name = input("Enter your name: ")
user = User(user_name)

print("\nAvailble Restaurants: ")
print("1. Restaurant A")
print("2. Restaurant B")

# Allow user to select a restaurant
restaurant_choice = int(input("Enter the number of restaurant you want to order from: "))
selected_restaurant = restaurant1 if restaurant_choice == 1 else restaurant2

print(f"\nMenu of {selected_restaurant.name}: ")
for idx , item in enumerate(selected_restaurant.menu, start=1):
    print(f"{idx}. {item.name} - ${item.price}")


# Allow user to add itmes to their cart.
while True:
    item_choice = input("Enter the number of item you want to add to cart (or 'done' to finish):")
    if item_choice.lower() == 'done':
        break

    try:
        idx = int(item_choice)
        if 1 <= idx <= len(selected_restaurant.menu):
            selected_item = selected_restaurant.menu[idx - 1]
            user.add_to_cart(selected_item)
            print(f"{selected_item.name} added to cart!")
        else:
            print("Invalid item number. Please try again")
    except ValueError:
        print("Invalid input. Please eneter a number or 'done'")


# Display the user's cart and total
total = sum(item.price for item in user.cart)
print(f"\n{user.name}'s Cart")
for item in user.cart:
    print(f"- {item.name}: ${item.price}")
print(f"Total: ${total}")