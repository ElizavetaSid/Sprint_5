import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import *

class TestStellarBurgersConstructor:
    
    def test_switch_to_sauces(self, driver):
        wait = WebDriverWait(driver, 10)

        sauces_tab = wait.until(EC.visibility_of_element_located((Locators.SAUCES_SECTION)))
        driver.find_element(*Locators.SAUCES_SECTION).click()
    
        assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class")
    

    def test_switch_to_toppings(self, driver):
        wait = WebDriverWait(driver, 10)

        toppings_tab = wait.until(EC.visibility_of_element_located((Locators.FILLINGS_SECTION)))
        toppings_tab.click()
    
        assert "tab_tab_type_current__2BEPc" in toppings_tab.get_attribute("class")
        assert wait.until(EC.visibility_of_element_located((Locators.FILLINGS_SECTION)))

    def test_switch_to_buns(self, driver):
        wait = WebDriverWait(driver, 10)

        sauces_tab = wait.until(EC.visibility_of_element_located((Locators.SAUCES_SECTION)))
        sauces_tab.click()
    
        buns_tab = wait.until(EC.visibility_of_element_located((Locators.BUNS_SECTION)))
        buns_tab.click()
    
    
        assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class")
        assert wait.until(EC.visibility_of_element_located((Locators.BUNS_SECTION)))