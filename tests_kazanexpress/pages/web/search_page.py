import allure
from selene import browser, have


class SearchPage:
    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')

    @allure.step('В поле поиска вводим поисковой запрос "Кастрюли"')
    def fill_search_input(self):
        browser.element('[data-test-id=input__search]').type('Кастрюли').press_enter()

    @allure.step('Проверяем результат поиска (в тайтле поиска есть слово "Кастрюли и ковши"')
    def check_search_results(self):
        browser.element('[data-test-id=text__title]').should(have.text('Кастрюли и ковши'))


search_page = SearchPage()
