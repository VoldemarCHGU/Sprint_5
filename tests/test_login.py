from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *
from pages.locators import LocatorsForRegistrationAndAndLogin, LocatorsMainPage, LocatorsForgotPassword, \
    LocatorsConstructor
from pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.parametrize('start_url, locator', [
        ("https://stellarburgers.nomoreparties.site/", LocatorsConstructor.BTN_LOGIN_IN_CONSTR),
        ("https://stellarburgers.nomoreparties.site/login", None),
        ("https://stellarburgers.nomoreparties.site/register", LocatorsForRegistrationAndAndLogin.BTN_LOGIN_IN_REG_PAGE),
        ("https://stellarburgers.nomoreparties.site/forgot-password", LocatorsForgotPassword.BTN_LOGIN_IN_PAGE_FORGOT_PASS)
    ])
    def test_successful_login(self, test_user, driver: WebDriver, start_url, locator):
        driver.get(start_url)

        login_page = LoginPage(**test_user)
        # Переходим на страницу входа
        login_page.click_element(driver, locator)
        # Вводим необходимые данные в поля
        login_page.auth_user(driver)
        # Проверяем страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        assert "/login" not in driver.current_url
