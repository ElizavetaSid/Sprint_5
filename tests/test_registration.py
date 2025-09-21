import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from helpers import *
class TestStellarBurgersRegistration:

    def test_successful_registration(self, go_to_registration_page: WebDriverWait, helper):
        wait = go_to_registration_page

        name = "Лиза Иванова"
        email = helper.generate_email()
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

    @pytest.mark.parametrize("invalid_email", [
    "invalidemail",
    "invalid@",
    "@domain.com",
    "invalid@domain",
    "invalid@domain."
])
    def test_registration_with_invalid_email(self, invalid_email, go_to_registration_page: WebDriverWait):
        wait = go_to_registration_page
        name = "Лиза Иванова"
        password = "123456"

        wait.until(EC.element_to_be_clickable(Locators.NAME_INPUT)).clear()
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).clear()
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).clear()

        wait.until(EC.element_to_be_clickable(Locators.NAME_INPUT)).send_keys(name)
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(invalid_email)
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(password)
    
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

        assert "register" in wait._driver.current_url
        assert wait._driver.find_element(*Locators.REGISTER_BUTTON).is_displayed()

    def test_registration_with_short_password(self, go_to_registration_page: WebDriverWait, helper: Helpers):
        wait = go_to_registration_page

        name = "Лиза Иванова"
        email = helper.generate_email()
        short_password = "567"

        wait.until(EC.element_to_be_clickable(Locators.NAME_INPUT)).send_keys(name)
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(short_password)
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

        assert wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))


    def test_registration_with_existing_email(self, go_to_registration_page: WebDriverWait, helper: Helpers):
        wait = go_to_registration_page

        name = "Лиза Иванова"
        email = helper.generate_email()
        password = "123456"

        wait.until(EC.element_to_be_clickable(Locators.NAME_INPUT)).send_keys(name)
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

        time.sleep(3)

        wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT)).send_keys("Другой Пользователь")
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT)).send_keys(password)

        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

        assert "register" in wait._driver.current_url
        assert wait._driver.find_element(*Locators.REGISTER_BUTTON).is_displayed()