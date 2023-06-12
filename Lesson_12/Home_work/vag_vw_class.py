from abc import ABC

from vag_class import Vag


class Vw(Vag, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country, brand='VW',
                 city_office='Wolfsburg', motto='Das auto'):
        super().__init__(wheels, body, engine, engine_type, main_office_city, name, country)
        self.__brand = brand
        self.__city_office = city_office
        self.__motto = motto

    def work_long_without_crash(self):
        print('I have a reliable engine and choir')

    def hard_repair(self):
        print('Only some services can repair your car')

    def ride(self):
        print('Your ride will be nice')

    def say_motto(self):
        print(self.motto)

    def info_brand(self):
        Vw.say_motto()
        print(f'Office of {self.brand} in {self.city_office}')


if __name__ == '__main__':
    vw = Vw()
    vw.info_brand(self)
