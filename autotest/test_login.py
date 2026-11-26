import pytest
import allure
from core.config import Config
from ui.pages.login_page import LoginPage

@allure.epic("Авторизация")
@allure.feature("Позитивные проверки")
class TestLoginPositive:
    
    @allure.id("AUTH-01")
    @allure.title("Успешный вход по логину")
    def test_login_with_username(self, page):
        login_page = LoginPage(page)
        page.goto("/")
        login_page.open_modal()
        login_page.login(Config.LOGIN, Config.PASSWORD)
        login_page.verify_success()

    @allure.id("AUTH-02")
    @allure.title("Успешный вход по электронной почте")
    def test_login_with_email(self, page):
        login_page = LoginPage(page)
        page.goto("/")
        login_page.open_modal()
        login_page.login(Config.EMAIL, Config.PASSWORD)
        login_page.verify_success()


@allure.epic("Авторизация")
@allure.feature("Негативные проверки (Параметризованные)")
class TestLoginNegative:

    @allure.id("AUTH-NEG")
    @allure.title("Ошибки авторизации: {case_name}")
    @pytest.mark.parametrize("case_name, username, password", [
        ("Пустой логин", "", Config.PASSWORD),
        ("Пустой пароль", Config.LOGIN, ""),
        ("Оба поля пустые", "", ""),
        ("Неверный пароль", Config.LOGIN, "wrongpass"),
        ("Логин с пробелами", " sosnovskiim ", Config.PASSWORD),
        ("Пароль с пробелами", Config.LOGIN, " 7SKD9z "),
        ("Слишком длинный логин", "a" * 256, Config.PASSWORD),
        ("Спецсимволы в логине", "<script>alert(1)</script>", Config.PASSWORD),
    ])
    def test_login_negative(self, page, case_name, username, password):
        allure.dynamic.parameter("Тестовые данные", f"Логин: '{username}', Пароль: '{password}'")
        login_page = LoginPage(page)
        page.goto("/")
        login_page.open_modal()
        login_page.login(username, password)
        login_page.verify_error()
