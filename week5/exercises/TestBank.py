import  unittest

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
    
class TestBank(unittest.TestCase):

    def setUp(self):
        self.account1 = Bank('Kal',1001,600)
    def test_balance(self):
        self.assertEqual(self.account1.getbalance(),600,"Wrong balance")

    def test_deposit(self):
        self.account1.deposit(1000)
        self.assertEqual(self.account1.getbalance(),1600,"Deposition is incorrect")

    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.getbalance(),100,"Withdraw is incorrect")

    def test_insufficient_withdraw(self):
        self.account1.withdraw(3000)
        self.assertEqual(self.account1.getbalance(),600,"Withdrawed while insufficient amount")
    #or
    # def test_insufficient_withdraw(self):
    #     with self.assertRaises(ValueError):
    #         self.account1.withdraw(3000)
if __name__ == '__main__':
    unittest.main()