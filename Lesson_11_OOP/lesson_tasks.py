# from math import pi
#
#
# class Circles:
#     def __init__(self, radius: float or int):
#         self.radius = radius
#
#     def calculate_square(self):
#         return pi * pow(self.radius, 2)
#
#
# if __name__ == '__main__':
#     circle = Circles(2)
#
# print(circle.calculate_square())

# Change card balances

class Bank:
    def __init__(self, balance: float or int):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def add_money(self, amount_of_money):
        if amount_of_money > 0:
            self.__balance += amount_of_money
        else:
            raise ValueError('Positive only')

    def decrease_money(self, amount_of_money):
        if amount_of_money < 0 or self.__balance >= amount_of_money:
            self.__balance -= amount_of_money
        else:
            raise ValueError('Not enough money')


if __name__ == '__main__':
    bank = Bank(11000)

    bank.add_money(600)
    print(bank.balance)

    bank.decrease_money(1600)
    print(bank.balance)
