# tests/test_product_page_negative.py
import pytest
from pages.product_page import ProductPage


# 🔴 ПЕРВЫЙ ТЕСТ
# После добавления товара сообщение ПОЯВЛЯЕТСЯ, поэтому проверка is_not_element_present
# будет ЖДАТЬ таймаут (4-5 секунд) и затем УПАДЁТ (AssertionError)
@pytest.mark.xfail(reason="Success message appears after adding to basket - expected behavior")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Тест: после добавления товара сообщение НЕ должно быть видно.
    
    ⚠️ Этот тест:
    - ЖДЁТ 4-5 секунд (таймаут в is_not_element_present)
    - ПАДАЕТ (потому что сообщение ПОЯВЛЯЕТСЯ после добавления)
    """
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, product_url)
    
    page.open()
    page.add_to_basket()
    
    # 🔴 Ждёт таймаут (4-5 сек), затем падает, т.к. сообщение появляется
    assert page.is_success_message_not_present(timeout=4), \
        "Success message should not be present immediately after adding to basket"


# ✅ ВТОРОЙ ТЕСТ
# На чистой странице товара сообщения НЕТ, поэтому is_not_element_present
# будет ЖДАТЬ таймаут и затем УСПЕШНО ЗАВЕРШИТСЯ (вернёт True)
def test_guest_cant_see_success_message(browser):
    """
    Тест: на странице товара без действий сообщения быть не должно.
    
    ✅ Этот тест:
    - ЖДЁТ 4-5 секунд (таймаут в is_not_element_present)
    - ПРОХОДИТ (потому что сообщения действительно нет на странице)
    """
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, product_url)
    
    page.open()
    
    # ✅ Ждёт таймаут, убеждается что сообщения нет — тест проходит
    assert page.is_success_message_not_present(timeout=4), \
        "Success message should not be present on product page before adding"


# 🔴 ТРЕТИЙ ТЕСТ
# После добавления сообщение появляется. is_disappeared будет ЖДАТЬ
# пока оно исчезнет. Если не исчезнет за таймаут — тест УПАДЁТ
@pytest.mark.xfail(reason="Success message does not auto-disappear on this site")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Тест: сообщение должно исчезнуть после добавления.
    
    ⚠️ Этот тест:
    - ЖДЁТ 4-5 секунд (таймаут в is_disappeared)
    - ПАДАЕТ (потому что сообщение НЕ исчезает автоматически)
    """
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, product_url)
    
    page.open()
    page.add_to_basket()
    page.solve_quiz_if_present()
    
    # 🔴 Ждёт таймаут, сообщение не исчезает — тест падает
    assert page.is_success_message_disappeared(timeout=4), \
        "Success message should disappear after 4 seconds"