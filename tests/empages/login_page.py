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
        self.driver.find_element(By.XPATH, "//input[@id='Login_Email']").send_keys(
            username
        )  # Email element  XPATH from 'Page_EnergiaMONITOR/Login_Email_input'

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Login_Password']").send_keys(
            password
        )  # Password element from 'Page_EnergiaMONITOR/Login_Password_input'

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[@id='Login_Login']").click()  # Submit button ID 'Page_EnergiaMONITOR/Login_button'

    def verify_successful_login(self):
        try:
            logout_button = self.driver.find_element(By.LINK_TEXT, "Log out")
            return logout_button.is_displayed()
        except NoSuchElementException:
            pytest.fail("Logout button does not exist.")


# baseUrl https://em2-teszt.rubin.hu/
# user laczo.bettina+guiteszt@rubin.hu
# password Autom@t@t3st2k23
