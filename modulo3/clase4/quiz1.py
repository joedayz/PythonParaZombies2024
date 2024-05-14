
#1 - Crea una clase llamada Account
# Agrega las propiedades: title y Balance


#2 - Crea una clase llamada SavingsAccount
# Agrega interestRate




# Account("Mark", 5000)

# SavingsAccount("Mark", 5000, 5)

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        


carlos = SavingsAccount("Mark", 5000, 5)
print(carlos.title)
print(carlos.balance)
print(carlos.interestRate)

