import json
import logging
import os
import allure
import requests

from dotenv import load_dotenv
from requests import Response
from allure_commons._allure import step
from allure_commons.types import AttachmentType

from diplom_qa_guru.pages.api.token import api_token

load_dotenv()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Authorization": "Bearer " + api_token(),
    "Content-Type": "application/json"}
API_URL = os.getenv('API_URL')


def api_get(url, **kwargs):
    with step("API Request"):
        response = requests.get(url=f"https://{API_URL}{url}", headers=headers, **kwargs)
        response_logging(response)
        response_attaching(response)

    return response


def api_post(url, **kwargs):
    with step("API Request"):
        response = requests.post(url=f"https://{API_URL}{url}", headers=headers, **kwargs)
    response_logging(response)
    response_attaching(response)

    return response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )
    if response.request.body:  # логирование тела запроса если оно есть
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
