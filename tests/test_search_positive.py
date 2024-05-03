import allure

from diplom_qa_guru.pages.search_page import search_page


@allure.parent_suite('Web')
@allure.suite('Поиск')
@allure.title(f"Проверка поиска")
@allure.severity('Major')
def test_search_positive():
    search_page.open()

    search_page.fill_search_input()

    search_page.check_search_results()
