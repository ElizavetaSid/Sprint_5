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

class TestStellarBurgersLogOut:
    @pytest.fixture(scope="function", autouse=True)
    def login(self, driver):
        """Фикстура для предварительной авторизации пользователя"""
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input")))
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        
        email_input.send_keys("lizaveta.alexeewa1999@ya.ru") 
        password_input.send_keys("31Liza99")  
    
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        yield

    def test_logout_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']")))
        logout_button.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        
        assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed()
        assert driver.find_element(By.XPATH, "//button[text()='Войти']").is_displayed()
        
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed()
