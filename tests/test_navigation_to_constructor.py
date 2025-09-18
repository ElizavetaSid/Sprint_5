import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import *

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

class TestStellarBurgersNavigation:
        
    def test_switching_to_constructor_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
 
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located((Locators.MAIN_PAGE_TITLE)))

    def test_switching_to_constructor_from_order_feed(self, driver):
        wait = WebDriverWait(driver, 15)
        
        driver.find_element(*Locators.ORDER_FEED_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Лента заказов']")))
        
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located((Locators.MAIN_PAGE_TITLE)))

    def test_switching_logo_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()= 'Вход']" )))
        
        driver.find_element(*Locators.LOGO).click()
        assert wait.until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON_MAIN)))

    def test_redirect_via_logo_from_order_feed(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.find_element(*Locators.ORDER_FEED_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Лента заказов']")))
        
        driver.find_element(*Locators.LOGO).click()
        assert wait.until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON_MAIN)))