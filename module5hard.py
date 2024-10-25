import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname:
                if hash(i.password) == hash(password):
                    self.current_user = i
                    print(f"Пользователь {nickname} вошел!")
                    return 0
                else:
                    print("Неверный пароль!")
                    return 0
        else:
            print(f"Пользователь {nickname} не зарегистрирован")
            return 0

    def register(self, nickname_str, password, age):
        if not self.users:
            new_user = User(nickname_str, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Здравствуйте '{new_user.nickname}'!")
        else:
            new_user = User(nickname_str, password, age)
            for i in self.users:
                if i.nickname == new_user.nickname:
                    print(f"Пользователь {new_user.nickname} уже существует")
                    return 0
                else:
                    new_user = User(nickname_str, password, age)
                    self.users.append(new_user)
                    self.current_user = new_user
                    print(f"Здравствуйте '{new_user.nickname}'!")
                    return 0

    def log_out(self):
        print(f'Пользователь "{self.current_user.nickname}" вышел')
        self.current_user = None
        return self.current_user

    def add(self, *obj_video):
        if isinstance(obj_video, tuple):
            if not self.videos:
                for i in obj_video:
                    self.videos.append(i)
                return 0
            for i in obj_video:
                for j in self.videos:
                    if j.title == i.title:
                        continue
                    else:
                        self.videos.append(i)
        elif isinstance(obj_video, object):
            if not self.videos:
                self.videos.append(obj_video)
            else:
                for i in self.videos:
                    if obj_video.title == i.title:
                        continue
                    else:
                        self.videos.append(obj_video)

    def get_videos(self, title_video):
        list_ = []
        for i in self.videos:
            if title_video.lower() in i.title.lower():
                list_.append(i.title)
        return list_

    def watch_video(self, title_video):
        if self.current_user is not None:
            for i in self.videos:
                if i.title == title_video:
                    if i.adult_mode is False:
                        time.sleep(i.duration)
                        for j in range(1, i.duration+1):
                            print(j, end='')
                        print(" Конец видео")
                        return 0
                    elif i.adult_mode is True and self.current_user.age >= 18:
                        time.sleep(i.duration)
                        for j in range(1, i.duration + 1):
                            print(j, end='')
                        print(" Конец видео")
                        return 0
                    else:
                        print("Вам нет 18 лет, пожалуйста, покиньте страницу")
            print('Не верное название видео')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


urY = UrTube()

vid1 = Video("Классы это и есть ООП?", 7, adult_mode = True)
vid2 = Video("Топ 5 советов по программированию", 10)
vid3 = Video("Чем отличается медведь от 'духовки'?", 9)

urY.add(vid1, vid2, vid3)

print(urY.get_videos('Класс'))
print(urY.get_videos('ПРОГ'))

urY.watch_video('Классы это и есть ООП?')
urY.register('vasya_pupkin', 'lolkekcheburek', 13)
urY.watch_video('Классы это и есть ООП?')
urY.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
urY.watch_video('Классы это и есть ООП?')
urY.watch_video('Для чего девушкам парень программист?')
urY.log_in('vasya_pupkin', 'lolkekcheburek')
urY.log_out()
