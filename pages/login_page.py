from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import LocatorsForRegistrationAndAndLogin


class LoginPage:
    def __init__(self, name, email, password, driver: WebDriver = None):
        self.url = "https://stellarburgers.nomoreparties.site/login"
        self.__name = name
        self.__email = email
        self.__password = password
        if driver:
            driver.get(self.url)

    def get_user_info(self, key=None):
        data = {"name": self.__name, "email": self.__email, "password": self.__password}
        if key:
            return data[key]
        return {"name": self.__name, "email": self.__email, "password": self.__password}

    def set_new_user_data(self, data):
        if data:
            self.__name = data.get('name')
            self.__email = data.get('email')
            self.__password = data.get('password')

    def auth_user(self, driver: WebDriver):
        input_email = driver.find_element(*LocatorsForRegistrationAndAndLogin.INPUT_EMAIL)
        input_password = driver.find_element(*LocatorsForRegistrationAndAndLogin.INPUT_PASSWORD)
        btn_login = driver.find_element(*LocatorsForRegistrationAndAndLogin.BTN_LOGIN)

        # Вводим логин и пароль, нажимаем Войти
        input_email.click()
        input_email.send_keys(self.get_user_info('email'))
        input_password.click()
        input_password.send_keys(self.get_user_info('password'))
        btn_login.click()

    def click_element(self, driver: WebDriver, locator=None):
        if locator:
            el = WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located(locator))
            el.click()
        return driver
