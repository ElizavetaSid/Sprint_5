import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import *


class Helpers:
    def generate_email(self):
        random_number = random.randint(100, 999)
        return f"liza_ivanova_10_{random_number}@yandex.ru"
