import allure

from diplom_qa_guru.utils.request_helper import api_get
from jsonschema import validate

from schemas.get_product import product


@allure.parent_suite('API')
@allure.suite('Карточка товара')
@allure.title(f"Работа запроса /product/id")
@allure.severity('Critical')
def test_get_product():
    url = '/v2/product/1102727'
    with allure.step('Выполняем запрос на получение карточки товара'):
        response = api_get(url)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 200
    with allure.step('Проверяем соответствует ли id товара запросу'):
        assert response.json()['payload']['data']['id'] == 1102727
    with allure.step('Проверяем соответствет ли схеме ответа'):
        validate(response.json(), product)
