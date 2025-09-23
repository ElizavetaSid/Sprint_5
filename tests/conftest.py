import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import *

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features-AutomationControlled")
    driver = webdriver.Chrome(
        options=options
    )
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def go_to_registration_page(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)).click()
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
    return wait

@pytest.fixture(scope="function")
def helper():
    return Helpers()
