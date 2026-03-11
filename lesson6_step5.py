#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 🔍 Ищем ссылку по вычисленному тексту
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link_element = browser.find_element(By.LINK_TEXT, link_text)
    link_element.click()

    # 📝 Заполняем форму (как в предыдущем задании)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  # ✅ Уникальный класс для города
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()