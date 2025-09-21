import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from tests.locators import *


class TestStellarBurgersNavigation:
        
    def test_switching_to_constructor_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
 
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located((Locators.MAIN_PAGE_TITLE)))

    def test_switching_to_constructor_from_order_feed(self, driver):
        wait = WebDriverWait(driver, 15)
        
        driver.find_element(*Locators.ORDER_FEED_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((Locators.ORDER_FEED_BUTTON)))
        
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located((Locators.MAIN_PAGE_TITLE)))

    def test_switching_logo_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))
        
        driver.find_element(*Locators.LOGO).click()
        assert wait.until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON_MAIN)))

    def test_redirect_via_logo_from_order_feed(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.find_element(*Locators.ORDER_FEED_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located((Locators.ORDER_FEED_BUTTON)))
        
        driver.find_element(*Locators.LOGO).click()
        assert wait.until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON_MAIN)))