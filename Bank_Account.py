class Account: #this is a superclass of class object, which hold two parameter name and account.
    def __init__(self, name, account):
        self.name = name
        self.account = account
#name and account are passed in the subclass via super()
class BankAccount(Account):
    def __init__(self, name, account, balance):
        super().__init__(name, account)
        self.__balance = balance # "private instance"

    def debit(self, money):
        assert self.__balance > money

        self.__balance -= money

    def credit(self, money):
        self.__balance += money

    def info(self):
        return (self.name, self.account, self.__balance)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, money):
        self.debit(self.__balance)
        self.credit(money)
#creating a static method.
class Manage:
    @staticmethod
    def transfer(debitAcc, creditAcc, money):
        debitAcc.debit(money)
        creditAcc.credit(money)

acc1 = BankAccount("Simon", "2020", 1000)
acc2 = BankAccount("Son Goku",'2121', 2000)
print(acc1.info())
print(acc2.info())
Manage.transfer(acc2, acc1, 1000)
print(acc1.info())
print(acc2.info())
