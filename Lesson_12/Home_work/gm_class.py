from abc import ABC, abstractmethod

from autoclass import Auto


class Gm(Auto, ABC):
    def __init__(self, wheels, body, engine, main_office_city, name, country):
        super().__init__(wheels=4, body='Metal', engine='Power Engines')
        self.__main_office_city = 'Detroit'
        self.__name = 'GM'
        self.__country = 'USA'

    @abstractmethod
    def electricity_problem(self):
        pass

    @abstractmethod
    def simple_repair(self):
        pass
