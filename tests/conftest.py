from selene import browser
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from scripts.file_system_operations import TMP_DIR
from utils import attach


DEFAULT_BROWSER_VERSION = "126.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
        keep_alive=True
    )

    browser.config.driver = driver

    driver_options = webdriver.ChromeOptions()

    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    driver_options.add_experimental_option("prefs", prefs)

    browser.config.window_width = 1280
    browser.config.window_height = 724

    browser.config.base_url = 'https://www.cft.ru/'

    yield driver

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    driver.quit()


# @pytest.fixture(scope='session', autouse=True)
# def open_url():
#     driver_options = webdriver.ChromeOptions()
#
#     prefs = {
#                 "download.default_directory": TMP_DIR,
#                 "download.prompt_for_download": False,
#                 "download.directory_upgrade": True,
#                 "safebrowsing.enabled": True
#             }
#     driver_options.add_experimental_option("prefs", prefs)
#
#     driver_options.page_load_strategy = 'eager'
#     driver_options.add_argument('--window-size=1280,724')
#     browser.config.driver_options = driver_options
#
#     browser.config.base_url = 'https://www.cft.ru/'
#
#     yield
#
#     browser.quit()
