import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import random
from pages.my_login_page import MyLoginPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_log_in_complete_passed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        my_login_page.log_in("b.mackiewicz88@wp.pl", "Slonik18")
        msg = "Welcome"
        assert msg in my_login_page.get_message_my_profile()
        time.sleep(5)

    def test_password_change_passed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        my_login_page.password_change("b.mackiewicz88@wp.pl")
        msg = "Reset password"
        assert msg in my_login_page.get_message_resset_password()
        time.sleep(5)

    def test_entering_the_wrong_password_failed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        password = str(random.randint(0, 100000)) + "onik"
        my_login_page.log_in("b.mackiewicz88@wp.pl", password)
        assert my_login_page.is_sing_in_link_assert_displayed()
        time.sleep(5)

    def test_entering_the_wrong_email_failed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        email = str(random.randint(0, 100000)) + "b.mackiewicz88@wp.pl"
        my_login_page.log_in(email, "Slonik18")
        assert my_login_page.is_sing_in_link_assert_displayed()
        time.sleep(5)

    def test_entering_no_data_failed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        my_login_page.log_in_no_data()
        msg = 'Email is a required field'
        assert msg in my_login_page.get_message_email_required()
        msg1 = "Password"
        assert msg1 in my_login_page.get_message_password()
        time.sleep(5)

    def test_entering_no_email_failed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        my_login_page.log_in_no_email("Slonik18")
        msg = 'Email is a required field'
        assert msg in my_login_page.get_message_email_required()
        time.sleep(5)

    def test_entering_no_password_failed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        my_login_page.log_in_no_password("b.mackiewicz88@wp.pl")
        msg = "Password"
        assert msg in my_login_page.get_message_password()
        time.sleep(5)

    def test_checking_hyperlinks_register_passed(self):
        my_login_page = MyLoginPage(self.driver)
        my_login_page.open_page()
        my_login_page.check_register_link()
        assert my_login_page.is_sing_in_link_assert_displayed()
        time.sleep(5)