class File:

    def __init__(self, path, mode):
        self.__path = path
        self.__mode = mode
        self.__file = None

    def read(self):
        return self.__file.read()

    def __enter__(self):
        self.__file = open(self.__path, self.__mode)
        return self

   def __exit__(self, exc_type, exc_val, exc_tb):
       self.__file.close

if __name__ == '__main__':
    with File('text.txt', r) as file