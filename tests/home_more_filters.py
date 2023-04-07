import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support.select import Select
from pages.my_home_more_filters_page import MyMoreFiltersButton


@pytest.mark.usefixtures("setup")
class TestMoreFiltersEmploymentTypeButton:

    def test_choice_of_form_of_employment_b2b_passed(self):
        my_more_filters_page = MyMoreFiltersButton(self.driver)
        my_more_filters_page.open_page()
        my_more_filters_page.button_more_filters_employment_type_b2b()
        assert my_more_filters_page.is_message_search_b2b_displayed()
        time.sleep(5)

    def test_choice_of_form_of_employment_permanent_passed(self):
        my_more_filters_page = MyMoreFiltersButton(self.driver)
        my_more_filters_page.open_page()
        my_more_filters_page.button_more_filters_employment_type_permanent()
        assert my_more_filters_page.is_message_search_permanent_displayed()
        time.sleep(5)

    def test_choice_of_form_of_employment_mandate_contract_passed(self):
        my_more_filters_page = MyMoreFiltersButton(self.driver)
        my_more_filters_page.open_page()
        my_more_filters_page.button_more_filters_employment_type_mandate_contract()
        assert my_more_filters_page.is_message_search_mandate_contract_displayed()
        time.sleep(5)

    def test_choice_of_form_of_employment_all_passed(self):
        my_more_filters_page = MyMoreFiltersButton(self.driver)
        my_more_filters_page.open_page()
        my_more_filters_page.button_more_filters_employment_type_mandate_contract()
        my_more_filters_page.button_more_filters_employment_type_all()
        msg = "Offers with salary"
        assert msg in my_more_filters_page.get_message_offers()
        time.sleep(5)


#@pytest.mark.usefixtures("setup")
#class TestMoreFiltersSeniorityButton: