import allure

from diplom_qa_guru.pages.basket_page import basket_page


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Удаление товара из корзины")
def test_delete_from_basket():
    basket_page.open()

    basket_page.add_item_to_basket()
    basket_page.delete_item_from_basket()

    basket_page.should_basket_empty()
