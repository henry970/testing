from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPageLocators.Login_page_locators import NegativeLoginPageLocators


class LoginPage1:
    def __init__(self, driver):
        self.driver = driver

    def login_urls(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.USERNAME_))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.PASSWORD_))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.LOGIN_BUTTON_))
        click_login_button.click()

    def get_error_message_element(self):
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#login_button_container > div > form > '
                                                             'div.error-message-container.error > h3'))
        )

        return error_message_element
