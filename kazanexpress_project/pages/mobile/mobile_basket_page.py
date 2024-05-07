import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MobileBasketPage:
    @allure.step('Находим и добавляем товар в корзину')
    def add_item_to_basket(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/search_bar')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).set('Кастрюля из нержавеющей')
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="кастрюля из нержавеющей стали"]')).click()
        browser.all((AppiumBy.ID, 'com.kazanexpress.ke_app:id/title')).element_by(
            have.text('Кастрюля из нержавеющей стали')).click()
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/add_to_cart_button')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="2 литра"]')).click()
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/add_to_cart_button')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Перейти"]')).click()

        return self

    @allure.step('Проверяем то что в корзине находится 1 товар добавленный нами')
    def should_item_in_basket(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/cart_title')).should(
            have.text('Кастрюля из нержавеющей стали'))

        return self

    @allure.step('Удаляем товар из корзины')
    def delete_item_from_basket(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/cart_more')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Удалить"]')).click()

        return self

    @allure.step('Проверяем то что в корзине нет товаров')
    def should_basket_empty(self):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="В корзине пока нет товаров"]')).should(
            be.visible)

        return self


basket_page = MobileBasketPage()
