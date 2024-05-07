import allure

from tests_kazanexpress.pages.mobile.mobile_catalog_page import catalog_page
from tests_kazanexpress.pages.mobile.skip_promo_widget_page import skip_widget


@allure.parent_suite('Mobile')
@allure.suite('Каталог')
@allure.title(f'Поиск товара в категории')
@allure.severity('Major')
def test_catalog_mobile():
    skip_widget.skip_promo_widget()

    catalog_page.product_search_by_сategory()

    catalog_page.check_search_results()
