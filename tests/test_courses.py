import pytest

from playwright.sync_api import sync_playwright, expect

EMAIL = "user.name@gmail.com"
USERNAME = "username"
PASSWORD = "password"

COURSE_TITLE = "Courses"
COURSE_LIST_TITLE = "There is no results"
COURSE_LIST_DESCRIPTION_TEXT = "Results from the load test pipeline will be displayed here"


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        registration_button = page.get_by_test_id("registration-page-registration-button")

        email_input.fill(EMAIL)
        username_input.fill(USERNAME)
        password_input.fill(PASSWORD)
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        courses_list_icon = page.get_by_test_id("courses-list-empty-view-icon")
        courses_list_title = page.get_by_test_id("courses-list-empty-view-title-text")
        courses_list_description_text = page.get_by_test_id("courses-list-empty-view-description-text")

        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text(COURSE_TITLE)

        expect(courses_list_icon).to_be_visible()

        expect(courses_list_title).to_be_visible()
        expect(courses_list_title).to_have_text(COURSE_LIST_TITLE)

        expect(courses_list_description_text).to_be_visible()
        expect(courses_list_description_text).to_have_text(COURSE_LIST_DESCRIPTION_TEXT)
