import allure

from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOGO_BUTTON = (By.XPATH, './/img[@class="img-responsive"]/..')
    CART_BUTTON = (By.XPATH, './/li/a[@title="Shopping Cart"]')
    CURRENCY = (By.CSS_SELECTOR, '.fa.fa-caret-down')
    CURRENCY_VALUE = (By.XPATH, './/button[@class="btn btn-link dropdown-toggle"]/strong')
    EURO = (By.NAME, "EUR")
    POUND_STERLING = (By.NAME, "GBP")
    US_DOLLAR = (By.NAME, "USD")
    SEARCH_INPUT = (By.NAME, "search")

    MY_ACCOUNT_HEADER_BTN = (By.CSS_SELECTOR, r"a[title='My Account']")
    REGISTER_HEADER_BTN = (By.XPATH, r"//a[normalize-space()='Register']")
    LOGIN_HEADER_BTN = (By.XPATH, r"//a[normalize-space()='Login']")
    LOGOUT_HEADER_BTN = (By.XPATH, ".//li/a[text()='Logout']")

    PRODUCT_ITEM = (By.XPATH, './/div[@class="product-thumb transition"]')
    PRODUCT_NAME = (By.XPATH, './/div[@class="caption"]/h4/a')
    ADD_TO_CART_BTN_BY_NAME = (By.XPATH, './/h4/a[text()="{0}"]/../../../div[@class="button-group"]/button[1]')

    @allure.step("Кликнуть по лого сайта")
    def click_logo_btn(self):
        self.find_element(self.LOGO_BUTTON).click()

    @allure.step("Кликнуть по кнопке корзины")
    def click_cart_btn(self):
        self.find_element(self.CART_BUTTON).click()

    @allure.step("Кликнуть по выпадающему списку 'My Account'")
    def click_my_account_btn(self):
        self.find_element(self.MY_ACCOUNT_HEADER_BTN).click()

    @allure.step("Кликнуть по значению {value} в выпадающем списке 'My Account'")
    def click_value_in_my_account_dropdown(self, value):
        if value == "Register":
            self.find_element(self.REGISTER_HEADER_BTN).click()
        elif value == "Login":
            self.find_element(self.LOGIN_HEADER_BTN).click()
        elif value == 'Logout':
            self.find_element(self.LOGOUT_HEADER_BTN).click()
        else:
            raise ValueError(f"В выпадающем списке 'My Account' нет значения '{value}'")

    @allure.step("Кликнуть по выпадающему списку 'Currency'")
    def click_currency_btn(self):
        self.find_element(self.CURRENCY).click()

    @allure.step("Кликнуть по значению {currency_name} в выпадающем списке 'Currency'")
    def click_currency_by_name(self, currency_name):
        try:
            if currency_name == 'EUR':
                self.find_element(self.EURO).click()
            elif currency_name == 'GBP':
                self.find_element(self.POUND_STERLING).click()
            elif currency_name == 'USD':
                self.find_element(self.US_DOLLAR).click()
        except ValueError:
            raise f'Валюта "{currency_name}" не поддерживается данным сайтом.'

    @allure.step("Проверить активное значение валюты'")
    def check_currency_value(self, currency_name):
        actual_currency_value = self.find_element(self.CURRENCY_VALUE).text
        if currency_name == 'EUR':
            assert actual_currency_value == '€', f'Значение валюты "{actual_currency_value}" не соответствует ' \
                                                 f'ожидаемому "€"'
        elif currency_name == 'USD':
            assert actual_currency_value == '$', f'Значение валюты "{actual_currency_value}" не соответствует ' \
                                                 f'ожидаемому "$"'
        elif currency_name == 'GBP':
            assert actual_currency_value == '£', f'Значение валюты "{actual_currency_value}" не соответствует ' \
                                                 f'ожидаемому "£"'

    @allure.step("Проверить открытие главной страницы")
    def check_open_main_page(self):
        self.find_element(self.SEARCH_INPUT, timeout=15)

    @allure.step("Получить список товаров на странице")
    def get_product_list(self):
        lst = []
        items = self.find_elements(self.PRODUCT_ITEM)
        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text
            lst.append(name)
        return lst

    @allure.step("Кликнуть по кнопке добавления в корзину у товара {name}")
    def click_add_btn_by_product_name(self, name):
        s, l = self.ADD_TO_CART_BTN_BY_NAME
        self.find_element((s, l.format(name))).click()
