"""
The code starts by displaying a welcome message to the user and a line of asterisks as a separator, it initializes empty lists to store the items in the cart, their prices, quantities, and a variable to hold the total price. It then starts an infinite loop, which will continue until a break statement is encountered. The code prompts the user to enter an action number and validates the input, it ensures that the input is a valid integer between 1 and 5, the item, price, and quantity are then added to their respective lists (cart, prices, quantities).

The "View cart" action checks if the cart is empty and prints the items in the cart along with their prices, quantities, and total prices. The "Remove item" action prompts the user to enter the item number to remove, validates the input, and removes the specified quantity of the item from the cart such that if the quantity becomes zero, the item is completely removed from the cart. The "Compute total" action calculates the total price of the items in the cart and displays it to the user. The "Quit" action prints a farewell message and breaks the loop, ending the program.
"""  # noqa: E501


# Added features for error handling
# Extended formatting to include output text alignment
# Added ability to compute quantity addition and subtraction


print("\n~~~ SHOPPING CART ~~~")
print("~~~ Prove ~~~\n")

print("\nWelcome to the shopping cart program!")
print("*" * 40)

# Initialize empty lists to store cart items, prices, quantities, and total price
cart = []
prices = []
quantities = []
total = None

while True:
    print("\nPlease select one of the following:")
    print("*" * 35)
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print("-" * 35)
    print()

    while True:
        try:
            # Prompt the user to enter an action number
            action = int(input("Please enter an action: "))
            print()

            # Check if the action number is valid (between 1 and 5)
            if action < 1 or action > 5:
                raise ValueError("Invalid action number")
            break
        except ValueError:
            print("Not a valid number. Please select a number between 1 and 5.")
            print("-" * 50)
            print()

    if action == 1:
        # Add item to the cart
        item = input("What item would you like to add? ")

        # Prompt for the price of the item
        price = None
        while price is None:
            try:
                price = float(input("What is the price of '" + item + "'? "))

                # Check if the price is negative
                if price < 0:
                    print("Price cannot be negative.")
                    price = None
            except ValueError:
                print("Invalid input. Please enter a valid price.")
                price = None

        # Prompt for the quantity of the item
        quantity = None
        while quantity is None:
            try:
                quantity = int(input("What is the quantity of '" + item + "'? "))

                # Check if the quantity is negative
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    quantity = None
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
                quantity = None

        # Add the item, price, and quantity to their respective lists
        cart.append(item)
        prices.append(price)
        quantities.append(quantity)

        print("'" + item + "' has been added to the cart.\n")
        print("-" * 50)
        print()
        continue

    elif action == 2:
        if not cart:
            print("The cart is empty!")
        else:
            # View the contents of the shopping cart
            print("The content of the shopping cart is:")
            print(
                "{:<7} {:<15} {:<10} {:<10} {:<10}".format(
                    "Item #", "Item", "Price", "Quantity", "Total Price"
                )
            )
            for i, (item, price, quantity) in enumerate(
                zip(cart, prices, quantities), 1
            ):
                # Calculate the total price for each item
                total_price = price * quantity
                print(
                    "{:<7} {:<15} ${:<9.2f} {:<10} ${:<9.2f}".format(
                        i, item, price, quantity, total_price
                    )
                )
            print()

    elif action == 3:
        if not cart:
            print("The cart is empty!")
        else:
            # Remove an item from the cart
            item_number = input("Which item would you like to remove? ")
            while (
                not item_number.isdigit()
                or int(item_number) <= 0
                or int(item_number) > len(cart)
            ):
                print(
                    "Sorry, that is not a valid item number. Please select a number between 1 and",
                    len(cart),
                )
                item_number = input("Which item would you like to remove? ")

            index = int(item_number) - 1
            item = cart[index]
            price = prices[index]
            quantity = quantities[index]

            print(f"You have {quantity} {item} in your cart.")
            remove_quantity = int(input("How many would you like to remove? "))
            while remove_quantity < 1 or remove_quantity > quantity:
                print(
                    f"Invalid quantity. Please enter a number between 1 and {quantity}."
                )
                remove_quantity = int(input("How many would you like to remove? "))

            quantities[index] -= remove_quantity

            if quantities[index] == 0:
                # Remove the item if the quantity becomes zero
                cart.pop(index)
                prices.pop(index)
                quantities.pop(index)

            print(f"{remove_quantity} {item} has been removed from the cart.\n")
            print("-" * 50)
            print()

    elif action == 4:
        if not cart:
            print("The cart is empty!")
        else:
            # Compute the total price of the items in the cart
            total = sum(price * quantity for price, quantity in zip(prices, quantities))
            print(
                "The total price of the items in the shopping cart is ${:.2f}\n".format(
                    total
                )
            )
            print("-" * 70)
            print()
            continue

    elif action == 5:
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid input, please try again")
