import pytest
import allure
from core.browser import BrowserSession

@pytest.fixture(scope="function")
def browser_session():
    session = BrowserSession()
    session.start()
    yield session
    session.stop()

@pytest.fixture(scope="function")
def page(browser_session):
    return browser_session.page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="Screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
