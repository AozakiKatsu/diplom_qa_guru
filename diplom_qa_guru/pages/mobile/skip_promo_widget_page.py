import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, command


class SkipPromoWidget:
    @allure.step('Пропускаем стартовый виджет')
    def skip_promo_widget(self):
        swipe_element = browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/onboarding_image'))
        time.sleep(5)
        if swipe_element is not None:
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            swipe_element.perform(command.drag_and_drop_by_offset(x=-1200, y=0))
            browser.element((AppiumBy.ID, 'com.kazanexpress.ke_app:id/onboarding_skip_button')).click()
        else:
            browser.element((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]')).click()

        return self


skip_widget = SkipPromoWidget()
