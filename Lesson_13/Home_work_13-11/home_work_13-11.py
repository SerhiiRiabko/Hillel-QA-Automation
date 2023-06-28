from time import sleep, time

from abc import ABC

from i_human import IHuman
from i_walking import IWalking


class Traveller(IHuman, IWalking, ABC): #inheritance
    def __init__(self):
        self._walk_status = False
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        self.finish = True
        self.__tired = 0

    def _walk(self, x: int, y: int):
        while self.__walk_point_x != x or self.__walk_point_y != y:
            if self.__walk_point_x != x:
                self.__walk_point_x += 1
            if self.__walk_point_y != y:
                self.__walk_point_y += 1
            sleep(0.1)
            print('I am traveling')

            sleep(1.0)

    print('I am walking to EndPoint')

    #encapsulation
    def traveling(self, x, y):
        #
        start_time = time()
        self._walk_status = True
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        self._pack_things()
        self._consider_road()
        self._start_walk()
        self._walk(x=x, y=y)
        self._finish_walk()
        self._un_pack_things()
        self.reset_position()
        self.finish = True
        finish_time = time()
        print(f'I have traveled for {(finish_time - start_time)}')
        self.__tired += 35

    def reset_position(self):
        # encapsulation
        self.__walk_point_x = 0
        self.__walk_point_y = 0

    def _start_walk(self):
        self._walk_status = True
        print('I start my travel')

    def _finish_walk(self):
        self._walk_status = False
        self.finish = True
        print('I have finished my travel')

    def _pack_things(self):
        self._walk_status = False
        self.__walk_point_x = 0 #encapsulation
        self.__walk_point_y = 0 #encapsulation
        print('I am packing my things')

    def _consider_road(self):
        self._walk_status = False
        self.__walk_point_x = 0
        self.__walk_point_y = 0
        print('I am planning my travel')

    def _un_pack_things(self):
        self._walk_status = False
        print('I am unpacking my things!')


if __name__ == '__main__':
    traveller = Traveller()
    traveller.traveling(3, 7)
