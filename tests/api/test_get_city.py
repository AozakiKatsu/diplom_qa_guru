import allure

from diplom_qa_guru.utils.request_helper import api_get
from jsonschema import validate

from schemas.get_cities import cities


@allure.parent_suite('API')
@allure.suite('Доставка')
@allure.title(f"Получение списка городов")
@allure.severity('Major')
def test_get_cities():
    url = "/main/cities"
    with allure.step('Выполняем запрос на получение списка городов'):
        response = api_get(url)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 200
    with allure.step('Проверяем количество городов в выдаче'):
        assert len(response.json()['payload']) >= 122
    with allure.step('Проверяем, что первый город в выдаче Агрыз'):
        assert response.json()['payload'][0]['name'] == 'Агрыз'
    with allure.step('Проверяем соответствие схеме'):
        validate(response.json(), cities)
