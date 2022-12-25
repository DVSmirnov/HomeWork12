import random
import time

import allure
import pytest

from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from page_object.register_page import RegisterPage
from page_object.success_page import SuccessPage
from page_object.user_logout_page import UserLogoutPage
from page_object.user_main_page import UserMainPage
from test_data.data import random_user


@allure.title("Изменение валюты")
@pytest.mark.parametrize("currency_name", ["USD", "GBP", "EUR"])
def test_switch_currency(browser, currency_name):
    main_page = MainPage(browser)

    main_page.open()
    main_page.click_currency_btn()
    main_page.click_currency_by_name(currency_name)
    main_page.check_currency_value(currency_name)


@allure.title("Проверка главной страницы")
def test_check_main_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.check_open_main_page()


@allure.title("Регистрация нового пользователя")
def test_register_new_acc(browser):
    main_page = MainPage(browser)
    register_page = RegisterPage(browser)
    success_page = SuccessPage(browser)
    user_main_page = UserMainPage(browser)

    main_page.open()
    main_page.click_my_account_btn()
    main_page.click_value_in_my_account_dropdown(value="Register")

    register_page.register_new_account(
        first_name=random_user['first_name'],
        last_name=random_user['last_name'],
        email=random_user['email'],
        telephone=random_user['telephone'],
        password=random_user['password'],
        confirm_pass=random_user['password']
    )
    success_page.check_open_success_page()
    success_page.click_continue_button()
    user_main_page.check_open_user_main_page()


@allure.title("Авторизация в личный кабинет")
def test_log_in_account(browser):
    main_page = MainPage(browser)
    register_page = RegisterPage(browser)
    login_page = LoginPage(browser)
    user_main_page = UserMainPage(browser)

    # Подготовка тестовых данных
    main_page.open()
    main_page.click_my_account_btn()
    main_page.click_value_in_my_account_dropdown(value="Register")

    register_page.register_new_account(
        first_name=random_user['first_name'],
        last_name=random_user['last_name'],
        email=random_user['email'],
        telephone=random_user['telephone'],
        password=random_user['password'],
        confirm_pass=random_user['password']
    )
    main_page.click_my_account_btn()
    main_page.click_value_in_my_account_dropdown(value="Logout")
    # Конец подготовки тестовых данных

    main_page.click_my_account_btn()
    main_page.click_value_in_my_account_dropdown(value='Login')
    login_page.login_to_account(email=random_user['email'], password=random_user['password'])
    user_main_page.check_open_user_main_page()


@allure.title("Выход из личного кабинета")
def test_logout_from_acc(browser):
    main_page = MainPage(browser)
    register_page = RegisterPage(browser)
    user_logout_page = UserLogoutPage(browser)

    # Подготовка тестовых данных
    main_page.open()
    main_page.click_my_account_btn()
    main_page.click_value_in_my_account_dropdown(value="Register")

    register_page.register_new_account(
        first_name=random_user['first_name'],
        last_name=random_user['last_name'],
        email=random_user['email'],
        telephone=random_user['telephone'],
        password=random_user['password'],
        confirm_pass=random_user['password']
    )
    # Конец подготовки тестовых данных

    main_page.click_my_account_btn()
    main_page.click_value_in_my_account_dropdown(value="Logout")
    user_logout_page.click_continue_btn()
    main_page.check_open_main_page()
