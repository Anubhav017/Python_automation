import allure
import pytest

from locator.locators import HomeLocators, AccountLocators
from pageObjects.pictryPages.AccountPage import AccountPage
from pageObjects.pictryPages.HomePage import HomePage
from pageObjects.pictryPages.LogInPage import LogInPage
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("home page Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestHome:
    email, password = TestDataForProject.get_login_credential("Home", 0)

    @allure.title("Home page url")
    @allure.description("Home page --> url")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Home_page_url(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.AccountPage.get_element(*HomeLocators.Project)
        if element:
            if env in AccountLocators.HOME_Page_URL:
                expected_url = AccountLocators.HOME_Page_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                print(current_url)

    @allure.title("Home page title")
    @allure.description("Home page --> title")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Home_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        title = self.HomePage.get_HomePage_title(HomeLocators.HOME_Page_TITLE)
        assert title == HomeLocators.HOME_Page_TITLE

    @allure.title("Home page logo visible")
    @allure.description("Home page --> logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Home_logo_visible(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        flag = self.HomePage.is_logo_exist()
        assert flag

    @allure.title("Home page recent Project text is visible")
    @allure.description("Home page --> recent Project text")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Home_page_recent_Project_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        text = self.HomePage.get_element_text(*HomeLocators.recent_Project)
        assert text == "Recent projects"

    @allure.title("Home page Project text test")
    @allure.description("Home page --> Project text")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Home_page_Project_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        text = self.HomePage.get_element_text(*HomeLocators.Project)
        assert text == "Projects"
        print(text)

    @allure.title("Home page recent Project text is visible")
    @allure.description("Home page --> recent Project text")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Home_page_demo_Project_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        email, password = TestDataForProject.get_login_credential("Home", 1)

        self.LogInPage.loginpictory(email, password)
        elements = self.HomePage.get_elements(*HomeLocators.Demo)

        element_texts = [element.text for element in elements]
        assert all(text == "Demo Project" for text in element_texts), f"Not all elements have the expected text 'Demo Project'. Found texts: {element_texts}"

        assert len(elements) == 4, f"Expected 4 occurrences of 'Demo Project', but found {len(elements)}."

    @allure.title("video generate elements test")
    @allure.description("Home page --> video generate elements text")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Home_page_video_gen_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        with allure.step("Check if Script to video element is present of home page"):
            script = self.HomePage.get_video_text(*HomeLocators.ScriptToVideo)
            if script:
                assert script == "Text to video"
                print(script)

        with allure.step("Check if article to video element is present of home page"):
            article = self.HomePage.get_video_text(*HomeLocators.BlogToVideo)
            if article:
                assert article == "URL to video"
                print(article)

        with allure.step("Check if edit to video element is present of home page"):
            edit = self.HomePage.get_video_text(*HomeLocators.editVideo)
            if edit:
                assert edit == "AI video editor"
                print(edit)

        with allure.step("Check if visual to video element is present of home page"):
            visual = self.HomePage.get_video_text(*HomeLocators.VisualToVideo)
            if visual:
                assert visual == "Images to video"
                print(visual)

        with allure.step("Check if ppt to video element is present of home page"):
            PPT = self.HomePage.get_video_text(*HomeLocators.PptToVideo)
            if PPT:
                assert PPT == "PPT to video"
                print(PPT)

    @allure.title("User profile name text test")
    @allure.description("Home page --> User profile name text")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Home_page_UserProfile_name(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        text = self.HomePage.get_element_text(*HomeLocators.profileName)
        assert text == "Hello! Click one of the boxes below to create a new video"
        print(text)

    @allure.title("User profile elements test")
    @allure.description("Home page --> User profile elements visible")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Home_page_UserProfile_elements(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.LogInPage.clickOperation(*HomeLocators.hover_Profile)

        account = self.HomePage.get_element_DOM(*HomeLocators.My_account)
        Subscription = self.HomePage.get_element_DOM(*HomeLocators.My_Subscription)
        Affiliate_dash = self.HomePage.get_element_DOM(*HomeLocators.Affiliate_dash)
        logout = self.HomePage.get_element_DOM(*HomeLocators.logout)

        assert account.text == "My account" and Subscription.text == "My subscription" and Affiliate_dash.text == "Affiliate dashboard" and logout.text == "Log out"

    @allure.title("Home page Discover Quick start video tutorial link test")
    @allure.description("Home page --> Discover Quick start video tutorial link ")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.Regression
    def test_Home_page_Discover_Quick_start_video_tutorial_link(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        text = self.HomePage.get_element_text(*HomeLocators.discovr)
        assert text == "Discover"
        print(text)

        self.LogInPage.clickOperation(*HomeLocators.dislink)

        original_window_handle = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != original_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        if env == "dev":
            expected_url = HomeLocators.DEV_Discovr_PAGE_URL

        elif env == "staging":
            expected_url = HomeLocators.DEV_Discovr_PAGE_URL

        elif env == "prod":
            expected_url = HomeLocators.DEV_Discovr_PAGE_URL

        current_url = self.LogInPage.get_LoginPage_url(expected_url)
        assert current_url == expected_url
        print(current_url)

        self.driver.switch_to.window(original_window_handle)

    @allure.title("Home page Discover tips link test")
    @allure.description("Home page --> Discover tips link ")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.Regression
    def test_Home_page_Discover_tips_link(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        text = self.HomePage.get_element_text(*HomeLocators.discovr)
        assert text == "Discover"
        print(text)

        self.LogInPage.clickOperation(*HomeLocators.tiplink)

        original_window_handle = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != original_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        if env == "dev":
            expected_url = HomeLocators.DEV_tips_PAGE_URL

        elif env == "staging":
            expected_url = HomeLocators.DEV_tips_PAGE_URL

        elif env == "prod":
            expected_url = HomeLocators.DEV_tips_PAGE_URL

        current_url = self.LogInPage.get_LoginPage_url(expected_url)
        assert current_url == expected_url
        print(current_url)

        self.driver.switch_to.window(original_window_handle)
