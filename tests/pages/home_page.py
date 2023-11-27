import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class HeaderPanel():


    def __init__(self, browser):
        self.browser = browser
        self.search_box = browser.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
        self.search_button = browser.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
        self.product = browser.find_elements(By.XPATH,
                                        '//div[@class="s-main-slot s-result-list s-search-results `sg-row"]//span[@class="a-size-medium a-color-base a-text-normal"]')

        print(self.search_box)

    def get_product_count(self, products):
        return len(products)
