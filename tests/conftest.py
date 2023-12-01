# the purpose of conftest is fixture's
# code reusability: all the steps in the fixture's
# function will be passed to our test files with just
# the passing the name of this function (browser)

import pytest
from selenium import webdriver
import time
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from tests.step_definition.utilities import *
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from selenium.common import NoSuchElementException, TimeoutException



from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONSTANTS
# home_url = "https://www.amazon.com/"

# fixture
@pytest.fixture(scope="module") # purpose of fixture (BDD):
# the browser() function under this fixture
# can be used in all our test files when you pass the name
# of the function under this fixture,
# in this case 'browser' to our test functions
# so 'browser' here defines our browser:
# driver = webdriver.Chrome, implicitly_wait, sleep etc.
# so engineer can reuse this code in every test with
# just passing the name: 'browser'

def browser():

    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chr_options)

    # driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(3)
    print('browser opened')
    yield driver
    print('\nbrowser closing..')
    driver.quit()

@pytest.fixture(scope='session')
def quit_browser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chr_options)
    yield driver
    driver.quit()
