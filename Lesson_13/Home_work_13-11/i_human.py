from abc import ABC, abstractmethod

class IHuman(ABC):

    @abstractmethod
    def pack_things(self):
        pass

    @abstractmethod
    def consider_road(self):
        pass

    @abstractmethod
    def un_pack_things(self):
        pass
