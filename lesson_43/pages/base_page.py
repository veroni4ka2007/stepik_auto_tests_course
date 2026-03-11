# pages/base_page.py
import math
import time
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
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.browser.get(self.url)
                return
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                print(f"⚠️ Попытка {attempt + 1} не удалась, повтор через 2 сек...")
                time.sleep(2)

    def solve_quiz_and_get_code(self):
        """Решает математический квиз"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            print("No second alert presented")
            return None

    def solve_quiz_if_present(self, timeout=3):
        """Решает квиз, если он появился"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            
            if "x" in alert_text and ("log" in alert_text.lower() or "sin" in alert_text.lower()):
                x = alert_text.split(" ")[2]
                answer = str(math.log(abs(12 * math.sin(float(x)))))
                alert.send_keys(answer)
                alert.accept()
                
                try:
                    alert = self.browser.switch_to.alert
                    print(f"Your code: {alert.text}")
                    alert.accept()
                except NoAlertPresentException:
                    pass
            else:
                alert.accept()
                
        except (NoAlertPresentException, TimeoutException):
            pass

    def is_element_present(self, how, what, timeout=None):
        """Проверяет наличие элемента на странице"""
        if timeout is None:
            timeout = self.timeout
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
            return True
        except TimeoutException:
            return False

    def is_not_element_present(self, how, what, timeout=5):
        """
        Проверяет, что элемент НЕ появился на странице в течение таймаута.
        Возвращает True, если элемент не появился (хорошо для негативного теста).
        Возвращает False, если элемент появился (тест должен упасть).
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True  # Элемент не появился — это то, что нужно
        return False  # Элемент появился — плохо для негативного теста

    def is_disappeared(self, how, what, timeout=5):
        """
        Проверяет, что элемент ИСЧЕЗ со страницы в течение таймаута.
        Возвращает True, если элемент исчез.
        Возвращает False, если элемент всё ещё виден.
        """
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
            return True  # Элемент исчез
        except TimeoutException:
            return False  # Элемент не исчез

    def find_element(self, locator, timeout=10):
        """Находит элемент с явным ожиданием"""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )