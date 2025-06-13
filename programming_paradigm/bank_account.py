'''
# Define a class called BankAccount
- Initialize account_balance attribute

# Implement deposit(amount), withdraw(amount), and display_balance() methods.
- Deposit should add the specified amount to account_balance.
- Withdraw should deduct the amount from account_balance if funds are sufficient, returning True; 
  otherwise, return False and do not alter the balance.
- Display_balance should print the current balance in a user-friendly format
'''

class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
        
    # Implimenting Deposit Method
    def deposit(self, amount):
        self.account_balance += amount
    
    # Implimenting withdraw Method
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print(f"Insufficient funds. Your balance is {self.account_balance}")
            return False
            
    
    # Display Balance
    def display_balance(self):
        print(f"Your current account balance is: {self.account_balance}")