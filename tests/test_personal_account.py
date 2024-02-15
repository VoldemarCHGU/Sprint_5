from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestPersonalAccount:
    def test_switch_to_personal_account(self, driver, login):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsMainPage.BTN_MAKE_ORDER))
        assert "/login" not in driver.current_url
        driver.find_element(*LocatorsMainPage.BTN_MY_ACNT).click()
        # Проверки страницы профиля
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsPersonalAccounts.BTN_PROFILE))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsPersonalAccounts.BTN_ORDERS))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsPersonalAccounts.BTN_LOGOUT))
        assert "/account/profile" in driver.current_url

        # Проверяем соответствие имени в профиле
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsPersonalAccounts.USER_NAME))
        # Проверяем соответствие логина в профиле
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsPersonalAccounts.USER_LOGIN))
