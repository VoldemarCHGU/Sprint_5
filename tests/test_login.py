from conftest import *
from locators import *


class TestLogin:
    @pytest.mark.parametrize('start_url, locator', [
        ("https://stellarburgers.nomoreparties.site/", LocatorsConstructor.BTN_LOGIN_IN_CONSTR),
        ("https://stellarburgers.nomoreparties.site/login", LocatorsForRegistrationAndLogin.INPUT_EMAIL),
        ("https://stellarburgers.nomoreparties.site/register", LocatorsForRegistrationAndLogin.BTN_LOGIN_IN_REG_PAGE),
        ("https://stellarburgers.nomoreparties.site/forgot-password",
         LocatorsForgotPassword.BTN_LOGIN_IN_PAGE_FORGOT_PASS)
    ])
    def test_successful_login(self, driver, start_url, locator):
        driver.get(start_url)
        # Переходим на страницу входа
        driver.find_element(*locator).click()
        # Вводим необходимые данные в поля
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsForRegistrationAndLogin.BTN_LOGIN).click()
        # Проверяем страницу
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        assert "/login" not in driver.current_url
