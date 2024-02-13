from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *
from pages.locators import *
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage


class TestRegistration:

    def test_registration_new_user_pass(self, driver: WebDriver):
        reg_page = RegisterPage()
        # Переходим на страницу Регистрации
        driver.get(reg_page.url)
        # Вводим необходимые данные в поля
        reg_page.registration_uesr(driver)
        # Проверяем страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsForRegistrationAndAndLogin.BTN_LOGIN))
        assert '/login' in driver.current_url

        # Перед авторизацией настраиваем данные нового пользователя
        login_page = LoginPage(**reg_page.get_user_info())
        # Пробуем авторизоваться с новым пользователем
        login_page.auth_user(driver)

        # Проверяем страницу после входа на наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        assert "/login" not in driver.current_url

    @pytest.mark.parametrize("password, exception", [('test5', True), ('tests6', False)])
    def test_registration_check_not_valid_password(self, driver: WebDriver, password, exception):
        reg_page = RegisterPage()
        # Переходим на страницу Регистрации
        driver.get(reg_page.url)
        reg_page.set_new_pass(password)
        # Вводим необходимые данные в поля
        reg_page.registration_uesr(driver)
        # Проверяем наличие предупреждения о пароле
        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located(
                    LocatorsForRegistrationAndAndLogin.LABEL_INCORRECT_PASS))
            assert True if exception else False
        except:
            assert False if exception else True
