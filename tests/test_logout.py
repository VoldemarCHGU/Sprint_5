from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import *


class TestLogout:

    def test_logout(self, driver, login):
        # Переходим в личный кабинет
        driver.find_element(*LocatorsMainPage.BTN_MY_ACNT).click()
        # Ждём кнопку выхода и жмём на неё
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsPersonalAccounts.BTN_LOGOUT))
        driver.find_element(*LocatorsPersonalAccounts.BTN_LOGOUT).click()
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LocatorsForRegistrationAndLogin.BTN_LOGIN))
