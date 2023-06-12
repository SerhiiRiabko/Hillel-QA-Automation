from abc import ABC, abstractmethod

from autoclass import Auto


class Vag(Auto, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country):
        super().__init__(wheels=wheels, body=body, engine=engine, engine_type=engine_type)
        self.main_office_city = 'Wolfsburg'
        self.name = 'VAG'
        self.country = 'Germany'

    @abstractmethod
    def work_long_without_crash(self):
        pass

    @abstractmethod
    def hard_repair(self):
        pass
