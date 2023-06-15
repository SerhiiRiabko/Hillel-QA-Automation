from toyota_co import ToyotaCo


class Lexus(ToyotaCo):
    def __init__(self):
        super().__init__()
        self.brand = 'Lexus'
        self.city_office = 'Nagoia'
        self.motto = 'The passionate of potential'

    def latest_developments(self):
        print(f'{self.brand} can ride more 700k')

    def ride(self):
        print(f'Your ride will be agressive with {self.brand}')

    def say_motto(self):
        print(self.motto)
        lexus = Lexus()
        lexus.reliable()

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office}')

    def reliable(self):
        print('You pay much but for a long time')

    def refuel(self):
        print(f'{self.brand} likes only good fuel')
