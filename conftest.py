import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import UserData
from locators import *


@pytest.fixture(scope='function')
def driver():
    options = Options()
    service = Service(executable_path='./chromedriver.exe')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    """Для авторизации"""
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LocatorsConstructor.BTN_LOGIN_IN_CONSTR))
    driver.find_element(*LocatorsConstructor.BTN_LOGIN_IN_CONSTR).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LocatorsForRegistrationAndLogin.BTN_LOGIN))
    driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_EMAIL).send_keys(UserData.EMAIL)
    driver.find_element(*LocatorsForRegistrationAndLogin.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
    driver.find_element(*LocatorsForRegistrationAndLogin.BTN_LOGIN).click()


@pytest.fixture
def registration(driver):
    # Переходим на страницу регистрации
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LocatorsConstructor.BTN_LOGIN_IN_CONSTR))
    driver.find_element(*LocatorsConstructor.BTN_LOGIN_IN_CONSTR).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LocatorsForRegistrationAndLogin.LINK_REGISTER))
    driver.find_element(*LocatorsForRegistrationAndLogin.LINK_REGISTER).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LocatorsForRegistrationAndLogin.BTN_REGISTER))
