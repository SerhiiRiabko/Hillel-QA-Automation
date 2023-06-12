from abc import ABC, abstractmethod

from autoclass import Auto


class Toyota_Co(Auto, ABC):
    def __init__(self, wheels, body, engine, engine_type, main_office_city, name, country):
        super().__init__(wheels=4, body='Metal', engine=engine, engine_type='fuel')
        self.__main_office_city = 'Toyota(IT)'
        self.__name = 'Toyota'
        self.__country = 'Japan'

    @abstractmethod
    def latest_developments(self):
        pass

    @abstractmethod
    def reliable(self):
        pass
