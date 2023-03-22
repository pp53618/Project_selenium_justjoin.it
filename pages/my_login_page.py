from locators import locators
from selenium.webdriver.common.by import By


class MyLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.log_email_input = locators.LoginLocators.log_email_input
        self.password_input = locators.LoginLocators.password_input
        self.sing_in_button = locators.LoginLocators.sing_in_button
        self.message_my_profile = locators.LoginLocators.message_my_profile
        self.forgot_password_link = locators.AccountCreation.forgot_password_link
        self.reset_password_button = locators.LoginLocators.reset_password_button
        self.message_reset_password_assert = locators.LoginLocators.message_reset_password_assert
        self.message_email_required = locators.AccountCreation.message_email_required
        self.message_password_assert = locators.LoginLocators.message_password_assert
        self.register_button = locators.LoginLocators.register_button

    def open_page(self):
        self.driver.get("https://justjoin.it/devs")

    def password_change(self, email):
        self.driver.find_element(*self.forgot_password_link).click()
        self.driver.find_element(*self.log_email_input).send_keys(email)
        self.driver.find_element(*self.reset_password_button).click()

    def log_in(self, email, password):
        self.driver.find_element(*self.log_email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sing_in_button).click()

    def log_in_no_data(self):
        self.driver.find_element(*self.sing_in_button).click()

    def log_in_no_email(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sing_in_button).click()

    def log_in_no_password(self, email):
        self.driver.find_element(*self.log_email_input).send_keys(email)
        self.driver.find_element(*self.sing_in_button).click()

    def check_register_link(self):
        self.driver.find_element(*self.register_button).click()

    def get_message_my_profile(self):
        return self.driver.find_element(*self.message_my_profile).text

    def get_message_resset_password(self):
        return self.driver.find_element(*self.message_success_assert).text

    def is_sing_in_link_assert_displayed(self):
        return self.driver.find_element(*self.sing_in_button).is_displayed()

    def get_message_email_required(self):
        return self.driver.find_element(*self.message_email_required).text

    def get_message_password(self):
        return self.driver.find_element(*self.message_password_assert).text