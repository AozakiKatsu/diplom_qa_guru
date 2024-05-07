import allure
import pytest
import allure_commons
from selene import browser, support
import os
from dotenv import load_dotenv

from appium import webdriver

import config
from kazanexpress_project.utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.context_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    if context == 'bstack':
        attach.add_bstack_video(session_id)
