def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} has been deposited.")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount:.2f} has been withdrawn.")
        print(f"Your new balance is: ${balance:.2f}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance

print("Welcome to the Banking Program!")

def main():

    balance = 0
    is_running = True

    while is_running:
        print("********************************")
        print("Please select an option:")
        print("********************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("********************************")

        choice = input("Enter your choice (1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("********************************")
            print("Invalid choice. Please try again.")
        else:
            
            if choice == "1":
                show_balance(balance)

            elif choice == "2":
                balance = deposit(balance)

            elif choice == "3":
                balance = withdraw(balance)

            elif choice == "4":
                is_running = False
                print("Thank you for using the Banking Program. Goodbye!")
                print("********************************")

        


if __name__ == "__main__":
    main()