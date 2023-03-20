from selenium.webdriver.common.by import By


class AccountCreation:

    reg_email_input = (By.XPATH, "//input[@name='email']")
    register_button = (By.XPATH, "//button[@type='submit']")
    accept_term_checkbox = (By.XPATH, "//input[@name='acceptTerms']")
    terms_link = (By.CLASS_NAME, "css-1a9gzt0")
    sing_in_link = (By.XPATH, "//a[@href='/devs']")
    forgot_password_link = (By.XPATH, "//a[@href='/devs/reset-password']")
    message_email_required = (By.XPATH, "//p[contains(@class,'Mui-error')]//span")
    register_link_assert = (By.PARTIAL_LINK_TEXT, "Register")
    message_get_started = (By.TAG_NAME, "h1")
    message_already_have_account = (By.TAG_NAME, "h6")
    message_valid_email = (By.XPATH, "//p[contains(@class,'MuiFormHelperText-filled')]//span")
    message_terms_clients = (By.TAG_NAME, "h6")
    sing_in_link_assert = (By.PARTIAL_LINK_TEXT, "Sign in")
    message_reset_password = (By.XPATH, "//button[@type='submit']//span")
