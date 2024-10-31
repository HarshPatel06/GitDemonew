from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
This is the superclass of all pages.
It contains all the generic methods and other utilities.
"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def perform_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).click()

    def perform_sendKeys(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_title(self, title):
        WebDriverWait(self.driver, 5).until(ec.title_is(title))
        print(self.driver.title)
        return self.driver.title
