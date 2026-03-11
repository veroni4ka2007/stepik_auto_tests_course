# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ProductPage(BasePage):
    """Page Object для страницы товара"""
    
    # === ЛОКАТОРЫ ===
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.success")
    SUCCESS_MESSAGE_ALT = (By.CSS_SELECTOR, "div.alertinner.wicon")
    SUCCESS_MESSAGE_FALLBACK = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def add_to_basket(self):
        """Нажимает кнопку 'Добавить в корзину'"""
        button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        """Возвращает название товара"""
        element = self.find_element(self.PRODUCT_NAME)
        return element.text.strip()

    def get_product_price(self):
        """Возвращает цену товара"""
        element = self.find_element(self.PRODUCT_PRICE)
        return element.text.strip()

    def _find_success_message(self, timeout=10):
        """Ищет сообщение об успехе"""
        for locator in [self.SUCCESS_MESSAGE, self.SUCCESS_MESSAGE_ALT, self.SUCCESS_MESSAGE_FALLBACK]:
            try:
                return WebDriverWait(self.browser, timeout).until(
                    EC.presence_of_element_located(locator)
                )
            except:
                continue
        return None

    def get_success_message_text(self):
        """Возвращает текст сообщения"""
        element = self._find_success_message()
        if element:
            return element.text.strip()
        raise Exception("Success message not found")

    def should_be_added_message(self, timeout=10):
        """Проверяет, что сообщение появилось"""
        element = self._find_success_message(timeout)
        assert element is not None, "Success message is not presented"
        return True

    def product_name_matches_in_success_message(self, expected_name):
        """Проверяет название в сообщении"""
        message = self.get_success_message_text()
        assert expected_name in message, \
            f"Product name '{expected_name}' not found in message: '{message}'"

    def price_matches_in_success_message(self, expected_price):
        """Проверяет цену в сообщении"""
        message = self.get_success_message_text()
        assert expected_price in message, \
            f"Product price '{expected_price}' not found in message: '{message}'"

    def is_success_message_not_present(self, timeout=5):
        """Проверяет, что сообщение НЕ отображается"""
        for locator in [self.SUCCESS_MESSAGE, self.SUCCESS_MESSAGE_ALT, self.SUCCESS_MESSAGE_FALLBACK]:
            if not self.is_not_element_present(*locator, timeout):
                return False
        return True

    def is_success_message_disappeared(self, timeout=5):
        """Проверяет, что сообщение исчезло"""
        for locator in [self.SUCCESS_MESSAGE, self.SUCCESS_MESSAGE_ALT, self.SUCCESS_MESSAGE_FALLBACK]:
            try:
                WebDriverWait(self.browser, timeout).until_not(
                    EC.presence_of_element_located(locator)
                )
            except:
                continue
        return True