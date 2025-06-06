class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited. New Balance: {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
         self.balance -= amount
         print(f"{amount} withdraw. Displaying Balance: {self.balance}")

    def display_balance(self):
     print(f"Name: {self.name}, Account no: {self.account_number}, Balance: {self.balance}")

acc = BankAccount(123456789, "Sakshi", 20000)
acc.display_balance()
acc.deposit(1000)
acc.withdraw(500)
acc.withdraw(5000)

