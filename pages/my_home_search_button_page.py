from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyButtonSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.long_menu_button = locators.ButtonLocators.long_menu_button
        self.js_button = locators.ButtonLocators.js_button
        self.is_js_visibility_assert = locators.ButtonLocators.is_js_visibility_assert
        self.html_button = locators.ButtonLocators.html_button
        self.is_html_visibility_assert = locators.ButtonLocators.is_html_visibility_assert
        self.php_button = locators.ButtonLocators.php_button
        self.is_php_visibility_assert = locators.ButtonLocators.is_php_visibility_assert
        self.ruby_button = locators.ButtonLocators.ruby_button
        self.is_ruby_visibility_assert = locators.ButtonLocators.is_ruby_visibility_assert
        self.python_button = locators.ButtonLocators.python_button
        self.is_python_visibility_assert = locators.ButtonLocators.is_python_visibility_assert
        self.java_button = locators.ButtonLocators.java_button
        self.is_java_visibility_assert = locators.ButtonLocators.is_java_visibility_assert
        self.net_button = locators.ButtonLocators.net_button
        self.is_net_visibility_assert = locators.ButtonLocators.is_net_visibility_assert
        self.scala_button = locators.ButtonLocators.scala_button
        self.is_scala_visibility_assert = locators.ButtonLocators.is_scala_visibility_assert
        self.c_button = locators.ButtonLocators.c_button
        self.is_c_visibility_assert = locators.ButtonLocators.is_c_visibility_assert
        self.mobile_button = locators.ButtonLocators.mobile_button
        self.is_mobile_visibility_assert = locators.ButtonLocators.is_mobile_visibility_assert
        self.testing_button = locators.ButtonLocators.testing_button
        self.is_testing_visibility_assert = locators.ButtonLocators.is_testing_visibility_assert
        self.devops_button = locators.ButtonLocators.devops_button
        self.is_devops_visibility_assert = locators.ButtonLocators.is_devops_visibility_assert
        self.admin_button = locators.ButtonLocators.admin_button
        self.is_admin_visibility_assert = locators.ButtonLocators.is_admin_visibility_assert
        self.ux_ui_button = locators.ButtonLocators.ux_ui_button
        self.is_ux_ui_visibility_assert = locators.ButtonLocators.ux_ui_button
        self.pm_button = locators.ButtonLocators.pm_button
        self.is_pm_visibility_assert = locators.ButtonLocators.is_pm_visibility_assert
        self.game_button = locators.ButtonLocators.game_button
        self.is_game_visibility_assert = locators.ButtonLocators.is_game_visibility_assert
        self.analytics_button = locators.ButtonLocators.analytics_button
        self.is_analytics_visibility_assert = locators.ButtonLocators.is_analytics_visibility_assert
        self.security_button = locators.ButtonLocators.security_button
        self.is_security_visibility_assert = locators.ButtonLocators.is_security_visibility_assert
        self.data_button = locators.ButtonLocators.data_button
        self.is_data_visibility_assert = locators.ButtonLocators.is_data_visibility_assert
        self.go_button = locators.ButtonLocators.go_button
        self.is_go_visibility_assert = locators.ButtonLocators.is_go_visibility_assert
        self.support_button = locators.ButtonLocators.support_button
        self.is_support_visibility_assert = locators.ButtonLocators.is_support_visibility_assert
        self.erp_button = locators.ButtonLocators.erp_button
        self.is_erp_visibility_assert = locators.ButtonLocators.is_erp_visibility_assert
        self.architecture_button = locators.ButtonLocators.architecture_button
        self.is_architecture_visibility_assert = locators.ButtonLocators.is_architecture_visibility_assert
        self.other_button = locators.ButtonLocators.other_button
        self.is_other_visibility_assert = locators.ButtonLocators.is_other_visibility_assert

    def open_page(self):
        self.driver.get("https://justjoin.it/")

    def button_categories_js(self):
        self.driver.find_element(*self.js_button).click()

    def button_categories_html(self):
        self.driver.find_element(*self.html_button).click()

    def button_categories_php(self):
        self.driver.find_element(*self.php_button).click()

    def button_categories_ruby(self):
        self.driver.find_element(*self.ruby_button).click()

    def button_categories_python(self):
        self.driver.find_element(*self.python_button).click()

    def button_categories_java(self):
        self.driver.find_element(*self.java_button).click()

    def button_categories_net(self):
        self.driver.find_element(*self.net_button).click()

    def button_categories_scala(self):
        self.driver.find_element(*self.scala_button).click()

    def button_categories_c(self):
        self.driver.find_element(*self.c_button).click()

    def button_categories_mobile(self):
        self.driver.find_element(*self.mobile_button).click()

    def button_categories_testing(self):
        self.driver.find_element(*self.testing_button).click()

    def button_categories_devops(self):
        self.driver.find_element(*self.devops_button).click()

    def button_categories_admin(self):
        self.driver.find_element(*self.admin_button).click()

    def button_categories_ux_ui(self):
        self.driver.find_element(*self.ux_ui_button).click()

    def button_categories_pm(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.pm_button).click()

    def button_categories_game(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.game_button).click()

    def button_categories_analytics(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.analytics_button).click()

    def button_categories_security(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.security_button).click()

    def button_categories_data(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.data_button).click()

    def button_categories_go(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.go_button).click()

    def button_categories_support(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.support_button).click()

    def button_categories_erp(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.erp_button).click()

    def button_categories_architecture(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.architecture_button).click()

    def button_categories_other(self):
        self.driver.find_element(*self.long_menu_button).click()
        self.driver.find_element(*self.other_button).click()

    def is_js_visibility_displayed(self):
        return self.driver.find_element(*self.is_js_visibility_assert).is_displayed()

    def is_html_visibility_displayed(self):
        return self.driver.find_element(*self.is_html_visibility_assert).is_displayed()

    def is_php_visibility_displayed(self):
        return self.driver.find_element(*self.is_php_visibility_assert).is_displayed()

    def is_ruby_visibility_displayed(self):
        return self.driver.find_element(*self.is_ruby_visibility_assert).is_displayed()

    def is_python_visibility_displayed(self):
        return self.driver.find_element(*self.is_python_visibility_assert).is_displayed()

    def is_java_visibility_displayed(self):
        return self.driver.find_element(*self.is_java_visibility_assert).is_displayed()

    def is_net_visibility_displayed(self):
        return self.driver.find_element(*self.is_net_visibility_assert).is_displayed()

    def is_scala_visibility_displayed(self):
        return self.driver.find_element(*self.is_scala_visibility_assert).is_displayed()

    def is_c_visibility_displayed(self):
        return self.driver.find_element(*self.is_c_visibility_assert).is_displayed()

    def is_mobile_visibility_displayed(self):
        return self.driver.find_element(*self.is_mobile_visibility_assert).is_displayed()

    def is_testing_visibility_displayed(self):
        return self.driver.find_element(*self.is_testing_visibility_assert).is_displayed()

    def is_devops_visibility_displayed(self):
        return self.driver.find_element(*self.is_devops_visibility_assert).is_displayed()

    def is_admin_visibility_displayed(self):
        return self.driver.find_element(*self.is_admin_visibility_assert).is_displayed()

    def is_ux_ui_visibility_displayed(self):
        return self.driver.find_element(*self.is_ux_ui_visibility_assert).is_displayed()

    def is_pm_visibility_displayed(self):
        return self.driver.find_element(*self.is_pm_visibility_assert).is_displayed()

    def is_game_visibility_displayed(self):
        return self.driver.find_element(*self.is_game_visibility_assert).is_displayed()

    def is_analytics_visibility_displayed(self):
        return self.driver.find_element(*self.is_analytics_visibility_assert).is_displayed()

    def is_security_visibility_displayed(self):
        return self.driver.find_element(*self.is_security_visibility_assert).is_displayed()

    def is_data_visibility_displayed(self):
        return self.driver.find_element(*self.is_data_visibility_assert).is_displayed()

    def is_go_visibility_displayed(self):
        return self.driver.find_element(*self.is_go_visibility_assert).is_displayed()

    def is_support_visibility_displayed(self):
        return self.driver.find_element(*self.is_support_visibility_assert).is_displayed()

    def is_erp_visibility_displayed(self):
        return self.driver.find_element(*self.is_erp_visibility_assert).is_displayed()

    def is_architecture_visibility_displayed(self):
        return self.driver.find_element(*self.is_architecture_visibility_assert).is_displayed()

    def is_other_visibility_displayed(self):
        return self.driver.find_element(*self.is_other_visibility_assert).is_displayed()