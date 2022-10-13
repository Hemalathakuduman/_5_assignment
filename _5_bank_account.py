class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        total = balance - amount
        print(total)

    def deposit(self, amount):
        self.amount = amount
    def getBalance(self):
        balance = deposit - total
        print (balance)        

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        interest_amount = self.interestRate*balance/100

obj = SavingsAccount()
obj.interestAmount()
