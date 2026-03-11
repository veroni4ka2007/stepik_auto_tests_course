# tests/test_product_page.py
import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    
    # 🔴 Баг найден здесь — помечаем как ожидаемо падающий (xfail)
    # Замените offer2 на тот, где реально падает тест в вашем запуске
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        marks=pytest.mark.xfail(reason="Bug: incorrect price in success message for promo=offer2")
    ),
    
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
])
def test_guest_can_add_product_to_basket(browser, link):
    """
    Универсальный тест: гость может добавить ЛЮБОЙ товар в корзину.
    
    Проверяет:
    1. Сообщение о добавлении появляется
    2. Название товара в сообщении = название на странице
    3. Цена в сообщении = цена на странице
    
    Запускается на 10 промо-ссылках для поиска бага.
    """
    # === ARRANGE ===
    page = ProductPage(browser, link)
    
    # === ACT ===
    page.open()
    
    # 🔑 Извлекаем данные ДО добавления в корзину — это эталонные значения
    expected_name = page.get_product_name()
    expected_price = page.get_product_price()
    
    page.add_to_basket()
    
    # 🔑 Квиз появляется только при определённых промо — решаем если есть
    page.solve_quiz_if_present()
    
    # === ASSERT ===
    # 🔑 Передаём извлечённые данные в проверки — тест независим от контента!
    page.should_be_added_message()
    page.product_name_matches_in_success_message(expected_name)
    page.price_matches_in_success_message(expected_price)
    
    # === INFO ===
    print(f"\n✅ Тест пройден: {link.split('?')[0].split('/')[-1]}")