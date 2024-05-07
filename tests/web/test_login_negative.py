import allure

from tests_kazanexpress.pages.web.login_page import login_page


@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Проверка ввода неправильного номера телефона")
@allure.severity('Critical')
def test_login_negative():
    login_page.open()

    login_page.click_login_button()
    login_page.fill_phone_number()

    login_page.should_error_message()
