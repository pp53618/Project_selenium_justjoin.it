import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support.select import Select
from pages.my_home_city_selection_page import MyCitySelectionPage


@pytest.mark.usefixtures("setup")
class TestCitySelection:

    def test_city_selection_warsaw_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_warsaw()
        msg = 'Warszawa'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_krakow_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_krakow()
        msg = 'Kraków'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_wroclaw_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_wroclaw()
        msg = 'Wrocław'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_poznan_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_poznan()
        msg = 'Poznań'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_trojmiasto_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_trojmiasto()
        msg = 'Trójmiasto'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_slask_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_slask()
        msg = 'Śląsk'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_new_york_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_new_york()
        msg = 'New York'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_sydney_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_sydney()
        msg = 'Sydney'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_berlin_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_berlin()
        msg = 'Berlin'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_san_francisco_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_san_francisco()
        msg = 'San Francisco'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_london_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_london()
        msg = 'London'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)


@pytest.mark.usefixtures("setup")
class TestOtherCitySelection:

    def test_city_selection_bialystok_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_bialystok()
        msg = 'Białystok'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_bielsko_biala_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_bielsko_biala()
        msg = 'Bielsko-Biała'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_bydgoszcz_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_bydgoszcz()
        msg = 'Bydgoszcz'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_czestochowa_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_czestochowa()
        msg = 'Częstochowa'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_kielce_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_kielce()
        msg = 'Kielce'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_lublin_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_lublin()
        msg = 'Lublin'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_lodz_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_lodz()
        msg = 'Łódź'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_olsztyn_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_olsztyn()
        msg = 'Olsztyn'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_opole_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_opole()
        msg = 'Opole'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_reszow_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_rzeszow()
        msg = 'Rzeszów'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_szczecin_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_szczecin()
        msg = 'Szczecin'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_torun_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_torun()
        msg = 'Toruń'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)

    def test_city_selection_zielona_gora_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_zielona_gora()
        msg = 'Zielona Góra'
        assert msg in my_city_selection_page.get_message_results_city_selected()
        time.sleep(5)


@pytest.mark.usefixtures("setup")
class TestClearCitySelection:

    def test_city_selection_and_use_clear_filter_passed(self):
        my_city_selection_page = MyCitySelectionPage(self.driver)
        my_city_selection_page.open_page()
        my_city_selection_page.city_selection_new_york()
        my_city_selection_page.use_clear_filter()
        msg = 'Offers with salary'
        assert msg in my_city_selection_page.get_message_offers()
        time.sleep(5)