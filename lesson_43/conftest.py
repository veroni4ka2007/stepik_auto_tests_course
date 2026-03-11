# conftest.py
import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    """Фикстура с путём к ChromeDriver: C:\chromedriver"""
    print("\n🚀 Запуск браузера Chrome...")
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    # 🔑 Путь к драйверу
    driver_path = r"C:\chromedriver\chromedriver.exe"
    
    print(f"🔍 Используем драйвер: {driver_path}")
    
    if not os.path.exists(driver_path):
        raise FileNotFoundError(
            f"❌ ChromeDriver not found at: {driver_path}\n"
            f"💡 Убедитесь, что файл chromedriver.exe лежит в папке C:\\chromedriver\\"
        )
    
    try:
        driver = webdriver.Chrome(
            service=Service(driver_path),
            options=options
        )
        print("✅ Chrome запущен успешно!")
    except Exception as e:
        print(f"❌ Ошибка запуска Chrome: {e}")
        raise
    
    # Скрываем признак автоматизации
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    
    yield driver
    
    print("\n🔚 Завершение теста...")
    # 🔑 Игнорируем ошибки при закрытии браузера (WinError 10054)
    try:
        time.sleep(0.5)
        driver.quit()
        print("✅ Браузер закрыт")
    except Exception as e:
        print(f"⚠️ Предупреждение при закрытии (можно игнорировать): {type(e).__name__}")
        # Принудительно закрываем процесс Chrome
        try:
            driver.service.process.kill()
        except:
            pass