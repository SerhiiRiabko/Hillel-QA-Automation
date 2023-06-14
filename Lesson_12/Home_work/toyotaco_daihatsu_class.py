from toyota_co_class import ToyotaCo


class Daihatsu(ToyotaCo):
    def __init__(self):
        super().__init__()
        self.brand = 'Daihatsu'
        self.city_office = 'Osaka'
        self.motto = 'Light you up'

    def latest_developments(self):
        print(f'{self.brand} can ride more 300k')

    def hard_repair(self):
        print(f'Only some services can repair your car - {self.brand}')

    def ride(self):
        print(f'Your ride will be nice with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def refuel(self):
        print(f'{self.brand} go for a fuel')

    def reliable(self):
        print('My parts is expensive as for Lexus or Toyota')

    def electricity_problem(self):
        print(f'{self.brand} has troubles with electricity')

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office}')


if __name__ == '__main__':
    daihatsu = Daihatsu()
    daihatsu.electricity_problem()
