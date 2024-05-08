import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MobileFavoritesPage:
    @allure.step('Находим и добавляем товар в избранное')
    def add_item_to_favorites(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/search_bar')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).set('Кастрюля из нержавеющей')
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="кастрюля из нержавеющей стали"]')).click()
        browser.all((AppiumBy.ID, 'com.kazanexpress.ke_app:id/title')).element_by(
            have.text('Кастрюля из нержавеющей стали')).click()
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/product_favorite_button')).click()
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Вернуться назад"]')).click()
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/navigation_favorite')).click()

    @allure.step('Проверяем то что в избранном находится 1 товар добавленный нами')
    def should_item_in_favorites(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/title')).should(
            have.text('Кастрюля из нержавеющей стали'))

    @allure.step('Удаляем товар из избранного')
    def delete_item_from_favorites(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/favorite')).click()

    @allure.step('Проверяем то что в избранном нет товаров')
    def should_favorites_empty(self):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Добавьте то, что понравилось"]')).should(
            be.visible)


favorites_page = MobileFavoritesPage()
