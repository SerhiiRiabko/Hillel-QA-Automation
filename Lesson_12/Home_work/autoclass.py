from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, wheels, body, engine, engine_type):
        self.__wheels = wheels
        self.__body = body
        self.__engine = engine
        self.__engine_type = engine_type

    @abstractmethod
    def refuel(self):
        pass

    @abstractmethod
    def ride(self):
        pass
