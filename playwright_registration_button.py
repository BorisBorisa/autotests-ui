from playwright.sync_api import sync_playwright, expect

EMAIL = "user.name@gmail.com"
USERNAME = "username"
PASSWORD = "password"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")

    expect(registration_button).to_be_disabled()
    email_input.fill(EMAIL)
    username_input.fill(USERNAME)
    password_input.fill(PASSWORD)
    expect(registration_button).to_be_enabled()
