from abc import ABC

from vag_class import Vag


class Vw(Vag, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country, brand,
                 city_office, motto):
        super().__init__(wheels=4, body='Metal', engine=engine, engine_type='fuel', main_office_city='Wolfsburg',
                         name='Vag', country='Germany')
        self.brand = 'Vw'
        self.city_office = 'Wolfsburg'
        self.motto = 'Das auto'

    def work_long_without_crash(self):
        print(f'{self.brand} has a reliable engine and choir')

    def hard_repair(self):
        print(f'Only some services can repair your car - {self.brand}')

    def ride(self):
        print(f'Your ride will be nice with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def info_brand(self):
        Vw.say_motto()
        print(f'Office of {self.brand} in {self.city_office}')
