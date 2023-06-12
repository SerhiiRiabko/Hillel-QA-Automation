from abc import ABC

from toyota_co_class import Toyota_Co


class Daihatsu(Toyota_Co, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country, brand,
                 city_office, motto):
        super().__init__(wheels=4, body='Metal', engine=engine, engine_type='fuel', main_office_city='Toyota It',
                         name='Toyota', country='Japan')
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

    def electricity_problem(self):
        print(f'{self.brand} has troubles wit electricity')

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office}')
