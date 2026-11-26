from playwright.sync_api import Page, expect
from core.config import Config
from ui.base_element import BaseElement
from core.logger import get_logger

logger = get_logger("LoginPage")

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_link = BaseElement(page.get_by_role("link", name="Вход").first, "Ссылка Вход")
        self.login_input = BaseElement(page.locator("input[name='USER_LOGIN']"), "Поле Логин")
        self.password_input = BaseElement(page.locator("input[name='USER_PASSWORD']"), "Поле Пароль")
        self.submit_btn = BaseElement(page.locator("input[name='AUTH_ACTION']"), "Кнопка Войти")
        self.error_msg = BaseElement(page.locator(".alert.alert-danger"), "Сообщение об ошибке")
        self.profile_link = page.locator(".kph-act--user.is-auth")

    def open_modal(self):
        self.login_link.click()

    def login(self, username, password):
        if username:
            self.login_input.fill(username)
        if password:
            self.password_input.fill(password)
        self.submit_btn.click()
        
    def verify_success(self):
        logger.info("Проверка успешной авторизации")
        expect(self.profile_link).to_be_visible()
        expect(self.page.locator(".kph-act__avatar")).to_contain_text("SO")

    def verify_error(self):
        logger.info("Проверка ошибки авторизации")
        self.page.wait_for_load_state("networkidle")
        self.open_modal()
        expect(self.error_msg.locator).to_be_visible()
        expect(self.error_msg.locator).to_contain_text("Неверный логин или пароль.")
