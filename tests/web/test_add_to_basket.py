import allure

from diplom_qa_guru.pages.web.basket_page import basket_page


@allure.parent_suite('Web')
@allure.suite('Корзина')
@allure.title(f"Добавление товара в корзину")
@allure.severity('Blocker')
def test_add_to_basket():
    basket_page.open()

    basket_page.add_item_to_basket()

    basket_page.should_item_in_basket()
