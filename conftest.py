import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    options = Options()
    service = Service(executable_path='./chromedriver.exe')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def test_user():
    """Данные уже тестового зарегестрированного пользователя (для входа)"""
    user = {
        "name": "Vladimir",
        "email": 'vladimir_nikolaev_5_619@ucxxj.com',
        "password": 'VgBXfSiaoSv4IaKl9m8m'
    }
    return user
