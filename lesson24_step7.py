#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    """
    Вычисляет математическое выражение: log(abs(12 * sin(x)))
    """
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Инициализация WebDriver (Chrome)
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # Ожидаем, пока цена не станет $100 (минимум 12 секунд)
    # Элемент с ценой имеет id="price"
    price_condition = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    WebDriverWait(browser, 15).until(price_condition)
    
    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    # Дополнительная пауза для полной загрузки формы с задачей (опционально)
    time.sleep(1)
    
    # Находим элемент с задачей и извлекаем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в поле ввода
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
    # Даем время увидеть результат (алерт с ответом)
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()