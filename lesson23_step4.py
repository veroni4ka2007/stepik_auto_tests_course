import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    
    # === 1. Открываем страницу с кнопкой ===
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    # === 2. Нажимаем кнопку, которая вызывает confirm ===
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # === 3. Принимаем confirm-диалог ===
    confirm = browser.switch_to.alert
    confirm.accept()  # нажимаем OK
    
    # === 4. На новой странице решаем капчу ===
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