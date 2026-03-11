# pages/base_page.py
import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Objects"""
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        """Открывает страницу в браузере"""
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        """
        Решает математический квиз из алерта и возвращает проверочный код.
        Метод вызывается после добавления товара в корзину.
        """
        # Переключаемся на первый алерт с вопросом
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]  # Извлекаем число из текста алерта
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        
        # Обрабатываем второй алерт с кодом
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            print("No second alert presented")
            return None

    def is_element_present(self, how, what, timeout=None):
        """Проверяет наличие элемента на странице в течение таймаута"""
        if timeout is None:
            timeout = self.timeout
            
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator):
        """Возвращает текст элемента по локатору"""
        return self.browser.find_element(*locator).text