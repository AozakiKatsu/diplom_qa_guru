import allure

from diplom_qa_guru.pages.favorites_page import favorites_page


@allure.parent_suite('Web')
@allure.suite('Избранное')
@allure.title(f"Удаление товара из избранного")
@allure.severity('Major')
def test_delete_from_favorites():
    favorites_page.open()

    favorites_page.add_item_to_favorites()
    favorites_page.delete_item_from_favorites()

    favorites_page.should_favorites_empty()
