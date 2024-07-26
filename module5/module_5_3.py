class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    # сложение
    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)


    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    # вычитание
    def __sub__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors - value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors - value.number_of_floors)

    def __isub__(self, value):
        return self - value

    def __rsub__(self, value):
        if isinstance(value, int):
            return value - self.number_of_floors

    # умножение
    def __mul__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors * value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors * value.number_of_floors)

    def __isub__(self, value):
        return self * value

    def __rsub__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors * value)

    # деление целочисленное
    def __floordiv__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors // value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors // value.number_of_floors)
        return self

    def __ifloordiv__(self, value):
        return self // value

    def __rfloordiv__(self, value):
        if isinstance(value, int):
            return value // self.number_of_floors
        if isinstance(value, House):
            return value.number_of_floors // self.number_of_floors

    # нецелочисленное деление для количества этажей выглядит странно, потому перегрузка в целочисленное :-)
    def __truediv__(self, value):
        return self // value

    def __itruediv__(self, value):
        return self // value

    def __rtruediv__(self, value):
        return value // self

    # остаток от деления
    def __mod__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors % value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors % value.number_of_floors)
        return self

    def __imod__(self, value):
        return self % value

    def __rmod__(self, value):
        if isinstance(value, int):
            return value % self.number_of_floors
        if isinstance(value, House):
            return value.number_of_floors % self.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h3 = h1 + 10 # __add__
h3.name = 'ЖК Столбы'
print(h1)
print(h3)
print(h3 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h3 = h1 / 2
print(h3)
print(h1)