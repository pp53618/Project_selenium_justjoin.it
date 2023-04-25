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
        self.message_breakfast_with_programming_assert = locators.MenuLocators.message_breakfast_with_programming_assert
        self.message_for_junior_assert = locators.MenuLocators.message_for_junior_assert

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

    def get_message_programmer_100k(self):
        return self.driver.find_element(*self.message_programmer_100k_assert).text

    def get_message_for_junior(self):
        return self.driver.find_element(*self.message_for_junior_assert).text

    def is_message_breakfast_with_programming_displayed(self):
        return self.driver.find_element(*self.message_breakfast_with_programming_assert).is_displayed()
