import allure
from selene import browser, have


class CityPage:
    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Кликаем на текущий город"')
    def click_set_city(self):
        browser.element('[data-test-id=button__select-city]').click()

    @allure.step('Выбираем город "Воронеж"')
    def choose_city(self):
        browser.all('[data-test-id=list__city]').element_by(have.text('Воронеж')).click()

    @allure.step('Проверяем, что город поменялся на Воронеж')
    def check_selected_city(self):
        browser.element('[data-test-id=button__select-city]').should(have.text('Воронеж'))


city_page = CityPage()
