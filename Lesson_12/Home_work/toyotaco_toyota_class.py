from toyota_co_class import ToyotaCo


class Toyota(ToyotaCo):
    def __init__(self):
        super().__init__()
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

    def refuel(self):
        print(f'I need fuel')

    def reliable(self):
        print(f'No trouble to fix {self.brand}')


if __name__ == '__main__':
    toyota = Toyota()
    toyota.info_brand()
