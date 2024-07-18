from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPageLocators.Login_page_locators import LoginPageLocators


class NegativeLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.USERNAME)
        )
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD)
        )
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        click_login_button.click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3'))
        )

        # Verify the error message
        error_message = error_message_element.text
        assert "Invalid credentials" in error_message, "Username and password do not match any user in this service."

        print("Negative test passed: Username and password do not match any user in this service.")
