from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import LocatorsMainPage


class PersonalAccount:
    def __init__(self, name, email, password):
        self.url = "https://stellarburgers.nomoreparties.site/account/profile"
        self.__name = name
        self.__email = email
        self.__password = password

    def get_user_info(self, key=None):
        data = {"name": self.__name, "email": self.__email, "password": self.__password}
        if key:
            return data[key]
        return {"name": self.__name, "email": self.__email, "password": self.__password}

    def click_element(self, driver: WebDriver):
        el = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.BTN_MY_ACNT))
        el.click()
        return driver
