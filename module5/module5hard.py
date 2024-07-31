import time


class User:
    """
    Класс пользователя.
    Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    """
    Класс видео.
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    """
    Класс UrTube.
    Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

# регистрация нового пользователя с одновременным входом в аккаунт
    def register(self, nickname, password, age):
        for us in self.users:
            if us.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        self.users.append(User(nickname, hash(password), age))
        self.log_in(nickname, password)

# вход существующего пользователя в аккаунт
    def log_in(self, nickname, password):
        for us in self.users:
            if us.nickname == nickname:
                if us.password == hash(password):
                    self.current_user = nickname

# выход из аккаунта
    def log_out(self):
        self.current_user = None

# добавление видео(можно несколько) в список
    def add(self, *args):
        for i in args:
            flag = True
            for j in self.videos:
                if i.title == j.title:
                    flag = False
            if flag:
                self.videos.append(i)

# поиск видео по ключевому слову
    def get_videos(self, request):
        response = []
        for i in self.videos:
            if request.upper() in i.title.upper():
                response.append(i.title)
        return response

# просмотр видео с анализом ограничений
    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for i in self.videos:
            if i.title == title:
                if i.adult_mode == True:
                    for j in self.users:
                        if j.nickname == self.current_user:
                            if j.age < 18:
                                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                                return
                while i.time_now < i.duration:
                    time.sleep(1)
                    i.time_now += 1
                    print(i.time_now, end=' ')
                print('Конец видео', end='\n')
                i.time_now = 0



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
v3 = Video('Лучший язык программирования 2024 года', 777, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')