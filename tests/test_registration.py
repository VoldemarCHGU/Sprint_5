from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

        # Ожидаю кнопку входы, чтобы войти с новым пользователем
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LocatorsForRegistrationAndLogin.BTN_LOGIN))
        # Авторизация с новым пользователем
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsForRegistrationAndLogin.BTN_LOGIN).click()

        # Проверяем, что с новыми данными вход успешный => регистрация удалась (поиск наличия кнопки "Оформить заказ")
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))

    def test_registration_check_not_valid_password(self, driver, registration):
        # Вводим необходимые данные нового пользователя
        new_user = RandomUserData()
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_NAME).send_keys(new_user.name)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(new_user.email)
        driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(new_user.bad_password)
        driver.find_element(*LocatorsForRegistrationAndLogin.BTN_REGISTER).click()
        # Проверяем наличие предупреждения о пароле
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LocatorsForRegistrationAndLogin.LABEL_INCORRECT_PASS))
