from pages.dashboard_page import DashboardPage

import pytest

DASHBOARD_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit(DASHBOARD_URL)

    dashboard_page_with_state.navbar.check_visible(username="username")
    dashboard_page_with_state.sidebar.check_visible()

    dashboard_page_with_state.check_visible_dashboard_title()
    dashboard_page_with_state.check_visible_scores_chart()
    dashboard_page_with_state.check_visible_courses_chart()
    dashboard_page_with_state.check_visible_students_chart()
    dashboard_page_with_state.check_visible_activities_chart()
