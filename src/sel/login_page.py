from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username = (By.XPATH, "//input[@id='Login_Email']")
    password = (By.XPATH, "//input[@id='Login_Password']")
    submit_button = (By.XPATH, "//button[@id='Login_Login']")
    # Ez nem jó
    error_message = (By.XPATH, "//*[@class='orangehrm-login-error']/div[1]/div[1]/p")

    def execute_login(self, username: str, password: str):
        log = self.get_logger()
        log.info("Enter Username - " + username)
        self.find(self.username).send_keys(username)
        log.info("Enter Password - " + password)
        self.find(self.password).send_keys(password)
        self.find(self.submit_button).click()

    def actual_error(self):
        # Ez még nem jó
        log = self.get_logger()
        actual_errormessage = self.find(self.error_message).text
        log.info("Actual Error Message - " + actual_errormessage)
        return actual_errormessage
