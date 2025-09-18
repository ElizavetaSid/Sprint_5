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

class TestStellarBurgersLogin:
    USER_EMAIL = "lizaveta.alexeewa1999@ya.ru"
    USER_PASSWORD = "31Liza99"

    def test_login_main_page_button(self, driver):
        wait = WebDriverWait(driver, 5)
        
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        
        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)
        
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    def test_login_personal_account_button(self, driver):
        wait = WebDriverWait(driver, 5)
        
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        
        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)
        
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    def test_login_registration_form(self, driver):
        wait = WebDriverWait(driver, 5)
        
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
        
        driver.find_element(By.LINK_TEXT, "Войти").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    def test_login_via_password_recovery_form(self, driver):
        wait = WebDriverWait(driver, 5)
        
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Восстановление пароля']")))
        
        driver.find_element(By.LINK_TEXT, "Войти").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        email_input.send_keys(self.USER_EMAIL)
        password_input.send_keys(self.USER_PASSWORD)

        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

