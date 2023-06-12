from abc import ABC

from toyota_co_class import Toyota_Co


class Toyota(Toyota_Co, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country, brand,
                 city_office, motto):
        super().__init__(wheels=4, body='Metal', engine=engine, engine_type='fuel', main_office_city='Toyota It',
                         name='Toyota', country='Japan')
        self.brand = 'Toyota'
        self.city_office = 'Toyota It'
        self.motto = 'Drive your dream'

    def latest_developments(self):
        print(f'{self.brand} can ride more 700k')

    def ride(self):
        print(f'Your ride will be good with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office}')
