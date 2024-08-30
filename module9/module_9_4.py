from random import choice

# Lambda-функция
first = 'Мама мыла раму'
second = 'Раму мыла мама'

print(list(map(lambda x, y: x == y, first, second)))


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for str_ in data_set:
                file.write(str(str_) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка из букв', ['А', 'это', 'уже', 'число', 5, 'в', 'списке', 'слов'])


# Метод __call__
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть')
print(first_ball())
print(first_ball())
print(first_ball())
