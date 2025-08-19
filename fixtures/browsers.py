import pytest

from playwright.sync_api import Playwright, Page
from typing import Generator

from pages.authentication.registration_page import RegistrationPage

EMAIL = "user.name@gmail.com"
USERNAME = "username"
PASSWORD = "password"
REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(REGISTRATION_URL)

    registration_page.registration_form.fill(
        email=EMAIL,
        username=USERNAME,
        password=PASSWORD
    )
    registration_page.click_registration_button()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
