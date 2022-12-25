import time

from page_object.admin_auth_page import AdminAuthPage
from page_object.admin_main_page import AdminMainPage
from page_object.admin_products_page import AdminProductsPage
from page_object.admin_product_adding_page import AdminProductAddingPage
from test_data.data import add_product, admin_user
import allure


@allure.title('Авторизация в админку')
def test_login_to_admin(browser):
    auth_page = AdminAuthPage(browser)
    main_page = AdminMainPage(browser)

    auth_page.open(path=AdminAuthPage._path)
    auth_page.check_open_admin_login_page()
    auth_page.login_to_account(username=admin_user["name"], password=admin_user["password"])
    main_page.check_open_admin_main_page()


@allure.title('Открытие страницы добавления товара')
def test_open_product_cart(browser):
    auth_page = AdminAuthPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)

    auth_page.open(path=AdminAuthPage._path)
    auth_page.login_to_account(username=admin_user["name"], password=admin_user["password"])
    admin_main_page.check_open_admin_main_page()

    admin_main_page.click_catalog_menu_btn()
    time.sleep(1)
    admin_main_page.click_products_menu_btn()
    admin_products_page.check_open_admin_products_page()


@allure.title('Добавление нового товара')
def test_add_new_product(browser):
    auth_page = AdminAuthPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)
    admin_product_adding_page = AdminProductAddingPage(browser)

    auth_page.open(path=AdminAuthPage._path)
    auth_page.login_to_account(username=admin_user["name"], password=admin_user["password"])
    admin_main_page.check_open_admin_main_page()

    admin_main_page.click_catalog_menu_btn()
    time.sleep(1)
    admin_main_page.click_products_menu_btn()
    admin_products_page.check_open_admin_products_page()

    admin_products_page.click_add_product_btn()
    admin_product_adding_page.enter_values_into_text_fields(
        product_name=add_product()['product_name'], meta_tag_title=add_product()['meta_tag_title'],
        description=add_product()['description'], model=add_product()['model'])
    admin_product_adding_page.click_save_btn()
    admin_products_page.check_open_admin_products_page()
    admin_products_page.check_success_alert()


@allure.title('Удаление товара')
def test_remove_added_item(browser):
    auth_page = AdminAuthPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)

    auth_page.open(path=AdminAuthPage._path)
    auth_page.login_to_account(username=admin_user["name"], password=admin_user["password"])
    admin_main_page.check_open_admin_main_page()

    admin_main_page.click_catalog_menu_btn()
    time.sleep(1)
    admin_main_page.click_products_menu_btn()
    admin_products_page.check_open_admin_products_page()

    admin_products_page.click_random_product_checkbox()
    admin_products_page.click_delete_btn()
    admin_products_page.alert_accept()
    admin_products_page.check_success_alert()
