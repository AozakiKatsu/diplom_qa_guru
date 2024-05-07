import json

import allure

from tests_kazanexpress.utils.request_helper import api_post


@allure.parent_suite('API')
@allure.suite('Избранное')
@allure.title(f"Добавление товара в избранное")
@allure.severity('Major')
def test_post_add_to_favorites():
    url = "/favorites/add"
    data = json.dumps({
        "productId":
            1299225
    })
    url_remove = "/favorites/remove"
    with allure.step('Выполняем запрос на добавление товара в избранное'):
        response = api_post(url, data=data)
    with allure.step('Проверяем добавился ли товар в избранное'):
        assert response.status_code == 200
        assert response.json()['timestamp']
    with allure.step('Удаляем товар из избранного, чистим за собой'):
        api_post(url=url_remove, data=data)
