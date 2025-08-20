import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    COURSE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"

    CREATE_COURSE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
    CREATE_COURSE_DEFAULT_DATA = {
        "title": "",
        "estimated_time": "",
        "description": "",
        "max_score": "0",
        "min_score": "0"
    }
    CREATE_COURSE_TEST_DATA = {
        "title": "Playwright",
        "estimated_time": "2 weeks",
        "description": "Playwright",
        "max_score": "100",
        "min_score": "10"
    }
    UPDATE_COURSE_TEST_DATA = {
        "title": "Selenium",
        "estimated_time": "1 weeks",
        "description": "Selenium",
        "max_score": "5",
        "min_score": "1"
    }

    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(self.COURSE_URL)

        courses_list_page.navbar.check_visible(username="username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(self.CREATE_COURSE_URL)

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_page.create_course_from.check_visible(**self.CREATE_COURSE_DEFAULT_DATA)

        create_course_page.exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_from.fill(**self.CREATE_COURSE_TEST_DATA)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title=self.CREATE_COURSE_TEST_DATA["title"],
            max_score=self.CREATE_COURSE_TEST_DATA["max_score"],
            min_score=self.CREATE_COURSE_TEST_DATA["min_score"],
            estimated_time=self.CREATE_COURSE_TEST_DATA["estimated_time"]
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(self.CREATE_COURSE_URL)

        create_course_page.create_course_from.fill(**self.CREATE_COURSE_TEST_DATA)
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title=self.CREATE_COURSE_TEST_DATA["title"],
            max_score=self.CREATE_COURSE_TEST_DATA["max_score"],
            min_score=self.CREATE_COURSE_TEST_DATA["min_score"],
            estimated_time=self.CREATE_COURSE_TEST_DATA["estimated_time"]
        )

        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_from.fill(**self.UPDATE_COURSE_TEST_DATA)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title=self.UPDATE_COURSE_TEST_DATA["title"],
            max_score=self.UPDATE_COURSE_TEST_DATA["max_score"],
            min_score=self.UPDATE_COURSE_TEST_DATA["min_score"],
            estimated_time=self.UPDATE_COURSE_TEST_DATA["estimated_time"]
        )
