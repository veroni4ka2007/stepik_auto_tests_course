import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Добавляет параметр --language в командную строку pytest"""
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Language code for the interface (e.g., en, es, fr, ru)'
    )


@pytest.fixture(scope='function')
def browser(request):
    """Фикстура browser с поддержкой параметра языка"""
    # Получаем язык из командной строки
    language = request.config.getoption('--language')
    
    # Настраиваем Chrome с нужным языком интерфейса
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': language  # Устанавливаем язык браузера
    })
    
    # Инициализируем браузер
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    
    yield browser
    
    # Закрываем браузер после теста
    browser.quit()