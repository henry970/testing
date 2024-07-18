import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from loginPage.login_page_test import NegativeLoginPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(scope="module")
# def driver_setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = NegativeLoginPage(driver)
    login_page.login_url("https://www.saucedemo.com")
    return login_page


def negative_test_login_page_on_sauce_demo_website(login):
    login.enter_username("performance_glitch_user")
    login.enter_password("secret_sauce")
    login.click_login_button()

#
# # positive
#
# @pytest.fixture(scope="module")
# def driver_setup1():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope="module")
# def login(driver_setup):
#     driver = driver_setup
#     login_page = NegativeLoginPage(driver)
#     login_page.login_url("https://www.saucedemo.com")
#     return login_page
#
#
# def test_login_page_on_sauce_demo_website(login):
#     login.enter_username("performance_glitch_user")
#     login.enter_password("secret_sauce")
#     login.click_login_button()
