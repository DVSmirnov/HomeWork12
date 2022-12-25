import allure
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminMainPage(BasePage):
    CATALOG_MENU_BTN = (By.ID, 'menu-catalog')
    PRODUCTS_MENU_BTN = (By.XPATH, ".//li/ul/li/a[text()='Products']")

    @allure.step('Проверить открытие главной страницы админки')
    def check_open_admin_main_page(self):
        self.find_element(self.CATALOG_MENU_BTN)

    @allure.step('Кликнуть по кнопке "Catalog"')
    def click_catalog_menu_btn(self):
        self.find_element(self.CATALOG_MENU_BTN).click()

    @allure.step('Кликнуть по кнопке "Products"')
    def click_products_menu_btn(self):
        self.find_element(self.PRODUCTS_MENU_BTN).click()
