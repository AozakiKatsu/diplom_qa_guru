import os

import pytest
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from diplom_qa_guru import utils


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def context_options(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        options.load_capabilities({
            'remote_url': os.getenv('URL_LOCAL'),
            'udid': os.getenv('DEVICE_NAME_EMULATE'),
            'app': utils.file.abs_path_from_project(os.getenv('APP_LOCAL'))
        })

    if context == 'local_real_device':
        options.load_capabilities({
            'remote_url': os.getenv('URL_LOCAL'),
            'udid': os.getenv('DEVICE_NAME_LOCAL'),
            'app': utils.file.abs_path_from_project(os.getenv('APP_LOCAL'))
        })

    if context == 'bstack':
        options.load_capabilities({
            'remote_url': os.getenv('BS_URL'),
            'deviceName': os.getenv('BS_DEVICE'),
            'platformName': os.getenv('PLATFORM_NAME'),
            'platformVersion': os.getenv('PLATFORM_VERSION_BS'),
            'app': os.getenv('APP')
        })
        options.load_capabilities({
            'bstack:options': {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('BS_LOGIN'),
                'accessKey': os.getenv('BS_KEY'),
            }, }
        )

    return options
