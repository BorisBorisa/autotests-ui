import pytest
import allure

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    EMAIL = "user.name@gmail.com"
    USERNAME = "username"
    PASSWORD = "password"

    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(url=self.REGISTRATION_URL)
        registration_page.registration_form.fill(email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD)
        registration_page.click_registration_button()
        dashboard_page.toolbar_view.check_visible()
