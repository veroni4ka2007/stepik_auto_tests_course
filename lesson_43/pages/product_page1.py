# pages/product_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    """Page Object для страницы товара"""
    
    # === ЛОКАТОРЫ ===
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner.wicon")
    
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    # === ДЕЙСТВИЯ ===
    
    def add_to_basket(self):
        """Нажимает кнопку 'Добавить в корзину'"""
        button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        button.click()

    # === ПОЛУЧЕНИЕ ДАННЫХ ===
    
    def get_product_name(self):
        """Возвращает название товара со страницы"""
        return self.get_element_text(self.PRODUCT_NAME)

    def get_product_price(self):
        """Возвращает цену товара со страницы"""
        return self.get_element_text(self.PRODUCT_PRICE)

    def get_success_message_text(self):
        """Возвращает текст сообщения об успешном добавлении"""
        return self.get_element_text(self.SUCCESS_MESSAGE)

    # === ПРОВЕРКИ (ASSERTIONS) ===
    
    def should_be_added_message(self, timeout=5):
        """Проверяет, что сообщение о добавлении в корзину появилось"""
        assert self.is_element_present(*self.SUCCESS_MESSAGE, timeout=timeout), \
            "❌ Success message about adding to basket is not presented"

    def product_name_in_success_message(self, product_name):
        """Проверяет, что название товара в сообщении совпадает с добавленным"""
        message = self.get_success_message_text()
        assert product_name in message, \
            f"❌ Product name '{product_name}' not found in message: '{message}'"

    def price_in_success_message(self, product_price):
        """Проверяет, что цена товара отображается в сообщении корзины"""
        message = self.get_success_message_text()
        assert product_price in message, \
            f"❌ Product price '{product_price}' not found in message: '{message}'"