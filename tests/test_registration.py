from conftest import *
from data import *
from locators import *


class TestRegistration:

    def test_registration_new_user_success(self, driver, registration):
        # Вводим необходимые данные нового пользователя
        new_user = RandomUserData()
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_NAME).send_keys(new_user.name)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(new_user.email)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(new_user.good_password)
        driver.find_element(*LocatorsForRegistrationAndLogin.BTN_REGISTER).click()

        # Проверяем страницу, что выкинуло на форму авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForRegistrationAndLogin.BTN_LOGIN))
        assert '/login' in driver.current_url

        # Авторизация с новым пользователем
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsForRegistrationAndLogin.BTN_LOGIN).click()

        # Проверяем страницу после входа на наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        assert "/login" not in driver.current_url

    def test_registration_check_not_valid_password(self, driver, registration):
        # Вводим необходимые данные нового пользователя
        new_user = RandomUserData()
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_NAME).send_keys(new_user.name)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(new_user.email)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(new_user.bad_password)
        driver.find_element(*LocatorsForRegistrationAndLogin.BTN_REGISTER).click()
        # Проверяем наличие предупреждения о пароле
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LocatorsForRegistrationAndLogin.LABEL_INCORRECT_PASS))
