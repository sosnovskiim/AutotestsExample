from playwright.sync_api import Page, expect
from ui.base_element import BaseElement

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.h1_title = BaseElement(page.locator("h1"), "Заголовок страницы оформления")

    def verify_page_opened(self):
        expect(self.h1_title.locator).to_have_text("Оформление заказа")
