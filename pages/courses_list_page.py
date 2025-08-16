from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.course_view_component import CourseViewComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    COURSE_TITLE = "Courses"
    EMPTY_VIEW_TITLE = "There is no results"
    EMPTY_VIEW_DESCRIPTION_TEXT = "Results from the load test pipeline will be displayed here"

    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.empty_view = EmptyViewComponent(page, "courses-list")
        self.course_view = CourseViewComponent(page)

        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title=self.EMPTY_VIEW_TITLE,
            description=self.EMPTY_VIEW_DESCRIPTION_TEXT
        )
