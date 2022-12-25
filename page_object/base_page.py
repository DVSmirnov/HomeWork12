import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {path}')
    def open(self, path=''):
        try:
            self.driver.logger.info("Opening url: {}".format(self.driver.base_url + path))
            self.driver.get(self.driver.base_url + path)
        except Exception:
            self.driver.logger.error(f'Error during opening url {self.driver.base_url + path}')
            allure.attach(self.driver.get_screenshot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Страница {self.driver.base_url + path} не открывается"

    @allure.step('Ввести значение {value} в локатор {locator}')
    def _input(self, locator, value):
        try:
            self.driver.logger.info("Input {} in input {}".format(value, locator))
            web_element = self.find_element(locator=locator)
            web_element.click()
            web_element.clear()
            web_element.send_keys(value)
        except Exception:
            self.driver.logger.error(f'Error during entering {value} in {locator}')
            allure.attach(self.driver.get_screenshot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Не удалось ввести значение {value} в локатор {locator}"

    @allure.step('Проверка наличия локатора {locator}')
    def find_element(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.driver.logger.error(f'Error during finding element with locator {locator}')
            allure.attach(self.driver.get_screenshot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Ожидание локатора {locator} заняло слишком много времени"

    @allure.step('Найти все элементы с локатором {locator}')
    def find_elements(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.driver.logger.error(f'Error during finding elements with locator {locator}')
            allure.attach(self.driver.get_screenshot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Ожидание локатора {locator} заняло слишком много времени"

    @allure.step('Подтвердить алерт')
    def alert_accept(self):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        time.sleep(2)
