import time

import allure
from selene import browser, have, be


class FavoritesPage:
    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')

    @allure.step('Находим и добавляем товар в избранное')
    def add_item_to_favorites(self):
        browser.element('[data-test-id=input__search]').type('Кастрюля из нержавеющей стали').press_enter()
        browser.all('[data-test-id=item__product-card]').element_by(
            have.text('Кастрюля из нержавеющей стали со стеклянной крышкой')).click()
        try:
            browser.all('.radio-text-wrapper').element_by(have.text('2 литра')).click()
            browser.element('.add-cart>.favorite').click()
        except:
            browser.all('[data-test-id=item__sku]').element_by(have.text('2 литра')).click()
            browser.all('[data-test-id=button__add-to-favorites]').element_by(have.text('В желания')).click()

        browser.element('[data-test-id=button__wishes]').click()

    @allure.step('Проверяем то что в избранном находится товар добавленный нами')
    def should_item_in_favorites(self):
        browser.element('[data-test-id=item__product-card]').should(have.text('Кастрюля из нержавеющей стали'))

    @allure.step('Удаляем товар из избранного')
    def delete_item_from_favorites(self):
        browser.element('[data-test-id="list__products"] .list-complete-item').should(be.visible)
        browser.element('[data-test-id=button__add-to-favorites]').click()

    @allure.step('Проверяем то что в избранном нет товаров')
    def should_favorites_empty(self):
        browser.element('[data-test-id=text__empty-favorite-title]').should(have.text('Добавьте то, что понравилось'))


favorites_page = FavoritesPage()
