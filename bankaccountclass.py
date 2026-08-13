class BankAccount():
    balance = 500

    def __init__(self):
        print("Making a new bank account:")
    
    def show_details(self):
        print("Details of bank account are:")
        print(self.balance) 
    
    def withdrawal(self):
        withdrawal_amount = int(input("Please enter the amount of money you would like to withdraw:"))
        self.balance = self.balance - withdrawal_amount 
        print(self.balance)
    
    def deposit(self):
        deposit_amount = int(input("Please enter the amount of momey you would like to deposit:"))
        self.balance = self.balance + deposit_amount
        print(self.balance)


Expensive_Account = BankAccount()

Expensive_Account.show_details()

Expensive_Account.withdrawal() 

Expensive_Account.deposit() 