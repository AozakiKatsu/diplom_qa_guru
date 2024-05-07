import allure

from kazanexpress_project.pages.web.favorites_page import favorites_page


@allure.parent_suite('Web')
@allure.suite('Избранное')
@allure.title(f"Добавление товара в избранное")
@allure.severity('Major')
def test_add_favorites():
    favorites_page.open()

    favorites_page.add_item_to_favorites()

    favorites_page.should_item_in_favorites()
