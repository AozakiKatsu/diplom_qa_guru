import allure

from diplom_qa_guru.pages.mobile.mobile_favorites_page import favorites_page
from diplom_qa_guru.pages.mobile.skip_promo_widget_page import skip_widget


@allure.parent_suite('Mobile')
@allure.suite('Избранное')
@allure.title(f'Удаление из избранного')
@allure.severity('Critical')
def test_delete_from_favorites_mobile():
    skip_widget.skip_promo_widget()

    favorites_page.add_item_to_favorites()
    favorites_page.delete_item_from_favorites()

    favorites_page.should_favorites_empty()