class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
            return
        self.__balance -= amount

    def check_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.check_balance())  # prints: 70
account.withdraw(30)
account.withdraw(30)
account.withdraw(30)