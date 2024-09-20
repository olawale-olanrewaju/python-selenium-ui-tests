import json
import pytest

from selenium.webdriver import Chrome

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    if "browser" not in config:
        raise Exception('The config file does not contain the key "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    else:
        return config["browser"]

@pytest.fixture(scope='session')
def config_wait_time(config):
    return config["wait_time"] if "wait_time" in config else DEFAULT_WAIT_TIME

@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome()

    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()