from playwright.sync_api import expect, Playwright

import pytest

AUTH_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
WRONG_EMAIL_OR_PASS_ALERT_TEXT = "Wrong email or password"
TEST_DATA = (
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
)


@pytest.mark.parametrize("email, password", TEST_DATA)
def test_wrong_email_or_password_authorization(email: str, password: str, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AUTH_URL)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    login_button = page.get_by_test_id('login-page-login-button')
    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    email_input.fill(email)
    password_input.fill(password)
    login_button.click()

    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text(WRONG_EMAIL_OR_PASS_ALERT_TEXT)
