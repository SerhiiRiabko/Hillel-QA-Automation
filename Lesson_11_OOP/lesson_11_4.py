class Human:
    def __int__(self, name, age, gender):
        self.__name = name  # if self.__name - private, self._name - protected
        self.__age = age
        self.__gender = gender
        self.__security_data = {'card_namber': 12345, 'cvv': 766}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 20:
            self__name = new_name
        else:
            raise TypeError(f'Name not a string or the length more 20 {type(new_name)}')