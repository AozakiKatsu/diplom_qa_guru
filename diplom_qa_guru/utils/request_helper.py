import json
import logging
import os

from requests import Response
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
API_URL = "api.kazanexpress.ru/api"


def request_api_get(url, **kwargs):
    with step("API Request"):
        result = requests.get(url=f"https://{API_URL}{url}", headers=headers, **kwargs)
        response_logging(result)  # логирование запроса и ответа (пример реализации ниже)
        response_attaching(result)  # добавление аттачей( пример реализации ниже )
    return result


#
#
def request_api_post(url, **kwargs):
    with step("API Request"):
        result = requests.get(url="https://api.kazanexpress.ru/" + url, **kwargs)
        response_logging(result)  # логирование запроса и ответа (пример реализации ниже)
        response_attaching(result)  # добавление аттачей( пример реализации ниже )
    return result


#
def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)  # логирование тела запроса если оно есть
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:  # логирование тела запроса если оно есть
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
