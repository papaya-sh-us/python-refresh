class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
 
    def deposit(self, amount):
        self.balance = self.balance + amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: not enough balance!")
        else:
            self.balance = self.balance - amount
 
 
account = BankAccount("John", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(1000)
print(account.balance)