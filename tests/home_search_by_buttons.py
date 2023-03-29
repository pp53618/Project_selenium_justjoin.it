import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest
from selenium.webdriver.support.select import Select
from pages.my_home_search_button_page import MyButtonSearchPage


@pytest.mark.usefixtures("setup")
class TestButtonSearch:

    def test_button_search_js_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_js()
        assert my_button_search_page.is_js_visibility_displayed()
        time.sleep(5)

    def test_button_search_html_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_html()
        assert my_button_search_page.is_html_visibility_displayed()
        time.sleep(5)