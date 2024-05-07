import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MobileCatalogPage:
    @allure.step('Поиск товара по категориям каталога')
    def product_search_by_сategory(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/navigation_search')).click()
        browser.all((AppiumBy.ID, 'com.kazanexpress.ke_app:id/category_title')).element_by(have.text('Одежда')).click()
        browser.all((AppiumBy.ID, 'com.kazanexpress.ke_app:id/category_title')).element_by(
            have.text('Спецодежда')).click()
        browser.all((AppiumBy.ID, 'com.kazanexpress.ke_app:id/category_title')).element_by(
            have.text('Медицинская одежда')).click()

        return self

    @allure.step('Проверка результатов поиска')
    def check_search_results(self):
        browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/title')).should(
            have.text('Халат медицинский "Луиза"'))


catalog_page = MobileCatalogPage()
