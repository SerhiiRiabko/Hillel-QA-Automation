class Auto:

    # def __new__(cls, *args, **kwargs):
    #     print('From New')
    #     instance = super().__new__()
    #     return instance
    #     print('From New')
    #     instance = super().__new__()
    #       return instance

    # def __new__(cls, model: str):
    #     if not isinstance(model, str):
    #         raise TypeError('Model should be string')
    #     instance = super().__new__(cls)
    #     return instance
    #
    # def __repr__(self):
    #     return 'Auto(model = "X6"'

    def __init__(self, model: str):
        self.__model = model
        self.__doors = 4
        self.__color = 'Green'
        print('Hello init')

    # def __repr__(self):
    #     return 'Auto(model = "X6")'
    # 
    # def __getattr__(self, item):
    #     return item

    # def __getattribute__(self, item):
    #     if item.startswith('_Auto'):
    #         raise Warning('No access')
    #     return super().__getattribute__(item)
    # def __setattr__(self, key, value):
    #     if key == '_Auto_model' and not isinstance(value, str):
    #         raise TypeError('Only STR')
    #     super().__setattr__(key, value)


if __name__ == '__main__':
    bmw = Auto(model='X5')

