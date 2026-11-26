from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from core.config import Config
from core.logger import get_logger

logger = get_logger("BrowserSession")

class BrowserSession:
    def __init__(self):
        self.playwright: Playwright = None
        self.browser: Browser = None
        self.context: BrowserContext = None
        self.page: Page = None

    def start(self):
        logger.info("Запуск браузера...")
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=Config.HEADLESS)
        self.context = self.browser.new_context(base_url=Config.BASE_URL)
        self.context.set_default_timeout(Config.TIMEOUT)
        self.page = self.context.new_page()

    def stop(self):
        logger.info("Остановка браузера...")
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
