from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyButtonSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.js_button = locators.ButtonLocators.js_button
        self.is_js_visibility_assert = locators.ButtonLocators.is_js_visibility_assert
        self.html_button = locators.ButtonLocators.html_button
        self.is_html_visibility_assert = locators.ButtonLocators.is_html_visibility_assert
        self.php_button = locators.ButtonLocators.php_button
        self.is_php_visibility_assert = locators.ButtonLocators.is_php_visibility_assert

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def button_categories_js(self):
        self.driver.find_element(*self.js_button).click()

    def button_categories_html(self):
        self.driver.find_element(*self.html_button).click()

    def is_js_visibility_displayed(self):
        return self.driver.find_element(*self.is_js_visibility_assert).is_displayed()

    def is_html_visibility_displayed(self):
        return self.driver.find_element(*self.is_html_visibility_assert).is_displayed()