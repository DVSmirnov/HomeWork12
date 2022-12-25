import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import datetime
import logging
import allure
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests in")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")
    parser.addoption("--base_url", default="http://192.168.48.1:8081", help="Base URL")
    parser.addoption("--log_level", action="store", default="WARNING",
                     help="Log level: DEBUG, INFO, WARNING, ERROR or CRITICAL")
    parser.addoption("--executor", default="http://192.168.48.1:4444/wd/hub", help="Enter correct Selenoid url")
    parser.addoption("--remote", action="store_true", help="Enter '--remote' for remote test execute")
    parser.addoption("--bv")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    remote = request.config.getoption("--remote")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    log_file = f"logs_{datetime.datetime.now().date()}.log"
    logger = logging.getLogger(request.node.name)
    if not os.path.exists("logs/"):
        os.makedirs("logs/")

    file_handler = logging.FileHandler(f"logs/{log_file}")
    file_handler.setFormatter(logging.Formatter('%(asctime)s  %(levelname)s  %(name)s: %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("========== The test has started ==========")

    options = None
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
    elif browser_name in ['edge', 'MicrosoftEdge']:
        options = webdriver.EdgeOptions()

    if remote:
        capabilities = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }

        driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=capabilities,
            options=options,
        )
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        elif browser_name in ["edge", "MicrosoftEdge"]:
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
        else:
            raise ValueError(f"Browser {browser_name} isn't supported")

    driver.base_url = base_url
    driver.maximize_window()
    driver.log_level = log_level
    driver.logger = logger

    with allure.step(f"Open browser: {browser_name}"):
        yield driver

    with allure.step("Closing browser"):
        driver.close()
        logger.info("========== The test is over ==========\n")
