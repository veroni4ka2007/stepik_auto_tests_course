import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    
    def setUp(self):
        """Инициализация браузера перед каждым тестом"""
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
    
    def tearDown(self):
        """Закрытие браузера после каждого теста"""
        time.sleep(1)
        self.browser.quit()
    
    def test_registration1_success(self):
        """Тест для registration1.html — должен пройти успешно"""
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")
        
        # Заполняем форму с помощью уникальных CSS-селекторов
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input.first")
        first_name.send_keys("Ivan")
        
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input.second")
        last_name.send_keys("Petrov")
        
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input.third")
        email.send_keys("ivan@test.com")
        
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class input.first")
        phone.send_keys("+79991234567")
        
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class input.second")
        address.send_keys("Moscow")
        
        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        
        # Проверяем результат с помощью assertEqual
        time.sleep(1)
        result_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(result_text, "Congratulations! You have successfully registered!", 
                        "Сообщение об успехе не совпадает")
    
    def test_registration2_bug(self):
        """Тест для registration2.html — должен упасть с NoSuchElementException"""
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")
        
        # Заполняем форму
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input.first")
        first_name.send_keys("Ivan")
        
        # ⚠️ Этот элемент отсутствует на registration2.html — тест упадёт с NoSuchElementException
        # Не используем try/except — пусть unittest сам обработает исключение!
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input.second")
        last_name.send_keys("Petrov")
        
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input.third")
        email.send_keys("ivan@test.com")
        
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class input.first")
        phone.send_keys("+79991234567")
        
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class input.second")
        address.send_keys("Moscow")
        
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        
        time.sleep(1)
        result_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(result_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main(verbosity=2)