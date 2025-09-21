import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import *
class TestStellarBurgersLogOut:
    USER_EMAIL = "lizaveta.alexeewa1999@ya.ru"
    USER_PASSWORD = "31Liza99"
    
    def test_logout_from_personal_account(self, driver):
    
        wait = WebDriverWait(driver, 5)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)

        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located((Locators.PROFILE_SECTION)))
        
        logout_button = wait.until(EC.element_to_be_clickable((Locators.LOGOUT_BUTTON)))
        logout_button.click()
        wait.until(EC.visibility_of_element_located(Locators.ENTRANCE))
        
        assert driver.find_element(*Locators.ENTRANCE).is_displayed()
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()
