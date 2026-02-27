import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    
    # === 1. Считываем значение x ===
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = str(math.log(abs(12 * math.sin(int(x)))))  # или нужная формула из задачи
    
    # === 2. Находим поле для ответа и скроллим к нему ===
    answer_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(result)
    
    # === 3. Выбираем checkbox "I'm the robot" ===
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()
    
    # === 4. Переключаем radiobutton "Robots rule!" ===
    robots_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", robots_radio)
    robots_radio.click()
    
    # === 5. Находим и кликаем кнопку Submit ===
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    
    # === 6. Ждём и выводим код ===
    time.sleep(2)
    alert_text = browser.find_element(By.TAG_NAME, "pre").text
    print(f"🎉 Ваш код: {alert_text}")
    
finally:
    time.sleep(5)
    browser.quit()