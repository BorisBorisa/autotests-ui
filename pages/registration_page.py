from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        self.__email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        self.__username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        self.__password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        self.__registration_btn = page.get_by_test_id("registration-page-registration-button")
        self.__login_link = page.get_by_test_id("registration-page-login-link")

        super().__init__(page)

    def fill_registration_form(self, email: str, username: str, password: str) -> None:
        self.__email_input.fill(email)
        expect(self.__email_input).to_have_value(email)

        self.__username_input.fill(username)
        expect(self.__username_input).to_have_value(username)

        self.__password_input.fill(password)
        expect(self.__password_input).to_have_value(password)

    def click_registration_button(self) -> None:
        self.__registration_btn.click()

    def click_login_link(self) -> None:
        self.__login_link.click()
