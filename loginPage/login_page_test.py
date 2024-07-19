from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPageLocators.Login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        click_login_button.click()

# test
