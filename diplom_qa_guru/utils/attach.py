import os

import allure
import requests
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    selenoid_url = os.getenv("SELENOID_URL")
    video_url = f"https://{selenoid_url}/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def add_xml(browser):
    xml = browser.driver.page_source
    allure.attach(xml, name='screen xml dump', attachment_type=allure.attachment_type.XML)


def add_bstack_video(session_id):
    bs_login = os.getenv("BS_LOGIN")
    bs_key = os.getenv("BS_KEY")
    bs_url_api = os.getenv("BS_URL_API")

    bstack_session = requests.get(
        f'{bs_url_api}{session_id}.json',
        auth=(bs_login, bs_key),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
