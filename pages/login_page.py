from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    WRONG_EMAIL_OR_PASS_ALERT_TEXT = "Wrong email or password"

    def __init__(self, page: Page):
        self.__email_input = page.get_by_test_id("login-form-email-input").locator("input")
        self.__password_input = page.get_by_test_id("login-form-password-input").locator("input")
        self.__logint_btn = page.get_by_test_id("login-page-login-button")
        self.__registration_link = page.get_by_test_id("login-page-registration-link")
        self.__wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")

        super().__init__(page)

    def fill_login_form(self, email: str, password: str) -> None:
        self.__email_input.fill(email)
        expect(self.__email_input).to_have_value(email)

        self.__password_input.fill(password)
        expect(self.__password_input).to_have_value(password)

    def click_login_button(self) -> None:
        self.__logint_btn.click()

    def click_registration_link(self) -> None:
        self.__registration_link.click()

    def check_visible_wrong_email_or_password_alert(self) -> None:
        expect(self.__wrong_email_or_password_alert).to_be_visible()
        expect(self.__wrong_email_or_password_alert).to_have_text(self.WRONG_EMAIL_OR_PASS_ALERT_TEXT)
