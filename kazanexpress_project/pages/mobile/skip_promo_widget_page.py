import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, command


class SkipPromoWidget:
    @allure.step('Пропускаем стартовый виджет')
    def skip_promo_widget(self):
        swipe_element = browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/onboarding_image'))
        time.sleep(5)
        try:
            swipe_element()
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/onboarding_skip_button')).click()
        except:
            browser.element((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]')).click()


skip_widget = SkipPromoWidget()
