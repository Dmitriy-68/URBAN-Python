from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, n):
        self.n = n
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait = randint(3, 10)
        sleep(wait)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for g in guests:
            arr = False
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    g.start()
                    print(f'{g.name} сел(-а) за стол номер {t.n}')
                    arr = True
                    break
            if not arr:
                self.queue.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        def none_guests():
            flag = True
            for t in self.tables:
                if t.guest is None:
                    continue
                flag = False
            return flag

        while not (self.queue.empty() and none_guests()):
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {t.n} свободен')
                    t.guest = None
                    if not self.queue.empty():
                        t.guest = self.queue.get()
                        print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.n}')
                        t.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
