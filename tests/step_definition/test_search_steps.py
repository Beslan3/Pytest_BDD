# fixture is something that all tests (steps) will share
# you will create an object of it: ' def browser(): '
# and it will be shared between all the tests (steps):
# def test_start_home(browser)
# def test_search_web(browser)

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.step_definition.utilities import disable_google_ads
from pytest_bdd import scenarios, given, when, then, parser
from tests.pages.search_page import *
from pytest import mark
import allure
# from tests.step_definition.utilities import create_logger

# CONSTANTS
home_url = "https://www.amazon.com/"

# scenarios
scenarios("../features/search.feature")


# STEPS
@allure.severity("Critical")
@allure.description("validates home page is displayed")
@given("the store home page is displayed")  # this the Given
# scenario from features, should be mapped to this function
def test_start_home(browser):
    print('home page starting..')
    browser.get(home_url)
    disable_google_ads(browser)
    time.sleep(2)


@allure.severity("Critical")
@allure.description("validates the web search")
@when('the user searches for "dress"')  # this conforms to When
# scenario from features, should be mapped to this function
def test_search_web(browser):
    # # element locators:
    print('search is starting')
    search_box = browser.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    search_button = browser.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")

    # # actions with locators:
    search_box.send_keys('iphone')
    search_button.click()
    print('\nDone')


@allure.severity("Critical")
@allure.description("validates products list search result")
@then("at least one product is listed")  # this is Then scenario
# from features, should be mapped to this function
def test_verify_products_list(browser):
    # common elements from the result
    product = browser.find_elements(By.XPATH,
                                    '//div[@class="s-main-slot s-result-list s-search-results sg-row"]//span[@class="a-size-medium a-color-base a-text-normal"]')  # span that has div parent somewhere

    assert len(product) >= 1
    print('\nsearch result verified')
    assert 'iphone' in browser.current_url
    print('\ncurrent url verified')


@allure.severity("low")
@allure.description("validates smoke test")
@pytest.mark.smoke
def login(browser):
    print('home page starting..')
    browser.get(home_url)
    disable_google_ads(browser)
    time.sleep(2)


# log = create_logger('C:\dev\BDD-Project\logs\_search_page.log')
