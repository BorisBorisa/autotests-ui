from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    DASHBOARD_TITLE_TEXT = "Dashboard"

    def __init__(self, page: Page):
        self.__dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")

        super().__init__(page)

    def check_visible_dashboard_title(self):
        expect(self.__dashboard_title).to_be_visible()
        expect(self.__dashboard_title).to_have_text(self.DASHBOARD_TITLE_TEXT)
