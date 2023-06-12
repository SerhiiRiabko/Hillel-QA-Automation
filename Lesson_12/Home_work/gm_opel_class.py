from abc import ABC

from gm_class import Gm


class Opel(Gm, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country, brand,
                 city_office, country_brand, motto):
        super().__init__(wheels=4, body='Metal', engine=engine, engine_type='fuel', main_office_city='Detroit',
                         name='GM', country='USA')
        self.brand = 'Opel'
        self.city_office = 'Rosselhaim'
        self.country_brand = 'Germany'
        self.motto = 'Open own Opel'

    def work_long_without_crash(self):
        print(f'{self.brand} has a reliable engine and choir')

    def hard_repair(self):
        print(f'Only some services can repair your car - {self.brand}')

    def ride(self):
        print(f'Your ride will be nice with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def electricity_problem(self):
        print(f'{self.brand} has troubles wit electricity')

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office} - {self.country_brand}')
