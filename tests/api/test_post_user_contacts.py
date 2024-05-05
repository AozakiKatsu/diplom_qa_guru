import json

import allure

from diplom_qa_guru.utils.request_helper import api_post


@allure.parent_suite('API')
@allure.suite('Профиль')
@allure.title(f"Изменение персональных данных")
@allure.severity('Major')
def test_change_user_contacts():
    url = '/user/contacts'
    payload = json.dumps({
        "email": "mail@mail.ru",
        "firstname": "Петр",
        "lastname": "Петров",
        "patronymic": "Петрович",
        "phone": "+7 (904) 537-21-76",
        "sex": "",
        "birthDate": None,
        "accountId": 0
    })
    with allure.step('Выполняем запрос на изменение персоальных данных'):
        response = api_post(url, data=payload)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 200
    with allure.step('Проверяем изменились данные пользователя'):
        assert response.json()['timestamp']
