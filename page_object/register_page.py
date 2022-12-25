import allure

from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSCONFIRM = (By.ID, 'input-confirm')
    PRIVACYPOL = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    CONTINUE1 = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')

    @allure.step("Ввод регистрационных данных")
    def register_new_account(self, first_name, last_name, email, telephone, password, confirm_pass):
        self._input(self.FIRSTNAME, first_name)
        self._input(self.LASTNAME, last_name)
        self._input(self.EMAIL, email)
        self._input(self.TELEPHONE, telephone)
        self._input(self.PASSWORD, password)
        self._input(self.PASSCONFIRM, confirm_pass)
        self.find_element(self.PRIVACYPOL).click()
        self.find_element(self.CONTINUE1).click()
