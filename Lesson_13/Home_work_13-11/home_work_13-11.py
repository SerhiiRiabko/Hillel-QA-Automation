from time import sleep, time

from abc import ABC

from i_human import IHuman
from i_walking import IWalking


class Traveller(IHuman, IWalking, ABC):
    def __init__(self):
        self._walk_status = False
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        self.finish = True
        self.__tired = 0

    def walk(self, x: int, y: int):
        while self.__walk_point_x != x or self.__walk_point_y != y:
            if self.__walk_point_x != x:
                self.__walk_point_x += 1
            if self.__walk_point_y != y:
                self.__walk_point_y += 1
            sleep(0.1)
            print('I am traveling')

            sleep(1.0)

    print('I am walking to EndPoint')

    def traveling(self, x, y):
        start_time = time()
        self._walk_status = True
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        self.pack_things()
        self.consider_road()
        self.start_walk()
        self.walk(x=x, y=y)
        self.finish_walk()
        self.un_pack_things()
        self.reset_position()
        self.finish = True
        finish_time = time()
        print(f'I have traveled for {(finish_time - start_time)}')
        self.__tired += 35

    def reset_position(self):
        self.__walk_point_x = 0
        self.__walk_point_y = 0

    def start_walk(self):
        self._walk_status = True
        print('I start my travel')

    def finish_walk(self):
        self._walk_status = False
        self.finish = True
        print('I have finished my travel')

    def pack_things(self):
        self._walk_status = False
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        print('I am packing my things')

    def consider_road(self):
        self._walk_status = False
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        print('I am planning my travel')

    def un_pack_things(self):
        self._walk_status = False
        print('I am unpacking my things!')


if __name__ == '__main__':
    traveller = Traveller()
    traveller.traveling(3, 7)
