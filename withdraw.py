"""This function handles the withdrawal process for the user."""

# TODO: Pass in the checking_account and savings_account objects.
def handle_withdrawal():
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (CheckingAccount): The checking account object.
    - savings (SavingsAccount): The savings account object.

    The function prompts the user to select an account and make a withdrawal.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After each withdrawal, the function prints the updated balance of the respective account.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to make a withdrawal?")
    # TODO: Prompt the user to select an account to make a withdrawal.
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance


def choose_account():
    checking_account = BankAccount(1000)  # Example initial balance
    savings_account = BankAccount(500)     # Example initial balance

    account_choice = input("Select an account (1 for Checking, 2 for Savings, q to quit): ")

    if account_choice == '1':
        handle_withdrawal(checking_account, "Checking")
    elif account_choice == '2':
        handle_withdrawal(savings_account, "Savings")
    elif account_choice.lower() == 'q':
        print("Exiting the program.")
        return
    else:
        print("Invalid choice. Please enter '1', '2', or 'q'.")
        choose_account()


def handle_withdrawal(account, account_type):
    amount = float(input(f"Enter amount to withdraw from {account_type} account: "))
    account.withdraw(amount)
    print(f"Updated {account_type} Account Balance: ${account.get_balance():,.2f}")


# Start the account selection process

    # TODO: If the user chooses to quit, return from the function.

    while True:
        user_input = input("Enter something (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':  # Check if the user wants to quit
            print("Exiting the function. Goodbye!")
            return  # Exit the function
        else:
            print(f"You entered: {user_input}")

# Call the function
user_interaction()


   
  
       

