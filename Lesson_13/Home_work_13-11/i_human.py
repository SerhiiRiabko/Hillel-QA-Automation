from abc import ABC, abstractmethod

class IHuman(ABC):

    @abstractmethod
    def _pack_things(self):
        pass

    @abstractmethod
    def _consider_road(self):
        pass

    @abstractmethod
    def _un_pack_things(self):
        pass
