from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from web.pages.base import BasePage


class LoginPage(BasePage):

    email: str
    password: str

    def __init__(self, driver: WebDriver, email: str, password: str):
        super().__init__(driver)
        self.email = email
        self.password = password

    @property
    def path(self) -> str:
        return "login"

    def email_input_locator(self):
        return By.XPATH, "//input[@name='email']"

    def password_input_locator(self):
        return By.XPATH, "//input[@name='password']"

    def submit_button_locator(self):
        return By.XPATH, "//button[@type='submit']"

    def login(self) -> None:
        self.wait_for_element(self.email_input_locator()).send_keys(self.email)
        sleep(2)
        self.wait_for_element(self.password_input_locator()).send_keys(self.password)
        sleep(2)
        self.wait_for_element(self.submit_button_locator()).click()
        sleep(2)

        # Sleeping added to not trigger a captcha

        if self.get_current_url() == "https://discord.com/channels/@me":
            raise Exception("Login failed")
