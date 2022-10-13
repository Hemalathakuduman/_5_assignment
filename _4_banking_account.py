class account:
    def __init__(self, title, balance):
        self.title = None
        self.balance = 0
    

class savingsaccount(account):

    def __init__(self, interestRate):
        self.interestRate = 5
        
   
obj = savingsaccount()

       