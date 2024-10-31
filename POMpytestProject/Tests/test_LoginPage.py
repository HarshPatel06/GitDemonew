import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):


    def test_page_title(self):
        self.LoginPage = LoginPage(driver=self.driver)
        title = self.LoginPage.get_title_of_LoginPage(TestData.Login_page_title)
        assert title == TestData.Login_page_title
        print("Page title verified successfully")
        print("Page title verified successfully2")
        print("Page title verified successfully3")
        print("Page title verified successfully4")
        print("Page title verified successfully5")


    def test_login(self):
        self.LoginPage = LoginPage(driver=self.driver)
        self.LoginPage.perform_Login(TestData.user_name, TestData.password)
        print("User logged in successfully into ENT portal")
        print("Home Page opened successfully")
        print("Home Page opened successfully 2")
        print("Home Page opened successfully 3")
