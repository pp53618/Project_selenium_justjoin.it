from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyMoreFiltersButton:

    def __init__(self, driver):
        self.driver = driver
        self.more_filters_button = locators.MoreFiltersLocators.more_filters_button
        self.b2b_button = locators.MoreFiltersLocators.b2b_button
        self.show_offers_button = locators.MoreFiltersLocators.show_offers_button
        self.message_search_b2b_assert = locators.MoreFiltersLocators.message_search_b2b_assert
        self.permanent_button = locators.MoreFiltersLocators.permanent_button
        self.message_search_permanent_assert = locators.MoreFiltersLocators.message_search_permanent_assert
        self.mandate_contract_button = locators.MoreFiltersLocators.mandate_contract_button
        self.message_search_mandate_contract_assert = locators.MoreFiltersLocators.message_search_mandate_contract_assert
        self.all_button = locators.MoreFiltersLocators.all_button
        self.another_click_locations_button = locators.MoreFiltersLocators.another_click_locations_button
        self.message_offers_assert = locators.CitySelectionLocators.message_offers_assert

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def button_more_filters_employment_type_b2b(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.b2b_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_employment_type_permanent(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.permanent_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_employment_type_mandate_contract(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.mandate_contract_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_employment_type_all(self):
        self.driver.find_element(*self.another_click_locations_button).click()
        self.driver.find_element(*self.all_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def is_message_search_b2b_displayed(self):
        return self.driver.find_element(*self.message_search_b2b_assert).is_displayed()

    def is_message_search_permanent_displayed(self):
        return self.driver.find_element(*self.message_search_permanent_assert).is_displayed()

    def is_message_search_mandate_contract_displayed(self):
        return self.driver.find_element(*self.message_search_mandate_contract_assert).is_displayed()

    def get_message_offers(self):
        return self.driver.find_element(*self.message_offers_assert).text