import time
import traceback

import allure

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from locator.locators import SigninLocators, LoginLocators, HomeLocators
from base.BasePage import BasePage
from utilities.XlUtils import get_cell_data


class LogInPage(BasePage):
    # path = "./testData/AutoScript.xlsx"

    env = "dev"

    def __init__(self, driver):  # constructor of page class
        super().__init__(driver)

    @staticmethod
    def get_path_dev_test(env):
        if env == "dev":
            return "./testData/AutoScript_Dev.xlsx"
        elif env == "test":
            return "./testData/AutoScript_test.xlsx"

    def is_logo_exist(self):  # This is used to get Logo of login Page
        return self.is_visible(*LoginLocators.LOGO_VISIBLE)

    def get_LoginPage_url(self, current_url):  # This is used to get Login Url of login Page
        return self.get_url(current_url)

    @staticmethod
    def get_login_credential(sheet_name, row):
        path = LogInPage.get_path_dev_test(LogInPage.env)  # Call the method to get the file path
        email = get_cell_data(path, sheet_name, row, 1)
        password = get_cell_data(path, sheet_name, row, 2)

        return email, password

    def get_paymentmethod_buton(self):  # This is used to get Upgrade link of Subscription Page
        element = self.driver.find_element(By.XPATH, "//button[text() = 'Verify payment method']")
        return element

    def get_login_page_title(self, title):  # This is used to get Login Title of login Page
        return self.get_title(title)

    def is_pwlink_exist(self):  # This is used to get Forgot password link of login Page
        return self.is_visible(*LoginLocators.Forgot_Link)

    def is_tclink_exist(self):  # This is used to get Forgot password link of login Page
        return self.is_visible(*LoginLocators.Terms_and_condition_Link)

    def is_signup_link_exist(self):  # This is used to get SignUP link of login Page
        return self.is_visible(*SigninLocators.sign_next)

    def get_element_Invisible(self, by_locname, locator):
        try:
            if self.is_loader_invisible(by_locname, locator):
                print("loader is Invisible")
                return True
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def get_element_scrollClick(self, by_locname, locator):
        try:
            if self.is_loader_invisible(*LoginLocators.loader):
                print("loader is Invisible")
                return self.scrollToclick_element(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def get_element_click(self, by_locname, locator):
        try:
            if self.is_loader_invisible(*LoginLocators.loader):
                print("loader is Invisible")
                return self.is_clickable(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def login_element_exist(self, by_locname, locator):
        if self.is_visible(by_locname, locator):
            return self.do_element(by_locname, locator)

    def ScrollclickOperation(self, by_locname, locator):  # This is used to perform scroll and click to button
        try:
            if self.is_visible(by_locname, locator):
                return self.scrollToclick_element(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def chargebee_card_container_frame(self):
        try:
            iframe = self.driver.find_element(By.CLASS_NAME, "chargebee-card-container")
            self.driver.switch_to.frame(iframe)

        except NoSuchElementException:
            print(traceback.format_exc())

    def clickOperation(self, by_locname, locator):  # This is used to perform click to button
        try:
            if self.is_visible(by_locname, locator):
                self.is_clickable(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    @allure.step("Login with email: '1'")  # This is used to Login in Pictory app
    def loginpictory(self, email, password):
        try:
            script = """
                // Set and trigger change for email input
                var inputElement = document.querySelector('#emailField');
                var lastValue = inputElement.value;
                inputElement.value = arguments[0];
                
                // Trigger React's internal value tracker for email input
                var tracker = inputElement._valueTracker;
                if (tracker) {
                    tracker.setValue(lastValue);
                }
                
                // Dispatch 'input' event for email field
                var inputEvent = new Event('input', { bubbles: true });
                inputElement.dispatchEvent(inputEvent);
                
                // Set and trigger change for password input
                var passElement = document.querySelector('#outlined-adornment-password');
                var lastPassValue = passElement.value;
                passElement.value = arguments[1];
                
                // Trigger React's internal value tracker for password input
                var passTracker = passElement._valueTracker;
                if (passTracker) {
                    passTracker.setValue(lastPassValue);
                }
                
                // Dispatch 'input' event for password field
                var passInputEvent = new Event('input', { bubbles: true });
                passElement.dispatchEvent(passInputEvent);
                """
            self.driver.execute_script(script, email, password)

            """
            self.do_send_keys(*LoginLocators.email_field, email)
            self.do_send_keys(*LoginLocators.password_field, password)
            
            """

            self.do_click(*LoginLocators.login_bn)

        except StaleElementReferenceException:
            print(traceback.format_exc())
        # self.driver.find_element(*LogInLocators.password).send_keys(password, Keys.ENTER)

    def get_homepage_element(self, by_locname, locator):
        if self.is_visible(by_locname, locator):
            return self.do_element(by_locname, locator)

    def autocard_suggest(self):
        search = self.driver.find_element(By.XPATH, "//*[starts-with(@id, 'number')]")
        search.clear()
        search.send_keys('411')
        auto_complete = self.driver.find_elements(By.XPATH, "//div[starts-with(@class, 'cb-pmcard__details')]")
        auto_complete[0].click()

    @allure.step("Login with email: '1'")
    def loginusing_google(self, email, password):  # This is used to Login through Google in Pictory app
        try:
            time.sleep(5)
            self.do_send_keys(*LoginLocators.Gmail_Field, email)
            self.do_send_keys(*LoginLocators.Gmail_Field, Keys.ENTER)  # Simulate pressing the "Enter" key

            if self.is_visible(*LoginLocators.Gmail_password):
                self.do_send_keys(*LoginLocators.Gmail_password, password)
                self.do_send_keys(*LoginLocators.Gmail_password, Keys.ENTER)  # Simulate pressing the "Enter" key

            time.sleep(10)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            print(traceback.format_exc())

    def login_element_scrollClick(self, by_locname, locator):
        try:
            if self.is_loader_invisible(*HomeLocators.loader):
                print("loader is Invisible")
                return self.scrollToclick_element_DOM(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def get_element_text(self, by_locname, locator):  # This is used to get element text of login Page
        if self.is_visible(by_locname, locator):
            return self.do_element_text(by_locname, locator)

    def get_element_color(self, by_locname, locator):  # This is used to get element text color of login Page
        return self.do_element_color(by_locname, locator)
