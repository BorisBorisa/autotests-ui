import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    AUTH_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    TEST_DATA = (
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    )

    REGISTRATION_DATA = {
        "email": "user.name@gmail.com",
        "username": "username",
        "password": "password"
    }

    @pytest.mark.parametrize("email, password", TEST_DATA)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(url=self.AUTH_URL)
        login_page.login_form.fill(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
            login_page: LoginPage
    ):
        registration_page.visit(self.REGISTRATION_URL)
        registration_page.registration_form.fill(**self.REGISTRATION_DATA)
        registration_page.click_registration_button()

        dashboard_page.toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(username=self.REGISTRATION_DATA["username"])
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(
            email=self.REGISTRATION_DATA["email"],
            password=self.REGISTRATION_DATA["password"]
        )
        login_page.click_login_button()

        dashboard_page.toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(username=self.REGISTRATION_DATA["username"])
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(self.AUTH_URL)
        login_page.registration_link.click()

        registration_page.registration_form.check_visible(email="", username="", password="")
