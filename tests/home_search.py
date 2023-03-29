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

    def test_directory_search_js_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_js()
        msg = 'JavaScript'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_html_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_html(' HTML')
        msg = 'HTML'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_php_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' PHP')
        msg = 'PHP'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_ruby_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Ruby')
        msg = 'Ruby'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_python_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Python')
        msg = 'Python'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_java_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Java')
        msg = 'Java'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_scala_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Scala')
        msg = 'Scala'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_c_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' C')
        msg = 'C'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_mobile_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Mobile')
        msg = 'Mobile'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_testing_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Testing')
        msg = 'Testing'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_devops_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' DevOps')
        msg = 'DevOps'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_admin_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Admin')
        msg = 'Admin'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_pm_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' PM')
        msg = 'PM'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_game_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Game')
        msg = 'Game'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_analytics_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Analytics')
        msg = 'Analytics'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_security_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Security')
        msg = 'Security'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_data_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Data')
        msg = 'Data'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_support_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' Support')
        msg = 'Support'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_erp_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' ERP')
        msg = 'ERP'
        assert msg in my_home_search_page.get_message_results_search_assert()
        time.sleep(5)

    def test_directory_search_entering_special_characters_failed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' ERP#$%)*')
        assert my_home_search_page.is_chat_visibility_displayed()
        time.sleep(5)

    def test_directory_search_entering_numbers_only_passed(self):
        my_home_search_page = MyHomeSearchPage(self.driver)
        my_home_search_page.open_page()
        my_home_search_page.categories_search_other(' 45647880')
        msg = 'Sorry, there are no job offers for:'
        assert msg in my_home_search_page.get_message_error_search()
        time.sleep(5)


