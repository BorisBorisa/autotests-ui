from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent

from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_btn = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def click_registration_button(self) -> None:
        self.registration_btn.click()

    def click_login_link(self) -> None:
        self.login_link.click()
