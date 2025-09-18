import pytest
import random
import time
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

class TestStellarBurgersRegistration:
    
    def generate_email(self):
        random_number = random.randint(100, 999)
        return f"liza_ivanova_10_{random_number}@yandex.ru"

    def go_to_registration_page(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
        return wait

    def test_successful_registration(self, driver):
        wait = self.go_to_registration_page(driver)
        
        name = "Лиза Иванова"
        email = self.generate_email()
        password = "123456"
        
        name_input = wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)
        
        email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        
        assert wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        

    def test_registration_with_empty_name(self, driver):
        wait = self.go_to_registration_page(driver)
        
        email = self.generate_email()
        password = "123456"
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        

    def test_registration_with_invalid_email(self, driver):
        wait = self.go_to_registration_page(driver)
        
        name = "Лиза Иванова"
        invalid_emails = [
            "invalidemail",
            "invalid@",
            "@domain.com",
            "invalid@domain",
            "invalid@domain."
        ]
        
        for invalid_email in invalid_emails:
            driver.find_element(*Locators.NAME_INPUT).clear()
            driver.find_element(*Locators.EMAIL_INPUT).clear()
            driver.find_element(*Locators.PASSWORD_INPUT).clear()
            
            driver.find_element(*Locators.NAME_INPUT).send_keys(name)
            driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_email)
            driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
            driver.find_element(*Locators.REGISTER_BUTTON).click()
            
            assert "register" in driver.current_url
            assert driver.find_element(*Locators.REGISTER_BUTTON).is_displayed()

    def test_registration_with_short_password(self, driver):
        wait = self.go_to_registration_page(driver)
        
        name = "Лиза Иванова"
        email = self.generate_email()
        short_password = "567"
          
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
            
        assert wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
            
    
    def test_registration_with_existing_email(self, driver):
        wait = self.go_to_registration_page(driver)
        
        name = "Лиза Иванова"
        email = self.generate_email()
        password = "123456"
        
        wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT)).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        time.sleep(3)

        wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT)).send_keys("Другой Пользователь")
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT)).send_keys(password)
        
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        
        assert "register" in driver.current_url
        assert driver.find_element(*Locators.REGISTER_BUTTON).is_displayed()