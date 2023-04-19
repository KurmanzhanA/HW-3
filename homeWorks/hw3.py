class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        add_money = float(input('Введите сумму добавления: '))
        return self._balance + add_money

    def _kill(self):
        # withdraw_money = float(input('Введите сумму добавления: '))
        # print(self._balance - withdraw_money)
        self._balance = 0
        return self._balance

    @property
    def kill(self):
        return self._kill()

    def __jackpot(self):
        return self._balance * 10

    @property
    def jackpot(self):
        return self.__jackpot()

    def _manipulation(self, other):
        return f'Ваш сложенный баланс {self._balance + other._balance} было {self._balance}'

    @property
    def manipulation(self):
        return self._manipulation(a)


b = Bank('Optima', 2000)
a = Bank('Mbank', 1000)
print(b.moneyX())
print(b.jackpot)
print(b.manipulation)
print(b.kill)
