import pytest

from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page
from typing import Generator

from tools.playwright.pages import initialize_playwright_page
from pages.authentication.registration_page import RegistrationPage
from config import settings

EMAIL = "user.name@gmail.com"
USERNAME = "username"
PASSWORD = "password"
REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(REGISTRATION_URL)

    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_registration_button()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(
        initialize_browser_state,
        request: SubRequest,
        playwright: Playwright
) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )


@pytest.fixture
def chromium_page(
        request: SubRequest,
        playwright: Playwright
) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name
    )
