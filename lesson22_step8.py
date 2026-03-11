#
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    # === 1. Заполняем текстовые поля ===
    browser.find_element(By.NAME, "firstname").send_keys("Artur")
    browser.find_element(By.NAME, "lastname").send_keys("Piroshkov")
    browser.find_element(By.NAME, "email").send_keys("veronika@test.ru")
    
    # === 2. Создаём пустой .txt файл для загрузки ===
    # Сохраняем в текущую папку, чтобы не работать с путями
    file_path = os.path.join(os.getcwd(), "test_file.txt")
    with open(file_path, "w") as f:
        f.write("")  # пустой файл — можно написать любой текст
    
    # === 3. Загружаем файл через send_keys ===
    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)
    
    # === 4. Кликаем кнопку Submit ===
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # === 5. Ждём и выводим код ===
    time.sleep(2)
    result = browser.find_element(By.TAG_NAME, "pre").text
    print(f"🎉 Ваш код: {result}")
    
finally:
    # Удаляем тестовый файл после загрузки (опционально)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    time.sleep(3)
    browser.quit()