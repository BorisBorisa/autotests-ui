import pytest

from playwright.sync_api import expect, Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

COURSE_TITLE = "Courses"
COURSE_LIST_TITLE = "There is no results"
COURSE_LIST_DESCRIPTION_TEXT = "Results from the load test pipeline will be displayed here"
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
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(COURSE_URL)

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    courses_list_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    courses_list_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    courses_list_description_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")

    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text(COURSE_TITLE)

    expect(courses_list_icon).to_be_visible()

    expect(courses_list_title).to_be_visible()
    expect(courses_list_title).to_have_text(COURSE_LIST_TITLE)

    expect(courses_list_description_text).to_be_visible()
    expect(courses_list_description_text).to_have_text(COURSE_LIST_DESCRIPTION_TEXT)


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

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title=CREATE_COURSE_TEST_DATA["title"],
        max_score=CREATE_COURSE_TEST_DATA["max_score"],
        min_score=CREATE_COURSE_TEST_DATA["min_score"],
        estimated_time=CREATE_COURSE_TEST_DATA["estimated_time"]
    )
