import allure

from page_object.base_page import BasePage
from selenium.webdriver.common.by import By

import time


class LoginPage(BasePage):
    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSCONFIRM = (By.ID, 'input-confirm')
    PRIVACYPOL = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    CONTINUE1 = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')
    CONTINUE2 = (By.CSS_SELECTOR, '#content > div > div > a')
    LOGOUT = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')
    LOGIN_BTN = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')

    @allure.step("Авторизация пользователем с email {email} и паролем {password}")
    def login_to_account(self, email, password):
        self._input(self.EMAIL, email)
        self._input(self.PASSWORD, password)
        self.find_element(self.LOGIN_BTN).click()
        time.sleep(5)
