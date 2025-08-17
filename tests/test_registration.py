from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

import pytest

REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
EMAIL = "user.name@gmail.com"
USERNAME = "username"
PASSWORD = "password"


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit(url=REGISTRATION_URL)
    registration_page.registration_form.fill(email=EMAIL, username=USERNAME, password=PASSWORD)
    registration_page.click_registration_button()
    dashboard_page.toolbar_view.check_visible()
