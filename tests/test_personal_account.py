import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from tests.locators import *

class TestStellarBurgersPersonalAccount:

    def test_redirect_to_personal_account_unauthorized(self, driver):
        wait = WebDriverWait(driver, 5)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))
        
        assert driver.find_element(*Locators.EMAIL_INPUT_LOGIN).is_displayed()
        assert driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).is_displayed()
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()
        
    def test_redirect_to_personal_account_authorized(self, driver):
        wait = WebDriverWait(driver, 5)
        
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        email_input = wait.until(EC.visibility_of_element_located((Locators.EMAIL_INPUT_LOGIN)))
        password_input = driver.find_element(*Locators.PASSWORD_INPUT_LOGIN)
        
        email_input.send_keys("lizaveta.alexeewa1999@ya.ru")  
        password_input.send_keys("31Liza99") 
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located((Locators.PROFILE_SECTION)))
        
        assert driver.find_element(*Locators.PROFILE_SECTION).is_displayed()
        assert driver.find_element(*Locators.ORDER_HISTORY).is_displayed()
        assert driver.find_element(*Locators.LOGOUT_BUTTON).is_displayed()
        