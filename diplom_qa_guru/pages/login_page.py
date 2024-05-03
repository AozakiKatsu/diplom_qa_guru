import allure
from selene import browser, have


class LoginPage:
    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Кликаем на кнопку логина')
    def click_login_button(self):
        browser.element('[data-test-id=button__auth]').click()

    @allure.step('Проверяем что открылся поп-ап авторизации')
    def should_pop_up_visible(self):
        browser.element('.sign-in-phone').should(have.text('Введите номер телефона'))

    @allure.step('Вводим неверный номер телефона')
    def fill_phone_number(self):
        browser.element('.no-after').click().type('1').press_enter()

    @allure.step('Проверяем, что выдало ошибку')
    def should_error_message(self):
        browser.element('.error-text').should(have.text('Неверный формат номера'))


login_page = LoginPage()
