#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-картинку сундука и получаем значение атрибута valuex
    treasure_img = browser.find_element(By.ID, "treasure")
    x = treasure_img.get_attribute("valuex")

    # Вычисляем результат функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждём, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер после завершения
    browser.quit()