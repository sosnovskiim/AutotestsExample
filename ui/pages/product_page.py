from playwright.sync_api import Page, expect
from ui.base_element import BaseElement

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = BaseElement(page.locator(".kpc-v2-d-title"), "Название товара")
        self.price_main = BaseElement(page.locator(".kpc-v2-d-price-big"), "Цена за м2")
        self.buy_btn = BaseElement(page.get_by_role("link", name="Купить", exact=True), "Кнопка Купить")
        self.cart_link = BaseElement(page.locator("a[href='/cart/']").first, "Кнопка Корзины в шапке")

    def add_to_cart(self):
        self.buy_btn.click()
        expect(self.page.locator(".btn_to_buy")).to_contain_text("В корзине")

    def go_to_cart(self):
        self.cart_link.click()
