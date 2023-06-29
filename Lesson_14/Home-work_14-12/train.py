from wagon import Wagon
class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __repr__(self):
        wagon_list = "\n".join([str(wagon) for wagon in self.wagons])
        return f"Train:\n{wagon_list}"

    def __repr__(self):
        wagon_list = "-".join([str(wagon.number) for wagon in self.wagons])
        return f"<=[HEAD]-[{wagon_list}]"


train = Train()

wagon1 = Wagon(1)
wagon1.add_passenger("Passenger 1")
wagon1.add_passenger("Passenger 2")

wagon2 = Wagon(2)
wagon2.add_passenger("Passenger 3")
wagon2.add_passenger("Passenger 4")
wagon2.add_passenger("Passenger 5")

train.add_wagon(wagon1)
train.add_wagon(wagon2)

print(len(wagon1))  # Output: 2
print(len(wagon2))  # Output: 3
print(len(train))  # Output: 2

print(wagon1)
print(wagon2)

print(train)


wagon1 = Wagon(1)
wagon2 = Wagon(2)
wagon3 = Wagon(3)
wagon4 = Wagon(4)

train.add_wagon(wagon1)
train.add_wagon(wagon2)
train.add_wagon(wagon3)
train.add_wagon(wagon4)

print(train)






