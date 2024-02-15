from selenium.webdriver.common.by import By

from data import UserData


class LocatorsForRegistrationAndLogin:
    INPUT_NAME = By.XPATH, "//input[@name='name']"  # поле вводи имени
    INPUT_EMAIL = By.XPATH, "//*[@id='root']//label[text()='Email']/following-sibling::input"  # Поле ввода email
    INPUT_PASSWORD = By.XPATH, "//*[@id='root']//label[text()='Пароль']/following-sibling::input"  # поле ввода пароля
    BTN_REGISTER = By.XPATH, "//button[contains(text(),'Зарегистрироваться')]"  # Кнопка "Зарегистрироваться"
    LINK_REGISTER = By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"  # ссылка на страницу регистрации
    BTN_LOGIN = By.XPATH, "//button[contains(text(),'Войти')]"  # Кнопка "Войти"
    LABEL_INCORRECT_PASS = By.XPATH, "//div[contains(@class,'password')]/following-sibling::p[contains(text(), 'Некорректный пароль')]"
    BTN_LOGIN_IN_REG_PAGE = By.XPATH, "//a[contains(text(),'Войти')]"


class LocatorsForgotPassword:
    BTN_LOGIN_IN_PAGE_FORGOT_PASS = By.XPATH, "//a[contains(text(),'Войти')]"


class LocatorsMainPage:
    BTN_MAKE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    BTN_MY_ACNT = By.XPATH, "//p[text()='Личный Кабинет']"
    LOGO_STELLAR_BURGERS = By.XPATH, "//div[contains(@class,'logo')]"
    BTN_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"


class LocatorsPersonalAccounts:
    BTN_SAVE = By.XPATH, "//button[contains(text(),'Сохранить')]"
    BTN_LOGOUT = By.XPATH, "//button[contains(text(),'Выход')]"
    BTN_PROFILE = By.XPATH, "//a[contains(text(),'Профиль')]"
    BTN_ORDERS = By.XPATH, "//a[contains(text(),'История заказов')]"
    BTN_CANCEL = By.XPATH, "//button[contains(text(),'Отмена')]"
    USER_NAME = By.XPATH, f"//input[@value='{UserData.NAME}']"
    USER_LOGIN = By.XPATH, f"//input[@value='{UserData.EMAIL}']"


class LocatorsConstructor:
    H1_CREATE_BURGER = By.XPATH, "//section/h1[contains(text(), 'Соберите бургер')]"
    BTN_CREATE_ORDER = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    BTN_LOGIN_IN_CONSTR = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"
    TAB_TEST = By.XPATH, "//section//span[contains(text(),'Соусы')]"
    TAB_TEST_AFTER_CHOOSE = By.XPATH, "//div[contains(@class,'current')]/span[contains(text(),'Соусы')]"
