from general_motors import Gm


class Opel(Gm):
    def __init__(self):
        super().__init__()
        self._brand = 'Opel'
        self._city_office = 'Rosselhaim'
        self._country_brand = 'Germany'
        self._motto = 'Open own Opel'

    def work_long_without_crash(self):
        print(f'{self._brand} has a reliable engine and choir')

    def hard_repair(self):
        print(f'Only some services can repair your car - {self._brand}')

    def refuel(self):
        print("I need good petrol")

    def simple_repair(self):
        print(f'{self._brand} has good repairebilitty')

    def ride(self):
        print(f'Your ride will be nice with {self._brand}')

    def say_motto(self):
        print(self._motto)

    def electricity_problem(self):
        print(f'{self._brand} has troubles wit electricity')

    def info_brand(self):
        print(f'Office of {self._brand} in {self._city_office} - {self._country_brand}')
