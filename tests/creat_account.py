import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest
from pages.my_register_page import MyRegisterPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_no_email_entry_failed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_no_date()
        msg = 'Email is a required field'
        assert msg in my_register_page.get_message_email_required()
        time.sleep(5)

    def test_create_account_enter_email_no_confirmation_regulations_failed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        email = str(random.randint(0, 1000000)) + "b.mackiewicz88@wp.pl"
        my_register_page.create_account_email_only(email)
        assert my_register_page.is_register_link_assert_displayed()
        time.sleep(5)

    def test_create_account_no_email_entry_with_acceptance_regulations_failed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_accept_terms_only()
        msg = 'Email is a required field'
        assert msg in my_register_page.get_message_email_required()
        time.sleep(5)

    def test_create_account_enter_email_with_acceptance_regulations_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        email = str(random.randint(0, 1000000)) + "b.mackiewicz88@wp.pl"
        my_register_page.create_account_complete(email)
        msg = 'Get started for free'
        assert msg in my_register_page.get_message_get_started()
        time.sleep(5)

    def test_create_account_with_valid_data_re_living_failed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_complete("b.mackiewicz88@wp.pl")
        msg = 'Already have an account? Sign in'
        assert msg in my_register_page.get_message_already_have_account()
        time.sleep(5)

    def test_create_account_entering_incorrect_data_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_complete("b.mackiewicz@rbhdsegxv.pl")
        msg = 'Get started for free'
        assert msg in my_register_page.get_message_get_started()
        time.sleep(5)

    def test_create_account_by_entering_special_characters_failed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_complete("b.mackiewicz@rb*&hdsegv.pl")
        msg = 'Email must be a valid email'
        assert msg in my_register_page.get_message_valid_email()
        time.sleep(5)

    def test_create_account_with_numbers_in_the_name_failed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_complete("646377")
        msg = 'Email must be a valid email'
        assert msg in my_register_page.get_message_valid_email()
        time.sleep(5)

    def test_create_account_using_uppercase_and_lowercase_letters_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_complete("b.MaxckiewiCZR88R@Wp.pl")
        msg = 'Get started for free'
        assert msg in my_register_page.get_message_get_started()
        time.sleep(5)

    def test_create_account_using_more_than_32_characters_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        email = str(random.randint(0, 100000000000000000000000)) + "@wdfdsfsfsffsfsfsfp.pl"
        my_register_page.create_account_complete(email)
        msg = 'Get started for free'
        assert msg in my_register_page.get_message_get_started()
        time.sleep(5)

    def test_create_account_using_less_than_6_characters_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        email = str(random.randint(0, 10)) + "@s.p"
        my_register_page.create_account_complete(email)
        msg = 'Get started for free'
        assert msg in my_register_page.get_message_get_started()
        time.sleep(5)

    def test_checking_the_correctness_of_linked_documents_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.check_terms_link()
        msg = 'Terms - Clients'
        assert msg in my_register_page.get_message_terms_clients()
        time.sleep(5)

    def test_checking_hyperlinks_sing_in_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.check_sing_in_link()
        assert my_register_page.is_sing_in_link_assert_displayed()
        time.sleep(5)

    def test_checking_hyperlinks_forgot_password_passed(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.check_forgot_password_link()
        msg = 'Reset password'
        assert msg in my_register_page.get_message_reset_password()
        time.sleep(5)


@pytest.mark.usefixtures("setup")
class TestCreateAccountByOtherPlatform:

    def test_create_account_by_fb(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_by_fb("b.mackiewicz88@wp.pl", "Slonik18")
        assert my_register_page.get_message_facebook()
        time.sleep(5)

    def test_create_account_by_google(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_by_google("b.mackiewicz88@wp.pl")
        msg = "Informacje o programiście"
        assert msg in my_register_page.get_message_google()
        time.sleep(5)

    def test_create_account_by_github(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_by_github("b.mackiewicz88@wp.pl", "slonik1819")
        msg = "Authorize just-join-it"
        assert msg in my_register_page.get_message_github()
        time.sleep(5)

    def test_create_account_by_linked(self):
        my_register_page = MyRegisterPage(self.driver)
        my_register_page.open_page()
        my_register_page.create_account_by_linkedin("b.mackiewicz88@wp.pl", "slonik1819")
        msg = "LinkedIn"
        assert msg in my_register_page.get_message_linkedin()
        time.sleep(5)