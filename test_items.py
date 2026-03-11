from selenium.webdriver.common.by import By
import time


def test_add_to_cart_button_exists_on_product_page(browser):
    """
    Проверяет, что на странице товара присутствует кнопка 
    добавления в корзину для разных языков интерфейса
    """
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    
    # ⚠️ Задержка для визуальной проверки языка интерфейса (по заданию)
    # Удалите или закомментируйте после проверки
    time.sleep(30)
    
    # Находим кнопку добавления в корзину по уникальному CSS-селектору
    # Селектор .btn-add-to-basket уникален для этой страницы
    add_to_cart_button = browser.find_element(
        By.CSS_SELECTOR, 
        "button.btn-add-to-basket"
    )
    
    # Проверяем, что кнопка отображается на странице
    assert add_to_cart_button.is_displayed(), \
        "Кнопка добавления в корзину не найдена или не отображается на странице товара"