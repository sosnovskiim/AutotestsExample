from playwright.sync_api import Locator
from core.logger import get_logger

logger = get_logger("BaseElement")

class BaseElement:
    def __init__(self, locator: Locator, name: str):
        self.locator = locator
        self.name = name

    def click(self):
        logger.info(f"Клик по элементу: {self.name}")
        self.locator.click()

    def fill(self, text: str):
        logger.info(f"Ввод текста '{text}' в элемент: {self.name}")
        self.locator.fill(text)

    def get_text(self):
        return self.locator.inner_text()

    def is_visible(self):
        return self.locator.is_visible()
