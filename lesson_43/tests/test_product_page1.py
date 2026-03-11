# tests/test_product_page.py
import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize("promo", ["newYear"])
def test_guest_can_add_product_to_basket(browser, promo):
    """
    Тест-кейс: Гость может добавить товар в корзину со страницы товара.
    
    Проверяет:
    1. Появление сообщения об успешном добавлении
    2. Название товара в сообщении совпадает с реальным
    3. Цена в сообщении совпадает с ценой товара
    """
    # === ARRANGE ===
    product_url = (
        f"http://selenium1py.pythonanywhere.com"
        f"/catalogue/the-shellcoders-handbook_209/?promo={promo}"
    )
    page = ProductPage(browser, product_url)
    
    # === ACT ===
    page.open()                           # Открываем страницу товара
    page.add_to_basket()                  # Нажимаем "Добавить в корзину"
    page.solve_quiz_and_get_code()        # Решаем квиз, получаем код в консоль
    
    # Сохраняем ожидаемые значения (берём ПОСЛЕ квиза, когда страница обновилась)
    expected_product_name = page.get_product_name()
    expected_product_price = page.get_product_price()
    
    # === ASSERT ===
    page.should_be_added_message()                              # Сообщение есть
    page.product_name_in_success_message(expected_product_name) # Название совпадает
    page.price_in_success_message(expected_product_price)       # Цена совпадает
    
    # === ДОП. ИНФО В КОНСОЛЬ ===
    print(f"\n✅ Тест пройден!")
    print(f"   Товар: {expected_product_name}")
    print(f"   Цена: {expected_product_price}")