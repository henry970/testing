import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    username_field = driver.find_element(By.NAME, "user-name")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauc")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3'))
    ).text

    assert "Invalid credentials" in error_message, "Username and password do not match any user in this service."

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    username_field = driver.find_element(By.NAME, "user-name")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(5)  # Adjust the sleep time if necessary

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
