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
    register_fb_button = (By.XPATH, "//a[@href='/developers/auth/facebook']")
    message_fb = (By.CLASS_NAME, "login_page")
    fb_password_input = (By.XPATH, "//input[@name ='pass']")
    log_in_fb_button = (By.ID, "loginbutton")
    accept_fb_button = (By.XPATH, "//button[@data-cookiebanner='accept_button']")
    register_google_button = (By.XPATH, "//a[@href='/developers/auth/google']")
    google_email_input = (By.XPATH, "//input[@type='email']")
    google_next_button = (By.XPATH, "//button[@type='button']")
    message_google = (By.XPATH, "//div[@jsname='YASyvd']")
    register_github_button = (By.XPATH, "//a[@href='/developers/auth/github']")
    github_email_input = (By.XPATH, "//input[@name='login']")
    github_password_input = (By.XPATH, "//input[@name='password']")
    github_sing_in_button = (By.XPATH, "//input[@type='submit']")
    message_github = (By.XPATH, "//h2[contains(@class,'mb-4')]")
    register_linkedin_button = (By.XPATH, "//a[@href='/developers/auth/linkedin']")
    linkedin_email_input = (By.ID, "username")
    linkedin_password_input = (By.ID, "password")
    linkedin_sing_in_button = (By.XPATH, "//button[@type='submit']")
    message_linkedin = (By.XPATH, "//h1[@class='header__logo']")


class LoginLocators:

    log_email_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//INPUT[@name='password']")
    sing_in_button = (By.XPATH, "//button[@type='submit']")
    reset_password_button = (By.XPATH, "//button[@type='submit']")
    message_my_profile = (By.XPATH, "//div[@class='css-jtlf28']")
    message_reset_password_assert = (By.TAG_NAME, "h1")
    message_password_assert = (By.XPATH, "//div[contains(@class,'MuiGrid-align-items-xs-center')]//label")
    register_button = (By.XPATH, "//a[@href='/devs/signup']")


class SearchLocators:

    search_home_input = (By.XPATH, "//input[@placeholder='Search']")
    search_js_category_span = (By.XPATH, "//span[text()='JavaScript']")
    message_results_search_assert = (By.XPATH, "//span[@class='css-lp92kk']")
    is_chat_visibility_assert = (By.XPATH, "//div[@id='chat-widget-container']")
    message_error_search = (By.XPATH, "//span[@class='css-x62lqu']")
    search_js_category_xpath = (By.XPATH, "//span[text()='JavaScript']")
    search_html_category_xpath = (By.XPATH, "//span[text()='HTML']")
    search_category_xpath = (By.XPATH, "//span[@class='css-g90fw7']")
#    back_search_button = (By.XPATH, "//button[contains(@class,'css-lp92kk')]//span")


class ButtonLocators:

    js_button = (By.XPATH, "//a[@href='/all/javascript']")
    is_js_visibility_assert = (By.XPATH, "//img[@src='/static/media/javascript.59ed3183.svg']")
