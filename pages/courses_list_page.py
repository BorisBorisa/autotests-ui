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

        self.courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id("courses-list-toolbar-create-course-button")

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text(self.COURSE_TITLE)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title=self.EMPTY_VIEW_TITLE,
            description=self.EMPTY_VIEW_DESCRIPTION_TEXT
        )

    def check_visible_create_course_button(self):
        expect(self.create_course_btn).to_be_visible()

    def click_create_course_button(self):
        self.create_course_btn.click()
