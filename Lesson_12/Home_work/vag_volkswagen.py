from abc import ABC

from vag import Vag


class Volkswagen(Vag, ABC):
    def __init__(self):
        super().__init__()
        self.brand = 'Vw'
        self.city_office = 'Wolfsburg'
        self.motto = 'Das auto'

    def work_long_without_crash(self):
        print(f'{self.brand} has a reliable engine and choir')

    def refuel(self):
        self.work_long_without_crash()
        print('But I need fuel')

    def hard_repair(self):
        print(f'Only some services can repair your car - {self.brand}')

    def ride(self):
        print(f'Your ride will be nice with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def info_brand(self):
        self.say_motto()
        print(f'Office of {self.brand} in {self.city_office}')
