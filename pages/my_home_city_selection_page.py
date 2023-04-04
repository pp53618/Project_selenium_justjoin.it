from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyCitySelectionPage:

    def __init__(self, driver):
        self.driver = driver
        self.locations_button = locators.CitySelectionLocators.locations_button
        self.city_warsaw_button = locators.CitySelectionLocators.city_warsaw_button
        self.message_results_city_selected_assert = locators.CitySelectionLocators.message_results_city_selected_assert
        self.city_krakow_button = locators.CitySelectionLocators.city_krakow_button
        self.city_wroclaw_button = locators.CitySelectionLocators.city_wroclaw_button
        self.city_poznan_button = locators.CitySelectionLocators.city_poznan_button
        self.city_trojmiasto_button = locators.CitySelectionLocators.city_trojmiasto_button
        self.city_slask_button = locators.CitySelectionLocators.city_slask_button
        self.city_new_york_button = locators.CitySelectionLocators.city_new_york_button
        self.city_sydney_button = locators.CitySelectionLocators.city_sydney_button
        self.city_berlin_button = locators.CitySelectionLocators.city_berlin_button
        self.city_san_francisco_button = locators.CitySelectionLocators.city_san_francisco_button
        self.city_london_button = locators.CitySelectionLocators.city_london_button
        self.other_locations_button = locators.CitySelectionLocators.other_locations_button
        self.city_bialystok_button = locators.CitySelectionLocators.city_bialystok_button
        self.city_biesko_biala_button = locators.CitySelectionLocators.city_biesko_biala_button
        self.city_bydgoszcz_button = locators.CitySelectionLocators.city_bydgoszcz_button
        self.city_czestochowa_button = locators.CitySelectionLocators.city_czestochowa_button
        self.city_kielce_button = locators.CitySelectionLocators.city_kielce_button
        self.city_lublin_button = locators.CitySelectionLocators.city_lublin_button
        self.city_lodz_button = locators.CitySelectionLocators.city_lodz_button
        self.city_olsztyn_button = locators.CitySelectionLocators.city_olsztyn_button
        self.city_opole_button = locators.CitySelectionLocators.city_opole_button
        self.city_rzeszow_button = locators.CitySelectionLocators.city_rzeszow_button
        self.city_szczecin_button = locators.CitySelectionLocators.city_szczecin_button
        self.city_torun_button = locators.CitySelectionLocators.city_torun_button
        self.city_zielona_gora_button = locators.CitySelectionLocators.city_zielona_gora_button
        self.clear_filter_button = locators.CitySelectionLocators.clear_filter_button
        self.another_click_locations_button = locators.CitySelectionLocators.another_click_locations_button
        self.message_offers_assert = locators.CitySelectionLocators.message_offers_assert

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def city_selection_warsaw(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_warsaw_button).click()

    def city_selection_krakow(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_krakow_button).click()

    def city_selection_wroclaw(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_wroclaw_button).click()

    def city_selection_poznan(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_poznan_button).click()

    def city_selection_trojmiasto(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_trojmiasto_button).click()

    def city_selection_slask(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_slask_button).click()

    def city_selection_new_york(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_new_york_button).click()

    def city_selection_sydney(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_sydney_button).click()

    def city_selection_berlin(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_berlin_button).click()

    def city_selection_san_francisco(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_san_francisco_button).click()

    def city_selection_london(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.city_london_button).click()

    def city_selection_bialystok(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_bialystok_button).click()

    def city_selection_bielsko_biala(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_biesko_biala_button).click()

    def city_selection_bydgoszcz(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_bydgoszcz_button).click()

    def city_selection_czestochowa(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_czestochowa_button).click()

    def city_selection_kielce(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_kielce_button).click()

    def city_selection_lublin(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_lublin_button).click()

    def city_selection_lodz(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_lodz_button).click()

    def city_selection_olsztyn(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_olsztyn_button).click()

    def city_selection_opole(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_opole_button).click()

    def city_selection_rzeszow(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_rzeszow_button).click()

    def city_selection_szczecin(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_szczecin_button).click()

    def city_selection_torun(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_torun_button).click()

    def city_selection_zielona_gora(self):
        self.driver.find_element(*self.locations_button).click()
        self.driver.find_element(*self.other_locations_button).click()
        self.driver.find_element(*self.city_zielona_gora_button).click()

    def use_clear_filter(self):
        self.driver.find_element(*self.another_click_locations_button).click()
        self.driver.find_element(*self.clear_filter_button).click()

    def get_message_results_city_selected(self):
        return self.driver.find_element(*self.message_results_city_selected_assert).text

    def get_message_offers(self):
        return self.driver.find_element(*self.message_offers_assert).text
