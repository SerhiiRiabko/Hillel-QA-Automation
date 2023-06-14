from vag_class import Vag


class Porsche(Vag):
    def __init__(self):
        super().__init__()
        self._brand = 'Porsche'
        self._city_office = 'Shtudgard'
        self._motto = 'Time is priceless'

    def work_long_without_crash(self):
        print(f'{self._brand} has a power engines')

    def refuel(self):
        print('I use a good fuel for more power')

    def hard_repair(self):
        print(f'Very expensive to repair - {self._brand}')

    def ride(self):
        print(f'Your ride will be nice with {self._brand}')

    def say_motto(self):
        print(self._motto)

    def info_brand(self):
        self.say_motto()
        print(f'Office of {self._brand} in {self._city_office}')
