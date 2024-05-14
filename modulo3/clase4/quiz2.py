# Account

# 1) implementa el metodo getBalance() que retorna el balance de la cuenta


# 2) implementa el metodo deposit(amount) que recibe una cantidad y la suma al balance de la cuenta

# balance = 2000
# deposite(500)

# getBalance() # 2500


# 3) implementa el metodo withdraw(amount) que recibe una cantidad y la resta al balance de la cuenta

# balance = 2000
# withdraw(500)
# getBalance() # 1500


# 4) Implementar el interestAmount() que retorna el interes de la cuenta  basado en esta formula:

# interest = balance * interestRate / 100

# balance = 2000
# interestRate = 5
# interestAmount() # 100


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object

demo1.deposit(10000)
demo1.withdrawal(5000)
print(demo1.getBalance())  # 7000
print(demo1.interestAmount())  # 350.0

