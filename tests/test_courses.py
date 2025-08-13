import pytest

from playwright.sync_api import expect, Page

COURSE_TITLE = "Courses"
COURSE_LIST_TITLE = "There is no results"
COURSE_LIST_DESCRIPTION_TEXT = "Results from the load test pipeline will be displayed here"
COURSE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"


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
