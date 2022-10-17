import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose lanuage: ru or es")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")
    if language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart russian language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart espaniol language for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or es")
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()