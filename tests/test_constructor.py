import time

from pages.constructor_page import ConstructorPage
from pages.locators import LocatorsForRegistrationAndAndLogin, LocatorsMainPage, LocatorsConstructor
from pages.login_page import *
from pages.account_page import *
from selenium.webdriver.chrome.webdriver import WebDriver
from conftest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    @pytest.mark.parametrize('locator',
                             [LocatorsMainPage.LOGO_STELLAR_BURGERS,
                              LocatorsMainPage.BTN_CONSTRUCTOR])
    def test_switch_to_constructor(self, test_user, driver: WebDriver, locator):
        """Проверка перехода на страницу конструктора"""
        # Начальная страница для теста
        driver.get("https://stellarburgers.nomoreparties.site/login")
        constructor_page = ConstructorPage()
        # Переходы
        constructor_page.click_element(driver, locator)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsConstructor.H1_CREATE_BURGER))
        assert constructor_page.url == driver.current_url


    def test_swith_tab_in_constructor(self, driver: WebDriver):
        """Проверка переключения tab в конструкторе"""
        constructor_page = ConstructorPage(driver)
        constructor_page.click_element(driver, LocatorsConstructor.TAB_TEST)
        # Проверяем, что вкладка "current" в классе
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsConstructor.TAB_TEST_AFTER_CHOOSE))


