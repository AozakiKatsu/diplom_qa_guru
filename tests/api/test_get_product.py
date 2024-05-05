from diplom_qa_guru.utils.request_helper import api_get
from jsonschema import validate

from schemas.get_cities import cities
from schemas.get_product import product


def test_get_product():
    url = '/v2/product/1102727'
    response = api_get(url)
    assert response.status_code == 200
    assert response.json()['payload']['data']['id'] == 1102727
    validate(response.json(), product)
