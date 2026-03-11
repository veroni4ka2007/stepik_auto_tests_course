#
# lesson6_step11.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Инициализируем браузер
    browser = webdriver.Chrome()

    # Открываем страницу регистрации
    # Для проверки бага поменяйте на registration2.html
    browser.get("http://suninjuly.github.io/registration1.html")

    # Находим поля формы с помощью УНИКАЛЬНЫХ CSS-селекторов
    # Используем вложенность и комбинацию классов для уникальности

    # Поле First name - ищем input с классом first внутри div с классом first_class
    first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input.first")
    first_name_input.send_keys("Ivan")

    # Поле Last name - ищем input с классом second внутри div с классом second_class
    # На странице registration2.html этого элемента НЕТ - тест упадет с NoSuchElementException
    last_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input.second")
    last_name_input.send_keys("Petrov")

    # Поле Email - ищем input с классом third внутри div с классом third_class
    email_input = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input.third")
    email_input.send_keys("ivan@test.com")

    # Поле Phone
    phone_input = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class input.first")
    phone_input.send_keys("+79991234567")

    # Поле Address
    address_input = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class input.second")
    address_input.send_keys("Moscow")

    # Находим и нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Ждем немного и проверяем, что перешли на страницу с результатом
    time.sleep(1)
    print("Тест успешно пройден!")

finally:
    # Обязательно закрываем браузер
    time.sleep(3)
    browser.quit()