from selenium.webdriver.common.by import By
class Locators:
# Главная страница
    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") 
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
# Конструктор
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")  
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
# Форма регистрации
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input")  
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input")  
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]//input")  
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  
    PASSWORD_ERROR = (By.XPATH, "//div/p[@class='input__error text_type_main-default' and contains(text(), 'Некорректный пароль')]")


    EMAIL_INPUT_LOGIN = (By.XPATH, "//label[text()='Email']/following-sibling::input")  
    PASSWORD_INPUT_LOGIN = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  


    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  
    LOGIN_LINK_FROM_RECOVERY = (By.XPATH, "//a[text()='Войти']")  

    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']") 
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")