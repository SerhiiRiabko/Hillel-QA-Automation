from abc import ABC, abstractmethod


class IWalking(ABC):

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def start_walk(self, x:int, y:int):
        pass

    @abstractmethod
    def finish_walk(self):
        pass
