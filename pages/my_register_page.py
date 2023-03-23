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
        self.register_fb_button = locators.AccountCreation.register_fb_button
        self.message_fb = locators.AccountCreation.message_fb
        self.log_email_input = locators.LoginLocators.log_email_input
        self.fb_password_input = locators.AccountCreation.fb_password_input
        self.log_in_fb_button = locators.AccountCreation.log_in_fb_button
        self.accept_fb_button = locators.AccountCreation.accept_fb_button
        self.register_google_button = locators.AccountCreation.register_google_button
        self.google_email_input = locators.AccountCreation.google_email_input
        self.google_next_button = locators.AccountCreation.google_next_button
        self.message_google = locators.AccountCreation.message_google
        self.register_github_button = locators.AccountCreation.register_github_button
        self.github_email_input = locators.AccountCreation.github_email_input
        self.github_password_input = locators.AccountCreation.github_password_input
        self.github_sing_in_button = locators.AccountCreation.github_sing_in_button
        self.message_github = locators.AccountCreation.message_github
        self.register_linkedin_button = locators.AccountCreation.register_linkedin_button
        self.linkedin_email_input = locators.AccountCreation.linkedin_email_input
        self.linkedin_password_input = locators.AccountCreation.linkedin_password_input
        self.linkedin_sing_in_button = locators.AccountCreation.linkedin_sing_in_button
        self.message_linkedin = locators.AccountCreation.message_linkedin

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

    def create_account_by_fb(self, email, passsword):
        self.driver.find_element(*self.register_fb_button).click()
        self.driver.find_element(*self.log_email_input).send_keys(email)
        self.driver.find_element(*self.fb_password_input).send_keys(passsword)
        self.driver.find_element(*self.accept_fb_button).click()
      #  self.driver.find_element(*self.log_in_fb_button).click()

    def create_account_by_google(self, email):
        self.driver.find_element(*self.register_google_button).click()
        self.driver.find_element(*self.google_email_input).send_keys(email)
        self.driver.find_element(*self.google_next_button).click()

    def create_account_by_github(self, email, password):
        self.driver.find_element(*self.register_github_button).click()
        self.driver.find_element(*self.github_email_input).send_keys(email)
        self.driver.find_element(*self.github_password_input).send_keys(password)
        self.driver.find_element(*self.github_sing_in_button).click()

    def create_account_by_linkedin(self, email, password):
        self.driver.find_element(*self.register_linkedin_button).click()
        self.driver.find_element(*self.linkedin_email_input).send_keys(email)
        self.driver.find_element(*self.linkedin_password_input).send_keys(password)
        self.driver.find_element(*self.linkedin_sing_in_button).click()

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

    def get_message_facebook(self):
        return self.driver.find_element(*self.message_fb).text

    def get_message_google(self):
        return self.driver.find_element(*self.message_google).text

    def get_message_github(self):
        return self.driver.find_element(*self.message_github).text

    def get_message_linkedin(self):
        return self.driver.find_element(*self.message_linkedin).text