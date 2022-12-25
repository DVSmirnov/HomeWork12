import allure
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class UserLogoutPage(BasePage):

    CONTINUE_BUTTON = (By.XPATH, ".//a[text()='Continue']")

    @allure.step("Кликнуть по кнопке 'Continue'")
    def click_continue_btn(self):
        self.find_element(self.CONTINUE_BUTTON).click()
