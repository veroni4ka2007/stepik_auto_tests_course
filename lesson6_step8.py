#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    
    # Заполняем форму (как в предыдущих шагах)
    browser.find_element(By.TAG_NAME, "input").send_keys("Veronika")
    browser.find_element(By.NAME, "last_name").send_keys("YourLastName")
    browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("Moscow")
    browser.find_element(By.ID, "country").send_keys("Russia")
    
    # 🔑 Ищем кнопку ПО XPath по точному тексту "Submit"
    submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    
    # Ждём и выводим код
    time.sleep(2)
    result = browser.find_element(By.TAG_NAME, "pre").text
    print(f"Ваш код: {result}")
    
finally:
    time.sleep(5)
    browser.quit()