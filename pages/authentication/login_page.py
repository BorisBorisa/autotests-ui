from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent

from playwright.sync_api import Page

import re
import allure

class LoginPage(BasePage):
    WRONG_EMAIL_OR_PASS_ALERT_TEXT = "Wrong email or password"

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.login_button = Button(page, "login-page-login-button", "Login")
        self.registration_link = Link(page, "login-page-registration-link", "Link")
        self.wrong_email_or_password_alert = Text(
            page, "login-page-wrong-email-or-password-alert", "Wrong email or password"
        )

    def click_login_button(self) -> None:
        self.login_button.click()

    def click_registration_link(self) -> None:
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    @allure.step("Check visible wrong email or password alert")
    def check_visible_wrong_email_or_password_alert(self) -> None:
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text(self.WRONG_EMAIL_OR_PASS_ALERT_TEXT)
