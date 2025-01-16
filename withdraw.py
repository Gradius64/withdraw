
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

# Call the function
# Call the function
                # TODO: Print an error message if the user enters an invalid amount.
amount = input("Enter the amount you want to deposit: ")
amount = float(amount)  # Try to convert the input to a float
if amount <= 0:
    print("Error: Please enter a positive amount.")
else:
    print(f"You have successfully deposited ${amount:.2f}.")
print("Error: Invalid input. Please enter a numeric value.")
# Example usage
# Example usage
                # TODO: Call the handle_withdrawal function recursively for an invalid amount.
                # Prompt the user to select an account
  
    # Prompt the user to select an account
input("Select an account to withdraw from (1 for Checking, 2 for Savings, q to quit): ")


      
    
        
    
    
       

   
        
        

    
       
     
        
        
        # Display the updated balance
        
    
   
    
     # Assuming checking_account has a withdraw method
                # TODO: Ensure the function returns after the recursive call.


        

# Test the function






# Assuming checking_account has a withdraw method
            # Assuming savings_account has a withdraw method
            # TODO: Add an if/else conditional statement to check the account choice,

        # Perform action on checking account
        
        # Here you can add code to handle deposit/withdrawal for checking
    
        # Perform action on savings account
       
        # Here you can add code to handle deposit/withdrawal for savings
    
      

# Example usage
user_choice = input("Enter '1' for Checking or '2' for Savings: ")

            # Prompt the user to select an account
   
 
        
 

        
        # Check the account choice and call the appropriate withdraw method

            # Withdraw from checking account
           
            
       
            # Withdraw from savings account
           
    
                # TODO: Call the withdraw method on the appropriate account.
def __init__(self, balance=0):
        self.balance = balance

def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


pass  # You can add specific methods for Checking if needed


pass  # You can add specific methods for Savings if needed



account_choice = input("Please select an account (1 for Checking, 2 for Savings): ")


            
            
            
       
       

# Example usage





                # TODO: Add a print statement to display the updated balance after the deposit
                # Prompt user to select an account to deposit into
                # Prompt user to select an account to deposit into
account_choice = input("Which account would you like to deposit into? (1 for Checking, 2 for Savings, q to quit): ")
    
if account_choice == 'q':
        

    if account_choice in ['1', '2']:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if account_choice == '1':
                checking_account.deposit(amount)  # Call the deposit method on the checking account
                print(f"Updated Checking Account Balance: ${checking_account.get_balance():,.2f}")  # Print updated balance
            elif account_choice == '2':
                savings_account.deposit(amount)  # Call the deposit method on the savings account
                print(f"Updated Savings Account Balance: ${savings_account.get_balance():,.2f}")  # Print updated balance
        except ValueError:
            print("Please enter a valid dollar amount.")
            handle_deposit(checking_account, savings_account)  # Call the function recursively if there is an error
    else:
        print("Invalid choice. Please enter '1' for Checking or '2' for Savings.")
        handle_deposit(checking_account, savings_account)
        
         
            

                # TODO: Format the balance to two decimal places and thousands.

    
    if account_choice == 'q':
        

   
        try:
            amount = float(input("Enter the amount to deposit: "))
            if account_choice == '1':
                checking_account.deposit(amount)  # Call the deposit method on the checking account
                formatted_balance = f"{checking_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Checking Account Balance: ${formatted_balance}")  # Print updated balance
            elif account_choice == '2':
                savings_account.deposit(amount)  # Call the deposit method on the savings account
                formatted_balance = f"{savings_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Savings Account Balance: ${formatted_balance}")  # Print updated balance
        except ValueError:
            print("Please enter a valid dollar amount.")
            handle_deposit(checking_account, savings_account)  # Call the function recursively if there is an error
    else:
        print("Invalid choice. Please enter '1' for Checking or '2' for Savings.")
        handle_deposit(checking_account, savings_account) 
                # TODO: Call the deposit methods on the appropriate account.
account_choice = input("Which account would you like to deposit into? (1 for Checking, 2 for Savings, q to quit): ")
    
   
        
amount = float(input("Enter the amount to deposit: "))
if account_choice == '1':
              
                formatted_balance = f"{checking_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Checking Account Balance: ${formatted_balance}")  # Print updated balance
            
                savings_account.deposit(amount)  # Call the deposit method on the savings account
                formatted_balance = f"{savings_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Savings Account Balance: ${formatted_balance}")  # Print updated balance
       
            
           
else:
        print("Invalid choice. Please enter '1' for Checking or '2' for Savings.")
        handle_deposit(checking_account, savings_account) 
                # TODO: Add a print statement to display the updated balance after the deposit
account_choice = input("Which account would you like to deposit into? (1 for Checking, 2 for Savings, q to quit): ")
   

  
amount = float(input("Enter the amount to deposit: "))
if account_choice == '1':
                checking_account.deposit(amount)  # Call the deposit method on the checking account
                # Print updated balance
                formatted_balance = f"{checking_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Checking Account Balance: ${formatted_balance}")  # Print updated balance
        
                savings_account.deposit(amount)  # Call the deposit method on the savings account
                # Print updated balance
                formatted_balance = f"{savings_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Savings Account Balance: ${formatted_balance}")  # Print updated balance

            
            # Call the function recursively if there is an error
   
        
        
                # TODO: Format the balance to two decimal places and thousands.
{
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
}.format(balance);

console.log(formattedBalance);
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
account_choice = input("Which account would you like to deposit into? (1 for Checking, 2 for Savings, q to quit): ")
    
  

amount = float(input("Enter the amount to deposit: "))
if account_choice == '1':
                checking_account.deposit(amount)  # Call the deposit method on the checking account
                formatted_balance = f"{checking_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Checking Account Balance: ${formatted_balance}")  # Print updated balance
            
                savings_account.deposit(amount)  # Call the deposit method on the savings account
                formatted_balance = f"{savings_account.get_balance():,.2f}"  # Format the balance
                print(f"Updated Savings Account Balance: ${formatted_balance}")  # Print updated balance
        
print("Please enter a valid dollar amount.")
handle_deposit(checking_account, savings_account)  # Call the function recursively if there is an error
    
        # Raise a ValueError for invalid choice
       

# Example usage
try:
    handle_deposit(checking_account, savings_account)
except ValueError as e:
    print(e)  # This will print the error message

    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.

