from gm_class import Gm


class Holden(Gm):
    def __init__(self):
        super().__init__()
        self.brand = 'Holden'
        self.city_office = 'Melbourne'
        self.country_brand = 'Australia'
        self.motto = 'Go better'

    def work_long_without_crash(self):
        print(f'{self.brand} has a reliable engine and choir')

    def simple_repair(self):
        print(f'Simple construction of {self.brand} helps anyone to repair it himself')

    def ride(self):
        print(f'Your ride will be nice with {self.brand}')

    def say_motto(self):
        print(self.motto)

    def electricity_problem(self):
        print(f'{self.brand} has troubles wit electricity')

    def refuel(self):
        print('This car use 92 or 95 petrol')

    def info_brand(self):
        print(f'Office of {self.brand} in {self.city_office} - {self.country_brand}')


if __name__ == '__main__':
    holden = Holden()
    holden.info_brand()
    holden.simple_repair()
