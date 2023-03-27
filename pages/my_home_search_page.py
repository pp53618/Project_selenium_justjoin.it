from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyHomeSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_home_input = locators.SearchLocators.search_home_input
        self.js_button = locators.SearchLocators.js_button
        self.search_js_category_span = locators.SearchLocators.search_js_category_span
        self.message_js_assert = locators.SearchLocators.message_js_assert

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def button_categories(self):
        self.driver.find_element(*self.js_button).click()

    def categories_search(self):
        self.driver.find_element(*self.search_home_input).click()
        self.driver.find_element(*self.search_js_category_span).click()

    def get_message_js_assert(self):
        return self.driver.find_element(*self.message_js_assert).text
