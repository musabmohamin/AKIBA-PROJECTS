
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance



account1 = BankAccount("Musab Mohammed", 5000)
account2 = BankAccount("Ahmed", 3000)

account1.deposit(1000)
account1.withdraw(2000)
print("Account holder:", account1.account_holder)
print("Current balance:", account1.get_balance())
account1.deposit(-500)
account1.withdraw(-200)
account1.withdraw(10000)
