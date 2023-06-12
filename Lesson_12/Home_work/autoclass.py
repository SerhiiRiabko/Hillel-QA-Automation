from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self):
        self.__wheels = 4
        self.__body = 'metal'
        self.__engine = True
        self.__engine_type = None
# class Auto(ABC):
#     def __init__(self, wheels, body, engine, engine_type):
#         self.__wheels = wheels
#         self.__body = body
#         self.__engine = engine
#         self.__engine_type = engine_type

    def refuel(self):
        print('I need fuel')

    @abstractmethod
    def ride(self):
        pass


if __name__ == '__main__':
    auto = Auto
    auto.refuel(self=1)
