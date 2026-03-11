# tests/test_product_page.py
import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize("product_url", [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    # Можно добавить ещё товаров для параметризации
])
def test_guest_can_add_product_to_basket(browser, product_url):
    """
    Универсальный тест: гость может добавить ЛЮБОЙ товар в корзину.
    
    Проверяет:
    1. Сообщение о добавлении появляется
    2. Название товара в сообщении = название на странице
    3. Цена в сообщении = цена на странице
    """
    # === ARRANGE ===
    page = ProductPage(browser, product_url)
    
    # === ACT ===
    page.open()
    
    # 🔑 Извлекаем данные ДО добавления в корзину — это наши "эталонные" значения
    expected_name = page.get_product_name()
    expected_price = page.get_product_price()
    
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # Решаем квиз, код выводится в консоль
    
    # === ASSERT ===
    # 🔑 Передаём извлечённые данные в проверки — тест независим от контента!
    page.should_be_added_message()
    page.product_name_matches_in_success_message(expected_name)
    page.price_matches_in_success_message(expected_price)
    
    # === INFO ===
    print(f"\n✅ Тест пройден для товара: {expected_name}")
    print(f"   Цена: {expected_price}")