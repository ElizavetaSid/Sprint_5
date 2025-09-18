import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

class TestStellarBurgersConstructor:
    
    def test_constructor_section(self, driver):
        wait = WebDriverWait(driver, 10) 
        
        buns_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Булки']/..")))
        sauces_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Соусы']/..")))
        fillings_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Начинки']/..")))
        
        assert "tab_tab_type_current__2BEPc" in buns_section.get_attribute("class")
        
        sauces_section.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']")))
        assert "tab_tab_type_current__2BEPc" in sauces_section.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" not in buns_section.get_attribute("class")
        
        fillings_section.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']")))
        assert "tab_tab_type_current__2BEPc" in fillings_section.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" not in sauces_section.get_attribute("class")
    
        buns_section.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']")))
        assert "tab_tab_type_current__2BEPc" in buns_section.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" not in fillings_section.get_attribute("class")
