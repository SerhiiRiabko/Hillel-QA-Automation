class Human:
    def __int__(self, name, age, gender):
        self.name = name # if self.__name - private, self._name - protected
        self.age = age
        self.gender = gender
        self.security_data = {'card_namber': 12345, 'cvv': 766}

    def say_no(self):
        print(f'Hello: {self.name}')


if __name__ == '__main__':
    john = Human('John', 23, 'Male')

