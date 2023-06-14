class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius ** 2


class Rectangle(Shape):
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    def calculate_area(self):
        return self.__weight * self.__height


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(7, 10)

    print(circle.calculate_area())
    print(rectangle.calculate_area())
