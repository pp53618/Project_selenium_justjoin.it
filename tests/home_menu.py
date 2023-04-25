import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support.select import Select
from pages.my_home_menu_page import MyMenuButton



@pytest.mark.usefixtures("setup")
class TestMenuButton:

    def test_hyperlink_programmer_100k_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_menu_programmer_100k()
        msg = "programista100k@justjoin.it"
        assert msg in my_menu_page.get_message_programmer_100k()
        time.sleep(5)

    def test_hyperlink_breakfast_with_programming_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_menu_breakfast_with_programming()
        assert my_menu_page.is_message_breakfast_with_programming_displayed()
        time.sleep(5)

    def test_hyperlink_for_junoior_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_for_junior()
        msg = "OD JUNIORA DO SENIORA"
        assert msg in my_menu_page.get_message_for_junior()
        time.sleep(5)