class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        add_money = float(input('Input the amount to add: '))
        return self._balance + add_money

    def _kill(self):
        withdraw_money = float(input('Input the amount to withdraw: '))
        print(self._balance - withdraw_money)
        # self._balance
        # return self._balance

    @property
    def kill(self):
        return self._kill()

    def __jackpot(self):
        return self._balance * 10

    @property
    def jackpot(self):
        return self.__jackpot()

    def _manipulation(self, other):
        return f'Your total balance {self._balance + other._balance} was {self._balance}'

    @property
    def manipulation(self):
        return self._manipulation(a)


b = Bank('Bakai', 20000)
a = Bank('Demir', 10000)
print(b.moneyX())
print(b.jackpot)
print(b.manipulation)
print(b.kill)
print(a.moneyX())
print(a.jackpot)
print(a.manipulation)
print(a.kill)