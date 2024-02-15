from conftest import *
from data import Main


class TestConstructor:
    @pytest.mark.parametrize('locator', [LocatorsMainPage.LOGO_STELLAR_BURGERS,
                                         LocatorsMainPage.BTN_CONSTRUCTOR])
    def test_switch_to_constructor(self, driver, locator):
        """Проверка перехода на страницу конструктора"""
        driver.find_element(*locator).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsConstructor.H1_CREATE_BURGER))
        assert Main.URL == driver.current_url

    def test_swith_tab_in_constructor(self, driver):
        """Проверка переключения tab в конструкторе"""
        driver.find_element(*LocatorsConstructor.TAB_TEST).click()
        # Проверяем, что вкладка "current" в классе
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsConstructor.TAB_TEST_AFTER_CHOOSE))
