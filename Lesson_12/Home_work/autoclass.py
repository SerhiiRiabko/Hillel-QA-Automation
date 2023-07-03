from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, wheels, body, engine, engine_type):
        self._wheels = wheels
        self._body = body
        self._engine = engine
        self._engine_type = engine_type

    @abstractmethod
    def refuel(self):
        pass

    @abstractmethod
    def ride(self):
        pass
