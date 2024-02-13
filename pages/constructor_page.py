from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConstructorPage:
    def __init__(self, driver: WebDriver = None):
        self.url = "https://stellarburgers.nomoreparties.site/"
        if driver:
            driver.get(self.url)

    def click_element(self, driver: WebDriver, locator):
        el = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        el.click()
        return driver
