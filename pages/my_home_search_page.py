from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyHomeSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_home_input = locators.SearchLocators.search_home_input
        self.search_js_category_xpath = locators.SearchLocators.search_js_category_xpath
        self.message_results_search_assert = locators.SearchLocators.message_results_search_assert
        self.search_html_category_xpath = locators.SearchLocators.search_html_category_xpath
        self.search_category_xpath = locators.SearchLocators.search_category_xpath
        self.is_chat_visibility_assert = locators.SearchLocators.is_chat_visibility_assert
        self.message_error_search = locators.SearchLocators.message_error_search
#        self.back_search_button = locators.SearchLocators.back_search_button

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def categories_search_js(self):
        self.driver.find_element(*self.search_home_input).click()
        self.driver.find_element(*self.search_js_category_xpath).click()

    def categories_search_html(self, category):
        self.driver.find_element(*self.search_home_input).send_keys(category)
        self.driver.find_element(*self.search_html_category_xpath).click()

    def categories_search_other(self, category):
        self.driver.find_element(*self.search_home_input).send_keys(category)
        self.driver.find_element(*self.search_category_xpath).click()

    def get_message_results_search_assert(self):
        return self.driver.find_element(*self.message_results_search_assert).text

    def is_chat_visibility_displayed(self):
        return self.driver.find_element(*self.is_chat_visibility_assert).is_displayed()

    def get_message_error_search(self):
        return self.driver.find_element(*self.message_error_search).text
