import allure

from diplom_qa_guru.pages.favorites_page import favorites_page


@allure.parent_suite('Web')
@allure.suite('Избранное')
@allure.title(f"Добавление товара в избранное")
def test_add_favorites():
    favorites_page.open()

    favorites_page.add_item_to_favorites()

    favorites_page.should_item_in_favorites()
