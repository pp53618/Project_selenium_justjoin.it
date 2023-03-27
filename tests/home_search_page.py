import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest
from pages.my_home_search_page import MyHomeSearchPage
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestCatalogSearch:

    def test_directory_search(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.button_categories()
        time.sleep(5)

    def test_directory_search(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search()
        msg = 'JavaScript'
        assert msg in my_home_search_page.get_message_js_assert()
        time.sleep(5)