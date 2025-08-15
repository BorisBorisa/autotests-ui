from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        self.username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        self.password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        self.registration_btn = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def fill_registration_form(self, email: str, username: str, password: str) -> None:
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self) -> None:
        self.registration_btn.click()

    def click_login_link(self) -> None:
        self.login_link.click()
