from abc import ABC, abstractmethod


class IWalking(ABC):

    @abstractmethod
    def _walk(self):
        pass

    @abstractmethod
    def _start_walk(self, x:int, y:int):
        pass

    @abstractmethod
    def _finish_walk(self):
        pass
