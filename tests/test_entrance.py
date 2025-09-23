import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import *

class TestStellarBurgersLogin:
    USER_NAME = "31 Елизавета Сидельникова"
    USER_EMAIL = "lizaveta.alexeewa1999@ya.ru"
    USER_PASSWORD = "31Liza99"

    def test_login_main_page_button(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located((Locators.LOGOUT_BUTTON)))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        
        
        driver.find_element(*Locators.LOGO).click()

        wait.until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON_MAIN)))
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)

        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))

    def test_login_personal_account_button(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located((Locators.LOGOUT_BUTTON)))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        
        
        driver.find_element(*Locators.LOGO).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)

        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))

    def test_login_registration_form(self, driver):
        wait = WebDriverWait(driver, 5)


        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located((Locators.LOGOUT_BUTTON)))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        
        
        driver.find_element(*Locators.LOGO).click()

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        wait.until(EC.visibility_of_element_located((Locators.REGISTER_BUTTON))).click()

        wait.until(EC.visibility_of_element_located((Locators.REGISTRATION)))

        driver.find_element(By.LINK_TEXT, "Войти").click()

        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))

    def test_login_via_password_recovery_form(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located((Locators.LOGOUT_BUTTON)))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        
        
        driver.find_element(*Locators.LOGO).click()

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))

        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()

        wait.until(EC.visibility_of_element_located((Locators.RECOVERY_TEXT)))

        driver.find_element(*Locators.LOGIN_LINK_FROM_RECOVERY).click()

        wait.until(EC.visibility_of_element_located((Locators.ENTRANCE)))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))