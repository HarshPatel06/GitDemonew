import pytest
from selenium import webdriver

from Config.config import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get(TestData.Base_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


