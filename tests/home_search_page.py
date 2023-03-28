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

    def test_directory_search_js(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_js()
        msg = 'JavaScript'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_html(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_html(' HTML')
        msg = 'HTML'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_php(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' PHP')
        msg = 'PHP'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_ruby(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Ruby')
        msg = 'Ruby'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_python(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Python')
        msg = 'Python'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_java(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Java')
        msg = 'Java'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_scala(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Scala')
        msg = 'Scala'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_c(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' C')
        msg = 'C'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_mobile(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Mobile')
        msg = 'Mobile'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_testing(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Testing')
        msg = 'Testing'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_devops(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' DevOps')
        msg = 'DevOps'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_admin(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Admin')
        msg = 'Admin'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_pm(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' PM')
        msg = 'PM'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_game(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Game')
        msg = 'Game'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_analytics(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Analytics')
        msg = 'Analytics'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_security(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Security')
        msg = 'Security'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_data(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Data')
        msg = 'Data'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_support(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Support')
        msg = 'Support'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_erp(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' ERP')
        msg = 'ERP'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

