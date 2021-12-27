import time

import pytest
import allure
from selenium.webdriver.common.keys import Keys


@allure.suite("searching")
@allure.story("test for searching")
def test_search(browser):
    search_string = "scala"

    with allure.step("find" + search_string):
        search_form = pytest.page.getSearchForm()
        search_form.send_keys(search_string)
        search_form.send_keys(Keys.RETURN)

    with allure.step("Checking main label after search"):
        actual_result = pytest.page.getMainSearchLabel().text
        assert search_string in actual_result.lower()


@allure.suite("city")
@allure.story("city in label")
def test_city(browser):

    with allure.step("Checking main label after search"):
        actual_value = pytest.page.getMainSearchLabel().text

        assert "Києві" in actual_value
