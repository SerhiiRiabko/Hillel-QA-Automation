from datetime import datetime


class Human:
    def __init__(self, name, year_birth):
        self.__name = name
        self.__year_birth = year_birth
        self.__is_live = True
        self.__current_age = datetime.now().year - self.__year_birth

    @property
    def name(self):
        return self.__name.capitalize()

    @property
    def years_birth(self):
        return self.__year_birth

    # @age.setter
    # def age(self, new_age):
    #     if new_age > self.__year_birth and isinstance(new_age, int):
    #         self.__year_birth = new_age
    #     else:
    #         print('Warning, new age less previous')
    #     if self.__year_birth > 100:
    #         self.__make_dead()
    def increase_age(self):
        now = datetime.now().year
        current_age = now - self.__year_birth
        if self.__current_age > 100:
            self.__make_dead()
            print('You are dead')
        self.__current_age += 1

    def get_current_age(self):
        now = datetime.now().year
        current_age = now - self.__year_birth
        return current_age

    def __make_dead(self):
        self.__is_live = False
        print('Person dead')


if __name__ == '__main__':
    peter = Human('peter', 1923)
    homer = Human('Homer', 36)

    print(peter.get_current_age())
    peter.increase_age()
    peter.increase_age()

