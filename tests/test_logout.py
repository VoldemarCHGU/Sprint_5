from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import LocatorsForRegistrationAndAndLogin, LocatorsMainPage, LocatorsPersonalAccounts
from pages.login_page import LoginPage


class TestLogout:

    def test_logout(self, test_user, driver: WebDriver):
        login_page = LoginPage(**test_user, driver=driver)
        # Переходим на страницу входа
        # Вводим необходимые данные в поля
        login_page.auth_user(driver)
        # Проверяем страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        login_page.click_element(driver, LocatorsMainPage.BTN_MY_ACNT)
        login_page.click_element(driver, LocatorsPersonalAccounts.BTN_LOGOUT)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsForRegistrationAndAndLogin.BTN_LOGIN))
        assert "/login" in driver.current_url
