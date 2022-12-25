import random

import allure

from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminProductsPage(BasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, ".table tbody input")
    DEL_BUTTON = (By.CSS_SELECTOR, ".fa.fa-trash-o")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    @allure.step("Проверить открытие страницы 'Products'")
    def check_open_admin_products_page(self):
        self.find_element(self.ADD_BUTTON)

    @allure.step("Кликнуть по кнопке добавления товара")
    def click_add_product_btn(self):
        self.find_element(self.ADD_BUTTON).click()

    @allure.step('Проверить отображение сообщения после успешного добавления товара')
    def check_success_alert(self):
        self.find_element(self.SUCCESS_ALERT)

    @allure.step('Кликнуть по рандомному чекбоксу товара')
    def click_random_product_checkbox(self):
        random.choice(self.find_elements(self.PRODUCT_CHECKBOX)).click()

    @allure.step('Кликнуть по кнопке удаления товара')
    def click_delete_btn(self):
        self.find_element(self.DEL_BUTTON).click()
