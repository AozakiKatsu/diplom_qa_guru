from diplom_qa_guru.utils.request_helper import api_get
from jsonschema import validate

from schemas.get_cities import cities


def test_get_cities():
    url = "/main/cities"
    response = api_get(url)
    assert response.status_code == 200
    assert len(response.json()['payload']) >= 122
    assert response.json()['payload'][0]['name'] == 'Агрыз'
    validate(response.json(), cities)

