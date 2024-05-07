import allure

from tests_kazanexpress.pages.web.city_page import city_page


@allure.parent_suite('Web')
@allure.suite('Локация')
@allure.title(f"Проверка смены города на главной странице")
@allure.severity('Major')
def test_set_city():
    city_page.open()

    city_page.click_set_city()
    city_page.choose_city()

    city_page.check_selected_city()
