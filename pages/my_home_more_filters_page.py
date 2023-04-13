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
        self.junior_button = locators.MoreFiltersLocators.junior_button
        self.message_search_junior_assert = locators.MoreFiltersLocators.message_search_junior_assert
        self.clear_filters_button = locators.MoreFiltersLocators.clear_filters_button
        self.mid_button = locators.MoreFiltersLocators.mid_button
        self.message_search_mid_assert = locators.MoreFiltersLocators.message_search_mid_assert
        self.senior_button = locators.MoreFiltersLocators.senior_button
        self.message_search_senior_assert = locators.MoreFiltersLocators.message_search_senior_assert
        self.all_seniority_button = locators.MoreFiltersLocators.all_seniority_button
        self.show_only_friendly_offers_checkbox = locators.MoreFiltersLocators.show_only_friendly_offers_checkbox
        self.message_offers_ukraine_assert = locators.MoreFiltersLocators.message_offers_ukraine_assert

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

    def button_clear_filters(self):
        self.driver.find_element(*self.another_click_locations_button).click()
        self.driver.find_element(*self.clear_filters_button).click()

    def button_more_filters_seniority_junior(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.junior_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_seniority_mid(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.mid_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_seniority_senior(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.senior_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_seniority_all(self):
        self.driver.find_element(*self.another_click_locations_button).click()
        self.driver.find_element(*self.all_seniority_button).click()
        self.driver.find_element(*self.show_offers_button).click()

    def button_more_filters_checkbox(self):
        self.driver.find_element(*self.more_filters_button).click()
        self.driver.find_element(*self.show_only_friendly_offers_checkbox).click()
        self.driver.find_element(*self.show_offers_button).click()

    def is_message_search_b2b_displayed(self):
        return self.driver.find_element(*self.message_search_b2b_assert).is_displayed()

    def is_message_search_permanent_displayed(self):
        return self.driver.find_element(*self.message_search_permanent_assert).is_displayed()

    def is_message_search_mandate_contract_displayed(self):
        return self.driver.find_element(*self.message_search_mandate_contract_assert).is_displayed()

    def get_message_offers(self):
        return self.driver.find_element(*self.message_offers_assert).text

    def is_message_search_junior_displayed(self):
        return self.driver.find_element(*self.message_search_junior_assert).is_displayed()

    def is_message_search_mid_displayed(self):
        return self.driver.find_element(*self.message_search_mid_assert).is_displayed()

    def is_message_search_senior_displayed(self):
        return self.driver.find_element(*self.message_search_senior_assert).is_displayed()

    def is_message_search_friendly_ukraine_displayed(self):
        return self.driver.find_element(*self.message_offers_ukraine_assert).is_displayed()