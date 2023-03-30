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

    def test_button_search_php_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_php()
        assert my_button_search_page.is_php_visibility_displayed()
        time.sleep(5)

    def test_button_search_ruby_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_ruby()
        assert my_button_search_page.is_ruby_visibility_displayed()
        time.sleep(5)

    def test_button_search_python_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_python()
        assert my_button_search_page.is_python_visibility_displayed()
        time.sleep(5)

    def test_button_search_java_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_java()
        assert my_button_search_page.is_java_visibility_displayed()
        time.sleep(5)

    def test_button_search_net_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_net()
        assert my_button_search_page.is_net_visibility_displayed()
        time.sleep(5)

    def test_button_search_scala_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_scala()
        assert my_button_search_page.is_scala_visibility_displayed()
        time.sleep(5)

    def test_button_search_c_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_c()
        assert my_button_search_page.is_c_visibility_displayed()
        time.sleep(5)

    def test_button_search_mobile_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_mobile()
        assert my_button_search_page.is_mobile_visibility_displayed()
        time.sleep(5)

    def test_button_search_testing_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_testing()
        assert my_button_search_page.is_testing_visibility_displayed()
        time.sleep(5)

    def test_button_search_devops_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_devops()
        assert my_button_search_page.is_devops_visibility_displayed()
        time.sleep(5)

    def test_button_search_admin_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_admin()
        assert my_button_search_page.is_admin_visibility_displayed()
        time.sleep(5)

    def test_button_search_ux_ui_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_ux_ui()
        assert my_button_search_page.is_ux_ui_visibility_displayed()
        time.sleep(5)

    def test_button_search_pm_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_pm()
        assert my_button_search_page.is_pm_visibility_displayed()
        time.sleep(5)

    def test_button_search_game_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_game()
        assert my_button_search_page.is_game_visibility_displayed()
        time.sleep(5)

    def test_button_search_analytics_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_analytics()
        assert my_button_search_page.is_analytics_visibility_displayed()
        time.sleep(5)

    def test_button_search_security_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_security()
        assert my_button_search_page.is_security_visibility_displayed()
        time.sleep(5)

    def test_button_search_data_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_data()
        assert my_button_search_page.is_data_visibility_displayed()
        time.sleep(5)

    def test_button_search_go_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_go()
        assert my_button_search_page.is_go_visibility_displayed()
        time.sleep(5)

    def test_button_search_support_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_support()
        assert my_button_search_page.is_support_visibility_displayed()
        time.sleep(5)

    def test_button_search_erp_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_erp()
        assert my_button_search_page.is_erp_visibility_displayed()
        time.sleep(5)

    def test_button_search_architecture_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_architecture()
        assert my_button_search_page.is_architecture_visibility_displayed()
        time.sleep(5)

    def test_button_search_other_passed(self):
        my_button_search_page = MyButtonSearchPage(self.driver)
        my_button_search_page.open_page()
        my_button_search_page.button_categories_other()
        assert my_button_search_page.is_other_visibility_displayed()
        time.sleep(5)