import os

import allure
import pytest
from selene import browser
from utils import desktop_attach_allure
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_settings_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 30

    with allure.step(
            'Настраиваем драйвер на сбор логов в удаленной сессии "selenoid" для параметризованного автотеста'):
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:loggingPrefs'] = {
            'performance': 'ALL',
            'browser': 'ALL'
        }

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        }
    }

    # Объединяем capabilities
    options.capabilities.update(capabilities)
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield

    desktop_attach_allure.add_screenshot(browser)
    desktop_attach_allure.add_logs(browser)
    desktop_attach_allure.add_html(browser)
    desktop_attach_allure.add_video(browser)

    browser.quit()
