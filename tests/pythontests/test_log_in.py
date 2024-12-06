import time
import traceback

import allure
import pytest

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException

from locator.locators import LoginLocators, SigninLocators, HomeLocators
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.loadtimePage import LoadTimeTracker
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("LogIn Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestLogIn:
    email, password = TestDataForProject.get_login_credential("Login", 0)

    @allure.title("signup link visible")
    @allure.description("This is test of signup link visible")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_signup_link_visible(self):
        # self.logger.info("To verify link is visible on the app")
        self.LogInPage = LogInPage(self.driver)
        flag = self.LogInPage.is_signup_link_exist()
        assert flag

        # self.logger.info("Test passed: login page title on the app")

    @allure.title("signup link click")
    @allure.description("This is test of signup link click")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_signup_link_click(self, env):
        # self.logger.info("To verify link is visible on the app")
        self.LogInPage = LogInPage(self.driver)
        try:
            self.LogInPage.clickOperation(*LoginLocators.sign_next)

            if env in SigninLocators.SIGNIN_PAGE_URL:
                expected_url = SigninLocators.SIGNIN_PAGE_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)
                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                print("Current URL:", current_url)

        except StaleElementReferenceException:
            print(traceback.format_exc())

    @allure.title("login page url")
    @allure.description("This is test of login page url")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_login_page_url(self, env):

        self.LogInPage = LogInPage(self.driver)

        if env in LoginLocators.LOGIN_PAGE_URL:
            expected_url = LoginLocators.LOGIN_PAGE_URL[env]
            current_url = self.LogInPage.get_LoginPage_url(expected_url)

            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
            print("Current URL:", current_url)

    @allure.title("login page title")
    @allure.description("This is test of login page title")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_login_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        title = self.LogInPage.get_login_page_title(LoginLocators.LOGIN_PAGE_TITLE)
        assert title == LoginLocators.LOGIN_PAGE_TITLE

    @allure.title("login page logo visible")
    @allure.description("This is test of login page logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.sanity
    def test_login_logo_visible(self):
        self.LogInPage = LogInPage(self.driver)
        flag = self.LogInPage.is_logo_exist()
        assert flag

    @allure.title("email and password field is exist")
    @allure.description("email and password field --> exist")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_email_password_field(self):
        self.LogInPage = LogInPage(self.driver)
        element = self.LogInPage.login_element_exist(*LoginLocators.email_field)
        assert (element.is_displayed(), f"element with name '{element.text}' is not present on the page.")

        element = self.LogInPage.login_element_exist(*LoginLocators.password_field)
        assert (element.is_displayed(), f"element with name '{element.text}' is not present on the page.")

    @allure.title("forgot password link visible")
    @allure.description("This is test forgot password link")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_forgot_pwlink_visible(self):
        self.LogInPage = LogInPage(self.driver)
        flag = self.LogInPage.is_pwlink_exist()
        assert flag

    @allure.title("Login button is exist")
    @allure.description("Login button --> exist")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_login_butn_exist(self):
        self.LogInPage = LogInPage(self.driver)
        element = self.LogInPage.login_element_exist(*LoginLocators.login_bn)
        assert (element.is_displayed(), f"element with name '{element.text}' is not present on the page.")

    @allure.title("Terms and condition link visible")
    @allure.description("Terms and condition link --> visible")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_tclink_visible(self):
        self.LogInPage = LogInPage(self.driver)
        flag = self.LogInPage.is_tclink_exist()
        assert flag

    @allure.title("Terms and condition link click")
    @allure.description("This is test of Terms and condition link click")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_tclink_click(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.LogInPage.clickOperation(*LoginLocators.Terms_and_condition_Link)

        original_window_handle = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != original_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        if env == "dev":
            expected_url = LoginLocators.DEV_TC_PAGE_URL

        elif env == "staging":
            expected_url = LoginLocators.STAGING_TC_PAGE_URL

        elif env == "prod":
            expected_url = LoginLocators.PROD_TC_PAGE_URL

        current_url = self.LogInPage.get_LoginPage_url(expected_url)
        assert current_url == expected_url
        print(current_url)

        self.driver.switch_to.window(original_window_handle)

    @allure.title("Login with valid data test and Load time")
    @allure.description("This is test of login with valid data and Load time")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    @pytest.mark.PageLoad
    def test_login_withvalid_user(self):
        self.LogInPage = LogInPage(self.driver)

        email, password = TestDataForProject.get_login_credential("Login", 4)

        start_time = LoadTimeTracker.start_timing()
        self.LogInPage.loginpictory(email, password)

        text = self.LogInPage.get_element_text(*HomeLocators.Project)
        if text:
            assert text == "Projects"
            print(text)
            home_page_load_time = LoadTimeTracker.end_timing(start_time)
            print(f"Home page load time: {home_page_load_time} sec")

            # Attach load time to Allure report
            LoadTimeTracker.attach_load_time(home_page_load_time, page_type="login --> home page")
            LoadTimeTracker.monitor_cpu_usage(home_page_load_time)

    @allure.title("Login with invalid email test")
    @allure.description("This is test of login with invalid email")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_login_withInvalid_user(self):
        self.LogInPage = LogInPage(self.driver)

        email, password = TestDataForProject.get_login_credential("Login", 1)
        self.LogInPage.loginpictory(email, password)

        text = self.LogInPage.get_element_text(*LoginLocators.invalid_data_msg)
        hex_color = self.LogInPage.get_element_color(*LoginLocators.invalid_data_msg)
        exp_error_color = {'#ffe7d9', '#ffa48d', '#ff5252', '#b72136', '#7a0c2e', '#ffd0d0'}

        assert text == "Invalid username or password" and hex_color in exp_error_color
        print(hex_color)

    @allure.title("Login with Special character data test")
    @allure.description("This is test of login with Special character")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_login_specialcharacter_user(self):
        self.LogInPage = LogInPage(self.driver)
        email, password = TestDataForProject.get_login_credential("Login", 2)
        self.LogInPage.loginpictory(email, password)

        exp_error_color = {'#ffe7d9', '#ffa48d', '#ff5252', '#b72136', '#7a0c2e', '#ffd0d0', '#fff'}
        hex_color = self.LogInPage.get_element_color(*LoginLocators.Email_field_Required)

        if hex_color:
            assert hex_color in exp_error_color
            print(hex_color)

        # assert text=="Invalid username or password"

    @allure.title("Login with google text exist")
    @allure.description("Login with google text --> exist")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_google_Continue_text_exist(self):
        self.LogInPage = LogInPage(self.driver)
        element = self.LogInPage.login_element_exist(*LoginLocators.google_Continue)
        assert (element.is_displayed(), f"element with name '{element.text}' is not present on the page.")

    @allure.title("Login with google credential data test")
    @allure.description("This is test of login with google credential")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.sanity
    @pytest.mark.skip(reason="google security issue on cloud server")
    def test_login_withgoogle_account(self):
        self.LogInPage = LogInPage(self.driver)

        email, password = TestDataForProject.get_login_credential("Login", 3)

        self.LogInPage.clickOperation(*LoginLocators.google_Continue)
        login_Page = self.LogInPage.get_homepage_element(*LoginLocators.Gmail_Field)
        try:
            if login_Page:
                self.LogInPage.loginusing_google(email, password)

            repurpose = self.LogInPage.get_homepage_element(*LoginLocators.repurpose_homepage)
            if repurpose:
                try:
                    assert (
                        repurpose.is_displayed(), f"element with name '{repurpose.text}' is not present on the page.")
                    print(repurpose.text)

                except (StaleElementReferenceException, TimeoutException, NoSuchElementException):
                    print(traceback.format_exc())

        except (StaleElementReferenceException, TimeoutException, NoSuchElementException):
            print(traceback.format_exc())

    @allure.title("Logout after login in pictory")
    @allure.description("This is test of logout after login in pictory")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.sanity
    def test_logout_after_login(self, env):
        self.LogInPage = LogInPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.LogInPage.login_element_scrollClick(*LoginLocators.login_hover_Profile)
        self.LogInPage.login_element_scrollClick(*LoginLocators.logout_bn)

        element = self.LogInPage.login_element_exist(*LoginLocators.login_bn)
        if element:
            if env in LoginLocators.LOGIN_PAGE_URL:
                expected_url = LoginLocators.LOGIN_PAGE_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                print(current_url)
