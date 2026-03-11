#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Инициализация драйвера (предполагается, что chromedriver доступен в PATH)
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    
    # Находим элементы с числами
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    
    # Получаем текст чисел и преобразуем в целые числа
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    
    # Вычисляем сумму
    result = num1 + num2
    print(f"Считаем: {num1} + {num2} = {result}")
    
    # Находим выпадающий список и выбираем значение, равное сумме
    # Важно: передаём строку, а не число!
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    
    # Находим и нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    # Ждём немного, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер после завершения
    browser.quit()