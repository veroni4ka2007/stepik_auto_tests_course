import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    
    # === 1. Открываем страницу с кнопкой ===
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    # === 2. Нажимаем кнопку → открывается новая вкладка ===
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # === 3. Переключаемся на НОВУЮ вкладку ===
    # window_handles[0] — старая вкладка, [1] — новая
    browser.switch_to.window(browser.window_handles[1])
    
    # === 4. Решаем капчу на новой странице ===
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    # Считаем математическую функцию
    result = str(math.log(abs(12 * math.sin(int(x)))))
    
    # Вводим ответ в поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result)
    
    # === 5. Нажимаем Submit ===
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # === 6. Получаем и выводим код ===
    time.sleep(2)
    code = browser.find_element(By.TAG_NAME, "pre").text
    print(f"🎉 Ваш код: {code}")
    
finally:
    time.sleep(3)
    browser.quit()