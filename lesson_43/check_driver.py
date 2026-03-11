# check_driver.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver_path = r"C:\chromedriver\chromedriver.exe"

print(f"🔍 Проверка драйвера: {driver_path}")
print(f"✅ Файл существует: {os.path.exists(driver_path)}")

if not os.path.exists(driver_path):
    print("❌ Файл не найден!")
    exit(1)

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")

try:
    print("🚀 Запуск Chrome...")
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    driver.get("https://www.google.com")
    print(f"✅ Успех! Заголовок: {driver.title}")
    driver.quit()
    print("✅ Драйвер работает!")
except Exception as e:
    print(f"❌ Ошибка: {e}")