from playwright.sync_api import Page
from ui.base_element import BaseElement

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = BaseElement(page.get_by_role("searchbox", name="Быстрый и умный поиск"), "Строка поиска")
        self.search_btn = BaseElement(page.get_by_role("button", name="Поиск"), "Кнопка Найти")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_btn.click()
