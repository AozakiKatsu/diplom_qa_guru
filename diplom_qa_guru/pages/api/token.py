import os
import requests

headers = {"Authorization": "Basic a2F6YW5leHByZXNzLWN1c3RvbWVyOmN1c3RvbWVyU2VjcmV0S2V5"}

json_data = {
    "grant_type": "password",
    "username": '89045372176',
    "password": '1122334455aA',
}


def test_api_token():
    api_request = requests.post(url='https://api.kazanexpress.ru/api/oauth/token/?grant_type=password&username=89045372176&password=1122334455aA', data=json_data, headers=headers)
    return api_request.json()['access_token']
