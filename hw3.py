class Bank:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = balance

    def moneyX(self):
        add = int(input('Введите сумму, чтобы добавить денег на ваш счет:'))
        self._balance += add
        print(f'Ваш текущий балланс: {self._balance}')

    def _kill(self):
        self._balance = 0
        print('Ваш счет обнулен!')

    def _get_money(self, other):
        self._balance += other._balance
        other._balance = other._balance
        print(f"Балланс '{other._name}' был передан -> '{self._name}'\n"
              f"Ваш текущий балланс: {self._balance}\n"
              f"Балланс Azy: {other._balance}")

    def __jackpot(self):
        self._balance *= 10
        print(f"Поздравляем, ваш счет был умножен на 10"
              f"Вот ваш текущий счет: {self._balance}")

    def get_obj(self):
        return self.__jackpot

    # def set_obj(self, a):
    #     self.__jackpot = a


me = Bank('Aze', 100)
him = Bank('Ery', 100)
Bank.moneyX(me)
print(me.get_obj())
Bank._kill(me)


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b

    def __mul__(self):
        return self.a * self.b

    def __truediv__(self):
        return self.a / self.b


calculator = Calculator(200, 100)
print(f'Сложение: {calculator.__add__()}')
print(f'Вычитание: {calculator.__sub__()}')
print(f'Умножение: {calculator.__mul__()}')
print(f'Деление: {calculator.__truediv__()}')