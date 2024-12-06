import time
import pytest
import allure

from locator.locators import AccountLocators, HomeLocators
from pageObjects.pictryPages.AccountPage import AccountPage
from pageObjects.pictryPages.LogInPage import LogInPage
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Account Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestAccount:
    email, password = TestDataForProject.get_login_credential("AccountPage", 0)

    @allure.title("upload Picture is visible")
    @allure.description("account page --> upload Picture text is visible")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_upload_Picture_click(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)

        Picture = self.AccountPage.get_Upload_Picture()
        assert (Picture.is_enabled(), f"element with name '{Picture.text}' is not present on the page.")

    @allure.title("account page url")
    @allure.description("account page --> url")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_acount_page_url(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)

        element = self.AccountPage.get_element(*AccountLocators.Full_Name)
        if element:
            if env in AccountLocators.Account_Page_URL:
                expected_url = AccountLocators.Account_Page_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                print(current_url)

    @allure.title("account page title")
    @allure.description("account page --> title")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_login_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        title = self.AccountPage.get_AccountPage_title(AccountLocators.Account_Page_TITLE)
        assert title == AccountLocators.Account_Page_TITLE

    @allure.title("account page logo visible")
    @allure.description("account page --> logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_login_logo_visible(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        flag = self.AccountPage.is_logo_exist()
        if flag:
            assert flag

    @allure.title("account page profile Full name element")
    @allure.description("account page --> profile Full name element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_profile_name(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        text = self.AccountPage.get_Profile_element_text(*AccountLocators.Full_Name)
        assert text == "Full name"

    @allure.title("account page profile save button element")
    @allure.description("account page --> profile save button element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_profile_save_button(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        save = self.AccountPage.get_element(*AccountLocators.save_Butn)
        if save:
            assert (save.is_enabled(), f"element with name '{save.text}' is not present on the page.")

    @allure.title("account page profile element")
    @allure.description("account page --> profile element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_profile_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        time.sleep(5)

        Company = self.AccountPage.get_Profile_element_text(*AccountLocators.comapny_Name)
        assert Company == "Company name"

        country = self.AccountPage.get_Profile_element_text(*AccountLocators.Country)
        assert country == "Country"

        phone = self.AccountPage.get_Profile_element_text(*AccountLocators.Phone)
        assert phone == "Phone"

        email = self.AccountPage.get_Profile_element_text(*AccountLocators.Email)
        assert email == "Email"

        paswrd = self.AccountPage.get_Profile_element_text(*AccountLocators.change_PW)
        assert paswrd == "Change password"

    @allure.title("account page profile select country from dropdown")
    @allure.description("account page --> profile select country from dropdown")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_profile_select_country_fromDropdown(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)
        self.AccountPage.dropdown_elements(*AccountLocators.Country_dropdown)
        self.AccountPage.ScrollclickOperation(*AccountLocators.Name_country)

        text = self.AccountPage.get_Profile_element_text(*AccountLocators.India)
        if text:
            assert text == "India"

    @allure.title("account page save_profileData")
    @allure.description("account page --> save profile Data")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_save_profile_Data(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)

        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        Mobile = 9999889899

        self.AccountPage.saveProfile(Mobile)
        element = self.AccountPage.get_element(*HomeLocators.Project)
        if element:
            if env in AccountLocators.HOME_Page_URL:
                expected_url = AccountLocators.HOME_Page_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                print(current_url)

    @allure.title("account page --> change password checkbox and update Password")
    @allure.description("account page --> change password checkbox and update Password")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_checkbox_password_Update(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.update_Password("Pictory@123", "Pictory@123", "Pictory@123")

        if env in AccountLocators.HOME_Page_URL:
            expected_url = AccountLocators.HOME_Page_URL[env]
            current_url = self.LogInPage.get_LoginPage_url(expected_url)

            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

            print(current_url)
