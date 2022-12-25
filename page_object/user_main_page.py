import allure
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class UserMainPage(BasePage):

    ACCOUNT_BREADCRUMB = (By.XPATH, ".//a[text()='Account']")

    @allure.step("Проверить наличие хлебной крошки 'Account' после авторизации в ЛК")
    def check_open_user_main_page(self):
        self.find_element(self.ACCOUNT_BREADCRUMB)
