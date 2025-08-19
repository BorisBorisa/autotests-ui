import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    EMAIL = "user.name@gmail.com"
    USERNAME = "username"
    PASSWORD = "password"

    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(url=self.REGISTRATION_URL)
        registration_page.registration_form.fill(email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD)
        registration_page.click_registration_button()
        dashboard_page.toolbar_view.check_visible()
