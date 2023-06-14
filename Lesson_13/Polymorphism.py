from abc import ABC, abstractmethod


class Cat(ABC):
    def __init__(self):
        self.color = None
        self.tail = None
        self.legs = 4

    @abstractmethod
    def make_noise(self):
        pass


class Lion(Cat):
    def __init__(self):
        super().__init__()

    def make_noise(self):
        super().make_noise()
        print("Rrrrrrrrrr")


class Tiger(Cat):
    def __init__(self):
        self.__color = "Tricolor"
        self.__tail = "Long"
        self.__legs = 4

    def make_noise(self):
        print("rhrhrhrhrh")

if __name__ == '__main__':
    lion = Lion()
    tiger = Tiger()

lion.make_noise()
tiger.make_noise()