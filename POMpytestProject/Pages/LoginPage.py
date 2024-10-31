from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    """These are the locators"""
    USERNAME = (By.XPATH, '//*[@id="Username"]')
    PASSWORD = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="loginbtn"]')
    CONTINUE_BTN = (By.XPATH, '//input[@name="button"]')

    """Constructor of LoginPage class"""
    def __init__(self, driver):
        super().__init__(driver)


    """----PAGE ACTIONS----"""
    """This function is used to get the title of page"""
    def get_title_of_LoginPage(self, title):
        return self.get_element_title(title)


    """This is used to login to the application."""
    def perform_Login(self, username, password):
        self.perform_sendKeys(self.USERNAME, username)
        self.perform_sendKeys(self.PASSWORD, password)
        self.perform_click(self.LOGIN_BTN)
        self.perform_click(self.CONTINUE_BTN)

