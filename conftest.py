import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Язык интерфейса для браузера, например: es, fr, ru",
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    # Chrome передаёт этот язык сайту в заголовке Accept-Language.
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    print(f"\nstart chrome browser for test, language: {user_language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
