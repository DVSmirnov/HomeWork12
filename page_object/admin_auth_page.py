import allure

from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminAuthPage(BasePage):
    LOGIN_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    _path = "/admin"

    @allure.step('Авторизация в админке с логином {username} и паролем {password}')
    def login_to_account(self, username, password):
        self._input(self.LOGIN_INPUT, username)
        self._input(self.PASSWORD_INPUT, password)
        self.find_element(self.LOGIN_BUTTON).click()

    @allure.step('Проверить открытие страницы авторизации в админку')
    def check_open_admin_login_page(self):
        self.find_element(self.LOGIN_BUTTON)
