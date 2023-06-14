from abc import ABC

from gm_class import Gm


class Gmc(Gm, ABC):
    def __init__(self):
        super().__init__()
        self.brand = 'GMC'
        self.city_office = 'Detroit'
        self.motto = 'Everybody in'

    def work_long_without_crash(self):
        print(f'{self.brand} has a reliable engine and choir')

    def refuel(self):
        print('Please buy more petrol. I like 92!!!')

    def simple_repair(self):
        print(f'Only some services can repair your car - {self.brand}')

    def ride(self):
        print(f'Your ride will be nice with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def electricity_problem(self):
        print(f'{self.brand} has troubles wit electricity')

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office}')
