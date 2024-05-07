import json

import allure

from kazanexpress_project.utils.request_helper import api_post


@allure.parent_suite('API')
@allure.suite('Избранное')
@allure.title(f"Удаление товара из избранного")
@allure.severity('Major')
def test_post_add_to_favorites():
    url = "/favorites/add"
    data = json.dumps({
        "productId":
            1299225
    })
    url_remove = "/favorites/remove"
    with allure.step('Выполняем запрос на добавление товара в избранное'):
        api_post(url, data=data)
    with allure.step('Удаляем товар из избранного'):
        response = api_post(url=url_remove, data=data)

    with allure.step('Проверяем удалился ли товар из избранного'):
        assert response.json()['timestamp']
        assert response.status_code == 200
