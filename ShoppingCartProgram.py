items = {"Onion": 1.00, "Tomato": 2.00, "Potato": 1.50, "Carrot": 1.25, "Cucumber": 2.50}
is_running = True
Bill = 0
Cart = {} 

print("Welcome to the Shopping Cart Program!")

while is_running:

    print("Select an option:)")
    print("-------------------------------------")
    print("1. Add an item to the cart")
    print("2. Remove an item from the cart")
    print("3. View the items in the cart")
    print("4. Checkout")
    print("5. Exit the program")
    print("--------------------------------------")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter the item you want to add: ").capitalize()
        print("-------------------------------------")
        if item in items:
            qty = int(input(f"Enter the quantity of {item} you want to add: "))
            Cart[item] = Cart.get(item, 0) + qty
            Bill += items[item] * qty
            print(f"{qty} {item}(s) have been added to the cart.")
            print("-------------------------------------")
        else:
            print(f"{item} is not available in the store.")
            print("-------------------------------------")

    elif choice == "2":
        item = input("Enter the item you want to remove: ").capitalize()
        print("-------------------------------------")
        if item in Cart:
            qty = int(input(f"Enter the quantity of {item} you want to remove: "))
            if qty >= Cart[item]:
                Bill -= items[item] * Cart[item]
                del Cart[item]
                print(f"All {item}(s) have been removed from the cart.")
            else:
                Cart[item] -= qty
                Bill -= items[item] * qty
                print(f"{qty} {item}(s) have been removed from the cart.")
            print("-------------------------------------")
        else:
            print(f"{item} is not in the cart.")
            print("-------------------------------------")

    elif choice == "3":
        print("Items in the cart:")
        if not Cart:
            print("Your cart is empty.")
        else:
            for item, qty in Cart.items():
                print(f"- {item} x{qty}: ${items[item] * qty:.2f}")
        print(f"Total: ${Bill:.2f}")
        print("-------------------------------------")

    elif choice == "4":
        print("Checking out...")
        print("Items purchased:")
        if not Cart:
            print("Your cart is empty.")
        else:
            for item, qty in Cart.items():
                print(f"- {item} x{qty}: ${items[item] * qty:.2f}")
        print(f"Total: ${Bill:.2f}")
        Cart.clear()
        Bill = 0
        print("Checkout complete.")
        print("-------------------------------------")
        is_running = False

    elif choice == "5":
        is_running = False
        print("Thank you for using the Shopping Cart Program!")
        print("-------------------------------------")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")