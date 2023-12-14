class Bank:
    def __init__(self,name,_account,__balance):
        self.name = name
        self._account = _account
        self.__balance = __balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
        else:
            print("Insufficiet balance")
    
    def getbalance(self):
        return self.__balance
    
account1 = Bank('Kal',1001,600)
print(account1.getbalance())

account1.deposit(1000)
print(account1.getbalance())

account1.withdraw(5000)
print(account1.getbalance())