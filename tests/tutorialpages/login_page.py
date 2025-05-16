"""
Login Page Class for https://practicetestautomation.com/practice-test-login/
"""

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(
            username
        )  # Username element ID

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(
            password
        )  # Password element ID

    def click_login(self):
        self.driver.find_element(By.ID, "submit").click()  # Submit button ID

    def verify_successful_login(self):
        try:
            logout_button = self.driver.find_element(By.LINK_TEXT, "Log out")
            return logout_button.is_displayed()
        except NoSuchElementException:
            pytest.fail("Logout button does not exist.")
