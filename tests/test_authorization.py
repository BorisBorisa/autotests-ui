from pages.login_page import LoginPage

import pytest

AUTH_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
TEST_DATA = (
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
)


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", TEST_DATA)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit(url=AUTH_URL)
    login_page.login_form.fill(email, password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
