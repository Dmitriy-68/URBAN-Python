import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.sides_count == len(sides):
            self.__sides = list(sides)
        else:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r in range(0, 256) and g in range(0, 256) and b in range(0, 256)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if self.sides_count == len(new_sides):
            for i in new_sides:
                if not (isinstance(i, int) and i > 0):
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

    def set_sides(self, *new_sides):
        if self.sides_count == len(new_sides) and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        p = self.__len__() / 2  # полупериметр
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        self.__height = 2 * math.sqrt(p * (p - a) * (p - b) * (p - c)) / a  # высота к стороне a

    def get_square(self):
        return self.__height * self.get_sides()[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        list_sides = []
        if len(sides) == 1:
            list_sides += [sides[0]] * 12
        super().__init__(color, *list_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# (Цвет, стороны)
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
print(f'Circle {circle1.get_sides()}, {circle1.get_color()}')
print(f'Cube {cube1.get_sides()}, {cube1.get_color()}')

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'Circle color {circle1.get_color()}')
cube1.set_color(300, 70, 15)  # Не изменится
print(f'Cube color {cube1.get_color()}')

circle1.set_color(55, 66, -5)  # не изменится
print(f'Circle color {circle1.get_color()}')

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(f'Cube sides {cube1.get_sides()}')
circle1.set_sides(15)  # Изменится
print(f'Circle sides {circle1.get_sides()}')

# Проверка периметра (круга), это и есть длина:
print(f'Circle perimetr {len(circle1)}')
print(f'Circle square {circle1.get_square()}')

# Треугольник
triangle1 = Triangle((10, 152, 200), 3, 4, 5)
print(f'Triangle {triangle1.get_color()}, {triangle1.get_sides()}')
print(f'Triangle square {triangle1.get_square()}')

# Куб
print(f'Cube volume {cube1.get_volume()}')
