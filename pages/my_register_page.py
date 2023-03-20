from locators import locators
from selenium.webdriver.common.by import By


class MyRegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.reg_email_input = locators.AccountCreation.reg_email_input
        self.register_button = locators.AccountCreation.register_button
        self.accept_term_checkbox = locators.AccountCreation.accept_term_checkbox
        self.terms_link = locators.AccountCreation.terms_link
        self.sing_in_link = locators.AccountCreation.sing_in_link
        self.forgot_password_link = locators.AccountCreation.forgot_password_link
        self.message_email_required = locators.AccountCreation.message_email_required
        self.register_link_assert = locators.AccountCreation.register_link_assert
        self.message_get_started = locators.AccountCreation.message_get_started
        self.message_already_have_account = locators.AccountCreation.message_already_have_account
        self.message_valid_email = locators.AccountCreation.message_valid_email
        self.message_terms_clients = locators.AccountCreation.message_terms_clients
        self.sing_in_link_assert = locators.AccountCreation.sing_in_link_assert
        self.message_reset_password = locators.AccountCreation.message_reset_password

    def open_page(self):
        self.driver.get("https://justjoin.it/devs/signup")

    def create_account_no_date(self):
        self.driver.find_element(*self.register_button).click()

    def create_account_email_only(self, email):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.register_button).click()

    def create_account_accept_terms_only(self):
        self.driver.find_element(*self.accept_term_checkbox).click()
        self.driver.find_element(*self.register_button).click()

    def create_account_complete(self, email):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.accept_term_checkbox).click()
        self.driver.find_element(*self.register_button).click()

    def check_terms_link(self):
        self.driver.find_element(*self.terms_link).click()

    def check_sing_in_link(self):
        self.driver.find_element(*self.sing_in_link).click()

    def check_forgot_password_link(self):
        self.driver.find_element(*self.forgot_password_link).click()

    def get_message_email_required(self):
        return self.driver.find_element(*self.message_email_required).text

    def is_register_link_assert_displayed(self):
        return self.driver.find_element(*self.register_link_assert).is_displayed()

    def get_message_get_started(self):
        return self.driver.find_element(*self.message_get_started).text

    def get_message_already_have_account(self):
        return self.driver.find_element(*self.message_already_have_account).text

    def get_message_valid_email(self):
        return self.driver.find_element(*self.message_valid_email).text

    def get_message_terms_clients(self):
        return self.driver.find_element(*self.message_terms_clients).text

    def is_sing_in_link_assert_displayed(self):
        return self.driver.find_element(*self.sing_in_link_assert).is_displayed()

    def get_message_reset_password(self):
        return self.driver.find_element(*self.message_reset_password).text
