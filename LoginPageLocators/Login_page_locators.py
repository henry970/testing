from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
