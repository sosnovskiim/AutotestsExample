from playwright.sync_api import Page
from ui.base_element import BaseElement

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = BaseElement(page.locator(".basket-item-info-name-link"), "Название в корзине")
        self.item_price = BaseElement(page.locator(".basket-item-price-current-text").last, "Сумма товара")
        self.checkout_btn = BaseElement(page.get_by_role("button", name="Оформить заказ"), "Кнопка Оформить заказ")

    def click_checkout(self):
        self.checkout_btn.click()
