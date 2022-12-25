import allure
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class SuccessPage(BasePage):
    SUCCESS_MESSAGE = (By.XPATH, ".//h1[text()='Your Account Has Been Created!']")
    CONTINUE_BUTTON = (By.XPATH, ".//a[text()='Continue']")

    @allure.step("Проверить наличие заголовка 'Your Account Has Been Created!' после регистрации")
    def check_open_success_page(self):
        self.find_element(self.SUCCESS_MESSAGE)

    @allure.step("Кликнуть по кнопке 'Continue'")
    def click_continue_button(self):
        self.find_element(self.CONTINUE_BUTTON).click()
