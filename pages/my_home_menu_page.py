from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyMenuButton:

    def __init__(self, driver):
        self.driver = driver
        self.menu_button = locators.MenuLocators.menu_button
        self.programmer_100k_button = locators.MenuLocators.programmer_100k_button
        self.message_programmer_100k_assert = locators.MenuLocators.message_programmer_100k_assert
        self.breakfast_with_programming_button = locators.MenuLocators.breakfast_with_programming_button
        self.for_juniors_button = locators.MenuLocators.for_juniors_button
        self.ambassador_program_button = locators.MenuLocators.ambassador_program_button
        self.it_index_button = locators.MenuLocators.it_index_button
        self.event_button = locators.MenuLocators.event_button
        self.just_join_games_button = locators.MenuLocators.just_join_games_button
        self.press_room_button = locators.MenuLocators.press_room_button
        self.reports_button = locators.MenuLocators.reports_button
        self.careers_button = locators.MenuLocators.careers_button
        self.is_breakfast_with_programming_visibility_assert = locators.MenuLocators.is_breakfast_with_programming_visibility_assert
        self.message_for_junior_assert = locators.MenuLocators.message_for_junior_assert
        self.message_ambassador_program_assert = locators.MenuLocators.message_ambassador_program_assert
        self.message_it_index_assert = locators.MenuLocators.message_it_index_assert
        self.message_event_assert = locators.MenuLocators.message_event_assert
        self.is_just_join_games_visibility_assert = locators.MenuLocators.is_just_join_games_visibility_assert
        self.message_press_room_assert = locators.MenuLocators.message_press_room_assert
        self.message_reports_assert = locators.MenuLocators.message_reports_assert
        self.cookie_button = locators.MenuLocators.cookie_button
        self.message_careers_assert = locators.MenuLocators.message_careers_assert
        self.rss_button = locators.MenuLocators.rss_button
        self.help_button = locators.MenuLocators.help_button
        self.terms_button = locators.MenuLocators.terms_button
        self.is_chat_visibility_assert = locators.SearchLocators.is_chat_visibility_assert
        self.message_terms_clients = locators.AccountCreation.message_terms_clients
        self.sign_in_button = locators.MenuLocators.sign_in_button
        self.log_email_input = locators.MenuLocators.log_email_input
        self.log_password_input = locators.MenuLocators.log_password_input
        self.log_sign_in_button = locators.MenuLocators.log_sign_in_button
        self.message_invalid_email_or_password_assert = locators.MenuLocators.message_invalid_email_or_password_assert

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def button_menu_programmer_100k(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.programmer_100k_button).click()

    def button_menu_breakfast_with_programming(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.breakfast_with_programming_button).click()

    def button_for_junior(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.for_juniors_button).click()

    def button_ambassador_program(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.ambassador_program_button).click()

    def button_it_index(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.it_index_button).click()

    def button_event(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.event_button).click()

    def button_just_join_games(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.just_join_games_button).click()

    def button_press_room(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.press_room_button).click()

    def button_reports(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.reports_button).click()

    def button_careers(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.careers_button).click()

    def button_rss(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.rss_button).click()

    def button_help(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.help_button).click()

    def button_terms(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.terms_button).click()

    def button_sign_in(self, email, password):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.cookie_button).click()
        self.driver.find_element(*self.sign_in_button).click()
        self.driver.find_element(*self.log_email_input).send_keys(email)
        self.driver.find_element(*self.log_password_input).send_keys(password)
        self.driver.find_element(*self.log_sign_in_button).click()

    def get_message_programmer_100k(self):
        return self.driver.find_element(*self.message_programmer_100k_assert).text

    def get_message_for_junior(self):
        return self.driver.find_element(*self.message_for_junior_assert).text

    def is_breakfast_with_programming_displayed(self):
        return self.driver.find_element(*self.is_breakfast_with_programming_visibility_assert).is_displayed()

    def get_message_ambassador_program(self):
        return self.driver.find_element(*self.message_ambassador_program_assert).text

    def get_message_it_index(self):
        return self.driver.find_element(*self.message_it_index_assert).text

    def get_message_event(self):
        return self.driver.find_element(*self.message_event_assert).text

    def is_just_join_games_displayed(self):
        return self.driver.find_element(*self.is_just_join_games_visibility_assert).is_displayed()

    def get_message_press_room(self):
        return self.driver.find_element(*self.message_press_room_assert).text

    def get_message_reports(self):
        return self.driver.find_element(*self.message_reports_assert).text

    def get_message_careers(self):
        return self.driver.find_element(*self.message_careers_assert).text

    def is_chat_displayed(self):
        return self.driver.find_element(*self.is_chat_visibility_assert).is_displayed()

    def get_message_terms_clients(self):
        return self.driver.find_element(*self.message_terms_clients).text

    def get_message_invalid_email_or_password(self):
        return self.driver.find_element(*self.message_invalid_email_or_password_assert).text