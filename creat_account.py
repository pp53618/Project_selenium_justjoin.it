import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random


def test_create_account_no_email_entry_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Email is a required field" in driver.find_element(By.XPATH, "//p[contains(@class,'Mui-error')]//span").text


def test_create_account_enter_email_no_confirmation_regulations_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("b.mackiewicz88@wp.pl")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.PARTIAL_LINK_TEXT, "Register").is_displayed()


def test_create_account_no_email_entry_with_acceptance_regulations_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Email is a required field" in driver.find_element(By.XPATH, "//p[contains(@class,'Mui-error')]//span").text


def test_create_account_enter_email_with_acceptance_regulations_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    email = str(random.randint(0, 1000000)) + "b.mackiewicz88@wp.pl"
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Get started for free" in driver.find_element(By.TAG_NAME, "h1").text
    time.sleep(5)


def test_create_account_with_valid_data_re_living_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("b.mackiewicz88@wp.pl")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Already have an account? Sign in" in driver.find_element(By.TAG_NAME, "h6").text


def test_create_account_entering_incorrect_data_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("b.mackiewicz@rbhdsegv.pl")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Get started for free" in driver.find_element(By.TAG_NAME, "h1").text


def test_create_account_by_entering_special_characters_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("b.mackiewicz@rb*&hdsegv.pl")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Email must be a valid email" in driver.find_element(By.XPATH, "//p[contains(@class,'MuiFormHelperText-filled')]//span").text


def test_create_account_with_numbers_in_the_name_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("646377")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Email must be a valid email" in driver.find_element(By.XPATH,"//p[contains(@class,'MuiFormHelperText-filled')]//span").text


def test_create_account_using_uppercase_and_lowercase_letters_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("b.MackiewiCZR88R@Wp.pl")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Get started for free" in driver.find_element(By.TAG_NAME, "h1").text

    time.sleep(5)


def test_create_account_using_more_than_32_characters_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("b.mackiewsdfsfsfssfsfsfdsfsfsicz88@wdfdsfsfsffsfsfsfp.pl")
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Get started for free" in driver.find_element(By.TAG_NAME, "h1").text


def test_create_account_using_less_than_6_characters_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    email = str(random.randint(0, 10)) + "@s.p"
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='acceptTerms']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Get started for free" in driver.find_element(By.TAG_NAME, "h1").text


def test_checking_the_correctness_of_linked_documents_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.CLASS_NAME, "css-1a9gzt0").click()
    assert "Terms - Clients" in driver.find_element(By.TAG_NAME, "h6").text


def test_checking_hyperlinks_sing_in_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//a[@href='/devs']").click()
    assert driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").is_displayed()
    time.sleep(5)


def test_checking_hyperlinks_forgot_password_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://justjoin.it/devs/signup")
    driver.find_element(By.XPATH, "//a[@href='/devs/reset-password']").click()
    assert "Reset password" in driver.find_element(By.XPATH, "//button[@type='submit']//span").text
    time.sleep(5)
