class Calculation:
    def __init__(self, number_one, number_two):
        self.number_one = number_one

        self.number_two = number_two

    def __add__(self):
        return self.number_one + self.number_two

    def __sub__(self):
        return self.number_one - self.number_two

    def __mul__(self):
        return self.number_one * self.number_two

    def __truediv__(self):
        return self.number_one / self.number_two


a = Calculation(26, 30)

print(a.__add__())

print(a.__sub__())

print(a.__mul__())

print(a.__truediv__())
