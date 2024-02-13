import time

from pages.locators import LocatorsForRegistrationAndAndLogin, LocatorsMainPage, LocatorsPersonalAccounts
from pages.login_page import *
from pages.account_page import *
from selenium.webdriver.chrome.webdriver import WebDriver
from conftest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    def test_switch_to_personal_account(self, test_user, driver: WebDriver):
        login_page = LoginPage(**test_user)
        # Переходим на страницу входа
        driver.get(login_page.url)
        # Вводим необходимые данные в поля
        login_page.auth_user(driver)
        # Проверяем страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        assert "/login" not in driver.current_url

        personal_acnt = PersonalAccount(**login_page.get_user_info())
        personal_acnt.click_element(driver)

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsPersonalAccounts.BTN_PROFILE))
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsPersonalAccounts.BTN_ORDERS))
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsPersonalAccounts.BTN_LOGOUT))

        assert "/account/profile" in driver.current_url

        # Проверяем соответствие имени в профиле
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, f"//input[@value='{login_page.get_user_info('name')}']")))
        # Проверяем соответствие логина в профиле
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, f"//input[@value='{login_page.get_user_info('email')}']")))
