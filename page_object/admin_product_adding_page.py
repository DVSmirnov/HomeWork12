import allure

from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminProductAddingPage(BasePage):
    PAGE_TITLE = (By.XPATH, ".//h3[@class='panel-title' and text()=' Add Product']")
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    DESCRIPTION = (By.CLASS_NAME, "note-editable")
    BUTTON_SAVE = (By.CSS_SELECTOR, ".fa.fa-save")
    TAB_DATA = (By.XPATH, ".//*[@class='nav nav-tabs']/li/a[text()='Data']")
    MODEL = (By.ID, "input-model")

    @allure.step('Проверить открытие страницы добавления товара')
    def check_open_admin_product_adding_page(self):
        self.find_element(self.PAGE_TITLE)

    @allure.step('Ввести данные в текстовые поля')
    def enter_values_into_text_fields(self, product_name, meta_tag_title, description, model):
        self._input(self.PRODUCT_NAME, product_name)
        self._input(self.META_TAG_TITLE, meta_tag_title)
        self._input(self.DESCRIPTION, description)
        self.find_element(self.TAB_DATA).click()
        self._input(self.MODEL, model)

    @allure.step('Кликнуть по кнопке сохранения')
    def click_save_btn(self):
        self.find_element(self.BUTTON_SAVE).click()
