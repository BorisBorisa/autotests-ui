import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

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


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(COURSE_URL)

    courses_list_page.navbar.check_visible(username="username")
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()

    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit(CREATE_COURSE_URL)

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()

    create_course_page.check_visible_create_course_form(**CREATE_COURSE_DEFAULT_DATA)

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()

    create_course_page.fill_create_course_form(**CREATE_COURSE_TEST_DATA)

    create_course_page.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title=CREATE_COURSE_TEST_DATA["title"],
        max_score=CREATE_COURSE_TEST_DATA["max_score"],
        min_score=CREATE_COURSE_TEST_DATA["min_score"],
        estimated_time=CREATE_COURSE_TEST_DATA["estimated_time"]
    )
