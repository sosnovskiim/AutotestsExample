import allure
from playwright.sync_api import expect
from ui.pages.home_page import HomePage
from ui.pages.search_results_page import SearchResultsPage
from ui.pages.product_page import ProductPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage

@allure.epic("Сквозной сценарий")
@allure.feature("Покупка товара гостем")
class TestE2E:

    @allure.id("E2E-01")
    @allure.title("Полный путь оформления заказа (от поиска до формы заказа)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_guest_checkout(self, page):
        home_page = HomePage(page)
        search_results = SearchResultsPage(page)
        
        with allure.step("Открытие главной страницы и поиск товара"):
            page.goto("/")
            home_page.search("паркет")

        with allure.step("Переход в карточку товара (в новой вкладке)"):
            product_page_obj = search_results.open_first_product()
            product_page = ProductPage(product_page_obj)
            
            expect(product_page.title.locator).to_contain_text("Паркетная доска Таркетт")

        with allure.step("Добавление товара в корзину"):
            product_page.add_to_cart()

        with allure.step("Переход в корзину и проверка содержимого"):
            product_page.go_to_cart()
            cart_page = CartPage(product_page_obj)
            
            expect(cart_page.item_name.locator).to_contain_text("Паркетная доска Таркетт")
            expect(cart_page.item_price.locator).to_contain_text("19 090")

        with allure.step("Нажатие кнопки 'Оформить заказ'"):
            cart_page.click_checkout()
            checkout_page = CheckoutPage(product_page_obj)
            
            checkout_page.verify_page_opened()
