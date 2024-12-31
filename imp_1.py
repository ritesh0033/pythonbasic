#banking system

class BankAccount:
    def __init__(self, account_number, account_holder, account_balance=0.00):
        """
        Initialize a BankAccount object.
        """
        self.accountnumber = account_number
        self.accountholder = account_holder
        self.balance = account_balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount <= 0.00:
            print("Deposited amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited: {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if amount <= 0.00:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        print(f"Withdrew: {amount}, Remaining balance: {self.balance}")

    def display_details(self):
        """
        Display account details.
        """
        print(f"Account Number: {self.accountnumber}")
        print(f"Account Holder: {self.accountholder}")
        print(f"Account Balance: {self.balance}")

if __name__ == "__main__": 
    
    account_number = input("Enter the account number: ")
    account_holder = input("Enter the account holder name: ")
    account_balance = float(input("Enter the initial balance of the user: "))

    
    account = BankAccount(account_number, account_holder, account_balance)
    account.display_details()

    deposit_amount = float(input("Enter the deposit amount: "))
    account.deposit(deposit_amount)
    withdraw_amount = float(input("Enter the withdrawal amount: "))
    account.withdraw(withdraw_amount)
    account.display_details()

