from playwright.sync_api import Page
from ui.base_element import BaseElement

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_card = BaseElement(page.get_by_role("link", name="Паркетная доска Таркетт Сальса Дуб Лён BR (Tarkett Salsa Oak Linen)", exact=True), "Карточка товара")

    def open_first_product(self) -> Page:
        with self.page.expect_popup() as popup_info:
            self.product_card.click()
        return popup_info.value
