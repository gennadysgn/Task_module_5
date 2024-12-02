from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __ne__(self, other):
        return self.title != other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.current_user_age = None

    def log_in(self, nickname, password):
        for elem in self.users:
            if nickname == elem.nickname and password == elem.password:
                self.current_user = elem.nickname
                self.current_user_age = elem.age

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        for elem in self.users:
            if user.nickname == elem.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            self.users.append(user)
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, text):
        same_videos = []
        for elem in self.videos:
            if text.upper() in str(elem.title).upper():
                same_videos.append(str(elem.title))
        return same_videos

    def watch_video(self, title):
        time = []
        if self.current_user is not None:
            for elem in self.videos:
                if title in elem.title:
                    if elem.adult_mode is True and self.current_user_age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        self.log_out()
                    else:
                        for i in range(elem.time_now, elem.duration):
                            sleep(1)
                            i += 1
                            time.append(i)
                        print(*time, "Конец видео")
        else:
            print(f"Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
