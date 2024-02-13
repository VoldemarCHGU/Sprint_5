import random
import string

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.locators import LocatorsForRegistrationAndAndLogin


class RegisterPage:
    def __init__(self):
        self.url = "https://stellarburgers.nomoreparties.site/register"
        self.__name = "Vladimir"
        self.__email = self.__generate_random_login()
        self.__password = self.__generate_random_password()

    def get_user_info(self, key=None):
        data = {"name": self.__name, "email": self.__email, "password": self.__password}
        if key:
            return data[key]
        return {"name": self.__name, "email": self.__email, "password": self.__password}

    def __generate_random_login(self):
        """Генератор логина/почты"""
        random_digit = random.randint(100, 999)
        all_symbols = string.ascii_lowercase
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(1, 5)))
        email = f"vladimir_nikolaev_5_{random_digit}@{result}.com"
        return email

    def __generate_random_password(self):
        """Генератор пароля"""
        all_symbols = string.ascii_letters + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(8, 20)))
        return result

    def set_new_pass(self, password):
        self.__password = password

    def registration_uesr(self, driver: WebDriver):
        # Находим нужные локаторы для заполнения нового пользователя
        input_name = driver.find_element(*LocatorsForRegistrationAndAndLogin.INPUT_NAME)
        input_email = driver.find_element(*LocatorsForRegistrationAndAndLogin.INPUT_EMAIL)
        input_password = driver.find_element(*LocatorsForRegistrationAndAndLogin.INPUT_PASSWORD)
        btn_register = driver.find_element(*LocatorsForRegistrationAndAndLogin.BTN_REGISTER)

        # Заполняем данными нового пользователя
        input_name.send_keys(self.get_user_info('name'))
        input_email.click()
        input_email.send_keys(self.get_user_info('email'))
        input_password.click()
        input_password.send_keys(self.get_user_info('password'))
        btn_register.click()
