from vag_class import Vag


class Audi(Vag):
    def __init__(self):
        super().__init__()
        self._brand = 'Audi'
        self._city_office = 'Ingolshtad'
        self._motto = 'Advancement through technology'

    def work_long_without_crash(self):
        print(f'{self._brand} has a reliable engine and choir')

    def hard_repair(self):
        print(f'Difficult to repair - {self._brand}')

    def refuel(self):
        print('Good fuel - Good ride')

    def ride(self):
        print(f'Your ride will be nice with {self._brand}')

    def say_motto(self):
        print(self._motto)

    def info_brand(self):
        self.say_motto()
        print(f'Office of {self._brand} in {self._city_office}')
