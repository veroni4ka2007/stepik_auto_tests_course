from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Находим ВСЕ текстовые поля на странице
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    
    # Заполняем каждое поле коротким текстом (для скорости)
    for element in elements:
        element.send_keys("a")

    # Находим и кликаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла