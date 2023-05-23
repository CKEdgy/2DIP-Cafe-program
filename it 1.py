menu = {
    '1': {'name': 'Burger', 'price': 10.99},
    '2': {'name': 'Pizza', 'price': 8.99},
    '3': {'name': 'Salad', 'price': 5.99},
    '4': {'name': 'Soup', 'price': 4.99},
    '5': {'name': 'Fries', 'price': 3.99},
}

def display_menu():
    # Displays the menu items and their prices
    print("Menu:")
    for item, details in menu.items():
        print(f"{item}. {details['name']}: ${details['price']}")

def place_order():
    # Allows the user to select items from the menu and creates an order list
    order = []
    while True:
        choice = input("Enter item number (type 'finish' to finish): ")
        if choice == 'finish':
            break
        if choice not in menu:
            print("Invalid choice. Please try again.")
            continue
        # Adding items from the menu dictionary into the order list
        order.append(menu[choice])
    return order

def calculate_total(order):
    # Calculates the total price of the order
    total = 0
    for item in order:
        total += item['price']
    return total

def main():
    display_menu()
    print("Welcome to the BDSC Cafeteria ordering system")
    print("Please select items from the menu and enter 'finish' to finish.")
    order = place_order()
    print("Order summary:")
    for item in order:
        print(f"{item['name']}: ${item['price']}")
    total = calculate_total(order)
    print(f"Total: ${total}")

if __name__ == '__main__':
    main()
