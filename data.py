import random
import string


class Main:
    URL = "https://stellarburgers.nomoreparties.site/"


class UserData:
    # Для авторизации
    NAME = "Vladimir"
    EMAIL = 'vladimir_nikolaev_5_619@ucxxj.com'
    PASSWORD = 'VgBXfSiaoSv4IaKl9m8m'


class RandomUserData:
    """Для генерации логина и пароля"""

    def __init__(self):
        self.name = "Vladimir"
        self.email = self.__generate_random_login()
        self.good_password = self.__generate_random_password_valid()
        self.bad_password = self.__generate_random_password_not_valid()

    def __generate_random_login(self):
        """Генератор логина/почты"""
        random_digit = random.randint(100, 999)
        all_symbols = string.ascii_lowercase
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(1, 5)))
        email = f"vladimir_nikolaev_5_{random_digit}@{result}.com"
        return email

    def __generate_random_password_valid(self):
        """Генератор валидного пароля"""
        all_symbols = string.ascii_letters + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(6, 20)))
        return result

    def __generate_random_password_not_valid(self):
        """Генератор пароля,, который не соответствует требованиям (по длине)"""
        all_symbols = string.ascii_letters + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(1, 6)))
        return result

    def get_user_info(self, key=None):
        """для получения данных из класса"""
        data = {"name": self.__name, "email": self.__email, "password": self.__password}
        if key:
            return data[key]
        return {"name": self.__name, "email": self.__email, "password": self.__password}
