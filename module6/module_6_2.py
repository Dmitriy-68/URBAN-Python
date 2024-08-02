class Vehicle:
    __COLOR_VARIANTS = ['blue', 'orange', 'red', 'green', 'magenta', 'white', 'pink']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power} л.с.')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        flag = False
        for i in self.__COLOR_VARIANTS:
            if new_color.upper() == i.upper():
                self.__color = new_color
                flag = True
                break
        if not flag:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Feodor', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()
print()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print()

# Проверяем что поменялось
vehicle1.print_info()
