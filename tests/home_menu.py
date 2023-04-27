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
        assert my_menu_page.is_breakfast_with_programming_displayed()
        time.sleep(5)

    def test_hyperlink_for_junior_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_for_junior()
        msg = "OD JUNIORA DO SENIORA"
        assert msg in my_menu_page.get_message_for_junior()
        time.sleep(5)

    def test_hyperlink_ambassador_program_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_ambassador_program()
        msg = "Zostań Ambasadorem"
        assert msg in my_menu_page.get_message_ambassador_program()
        time.sleep(5)

    def test_hyperlink_it_index_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_it_index()
        msg = "Wspólnie jesteśmy w stanie stworzyć pierwszy barometr polskiej branży IT"
        assert msg in my_menu_page.get_message_it_index()
        time.sleep(5)

    def test_hyperlink_event_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_event()
        msg = "IDEA"
        assert msg in my_menu_page.get_message_event()
        time.sleep(5)

    def test_hyperlink_just_join_games_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_just_join_games()
        assert my_menu_page.is_just_join_games_displayed()
        time.sleep(5)

    def test_hyperlink_press_room_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_press_room()
        msg = "Bądź na bieżąco!"
        assert msg in my_menu_page.get_message_press_room()
        time.sleep(5)

    def test_hyperlink_reports_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_reports()
        msg = "Raport "
        assert msg in my_menu_page.get_message_reports()
        time.sleep(5)

    def test_hyperlink_careers_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_careers()
        msg = "Just Join IT"
        assert msg in my_menu_page.get_message_careers()
        time.sleep(5)


@pytest.mark.usefixtures("setup")
class TestMenuButton2:

    def test_hyperlink_rss_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_rss()
        time.sleep(5)

    def test_hyperlink_chat_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_help()
        assert my_menu_page.is_chat_displayed()
        time.sleep(5)

    def test_hyperlink_terms_clients_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_terms()
        msg = "Terms - Clients"
        assert msg in my_menu_page.get_message_terms_clients()
        time.sleep(5)


@pytest.mark.usefixtures("setup")
class TestMenuLoginButton:

    def test_menu_sign_in_and_log_in_incorrect_password_passed(self):
        my_menu_page = MyMenuButton(self.driver)
        my_menu_page.open_page()
        my_menu_page.button_sign_in("b.mackiewicz88@wp.pl", "Slonik18")
        msg = "Invalid Email or password."
        assert msg in my_menu_page.get_message_invalid_email_or_password()
        time.sleep(5)