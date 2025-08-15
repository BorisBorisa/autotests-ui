from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    WRONG_EMAIL_OR_PASS_ALERT_TEXT = "Wrong email or password"

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("login-form-email-input").locator("input")
        self.password_input = page.get_by_test_id("login-form-password-input").locator("input")
        self.logint_btn = page.get_by_test_id("login-page-login-button")
        self.registration_link = page.get_by_test_id("login-page-registration-link")
        self.wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")

    def fill_login_form(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self) -> None:
        self.logint_btn.click()

    def click_registration_link(self) -> None:
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self) -> None:
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text(self.WRONG_EMAIL_OR_PASS_ALERT_TEXT)
