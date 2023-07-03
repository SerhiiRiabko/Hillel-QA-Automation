class Mul:
    def __init__(self, speed, strenght):
        self.speed = speed
        self.strenght = strenght


class Horse:
    def __init__(self):
        self.speed = 50

    def __add__(self, other):
        return Mul(speed=self.speed, strenght=other.strenght)


class Donkey:
    def __init__(self):
        self.strenght = 25

    def __add__(self, other):
        return Mul(speed=other.speed, strenght=self.strenght)


if __name__ == '__main__':
    horse = Horse()
    donkey = Donkey()

    horse +=

