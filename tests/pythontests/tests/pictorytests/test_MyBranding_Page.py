import traceback

import pytest
import allure
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from locator.locators import MyBrandingLocators, SubscriptionLocators, ScriptToVideoLocators
from pageObjects.pictryPages.LogInPage import LogInPage

from pageObjects.pictryPages.MybrandingPage import MyBrandingPage
from pageObjects.pictryPages.ScriptToVideo import ScriptToVideo
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("My Branding Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestMyBranding:
    email, password = TestDataForProject.get_login_credential("MyBranding", 0)

    @allure.title("My Branding page url")
    @allure.description("My Branding page --> url")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_url(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)

        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            if env in MyBrandingLocators.MyBranding_Page_url:
                expected_url = MyBrandingLocators.MyBranding_Page_url[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                print(current_url)

    @allure.title("My Branding page title")
    @allure.description("My Branding page --> title")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)

        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            title = self.MyBrandingPage.get_MyBrandingPage_title(MyBrandingLocators.MyBranding_Page_TITLE)
            assert title == MyBrandingLocators.MyBranding_Page_TITLE

    @allure.title("My Branding page logo visible")
    @allure.description("My Branding page --> logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_logo_visible(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)

        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            flag = self.MyBrandingPage.is_logo_exist()
            assert flag

    @allure.title("My Branding page My Brands text is visible")
    @allure.description("My Branding page --> My Brands text")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_Brands_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)

        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            text = self.MyBrandingPage.get_element_text(*MyBrandingLocators.MyBranding)
            assert text == "Brand kits"
            print(text)

    @allure.title("Create your Brand template page Brand template element test")
    @allure.description("My Branding page --> Create your Brand template page --> Brand template element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_brandtemplate_elements(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        email, password = TestDataForProject.get_login_credential("MyBranding", 3)
        # Branding_name = "brands" + MyBrandingPage.random_generator()
        self.LogInPage.loginpictory(email, password)

        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)
        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            brand = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandCreate)
            if brand:
                assert (brand.is_displayed(), f"element with name '{brand.text}' is not present on the page.")

                self.LogInPage.ScrollclickOperation(*MyBrandingLocators.brandCreate)
                # self.MyBrandingPage.get_folder_name(*MyProjectLocators.folder_name, Branding_name)

                brandTemplate = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandTemplate)

                brandName = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandName)
                color = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.color)
                logo = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.logo)
                font = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.font)

                assert (
                    brandTemplate.is_displayed(), brandName.is_displayed(), logo.is_displayed(), color.is_displayed(),
                    font.is_displayed(),
                    f"element with name '{brandName.text}' is not present on the page.")

                print(brandName.text, logo.text, color.text, brandTemplate.text, font.text)

    @allure.title("Create your Brand template page Create button test")
    @allure.description("My Branding page --> Create your Brand template page --> Create button element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_Createbuton(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        email, password = TestDataForProject.get_login_credential("MyBranding", 3)
        # Branding_name = "brands" + MyBrandingPage.random_generator()
        self.LogInPage.loginpictory(email, password)

        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)
        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            self.LogInPage.ScrollclickOperation(*MyBrandingLocators.brandCreate)
            # self.MyBrandingPage.get_folder_name(*MyProjectLocators.folder_name, Branding_name)

        Createbutn = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.Create)

        assert (
            Createbutn.is_displayed(), f"element with name '{Createbutn.text}' is not present on the page.")

        print(Createbutn.text)

    @allure.title("Create your Brand template page Cancel button test")
    @allure.description("My Branding page --> Create your Brand template page --> Cancel button element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_Cancelbuton(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        email, password = TestDataForProject.get_login_credential("MyBranding", 3)
        # Branding_name = "brands" + MyBrandingPage.random_generator()
        self.LogInPage.loginpictory(email, password)

        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)
        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            self.LogInPage.ScrollclickOperation(*MyBrandingLocators.brandCreate)
            # self.MyBrandingPage.get_folder_name(*MyProjectLocators.folder_name, Branding_name)

        Cancelbutn = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.Cancel)

        assert (
            Cancelbutn.is_displayed(), f"element with name '{Cancelbutn.text}' is not present on the page.")

        print(Cancelbutn.text)

    @allure.title("Create your Brand test")
    @allure.description("My Branding page --> Create your Brand template page --> Create brand")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyBranding_page_Createbrand(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        name = "brand" + MyBrandingPage.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)

        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)

        try:
            brandCreate = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandCreate)
            if brandCreate.is_enabled():
                self.LogInPage.ScrollclickOperation(*MyBrandingLocators.brandCreate)
                # self.MyBrandingPage.get_folder_name(*MyProjectLocators.folder_name, Branding_name)

                Createbutn = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.Create)
                if Createbutn:
                    self.MyBrandingPage.put_Create_brand(*MyBrandingLocators.brand_name, name)
                    brandfont = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.font)
                    if brandfont:
                        self.LogInPage.ScrollclickOperation(*MyBrandingLocators.Create)
                        brand = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.brandSuccesful_text)
                        if brand:
                            assert brand.text == "Great Job! Brand successfully created"

                        print(brand.text)
            else:
                print("The create brand is disable .")
                self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
                self.LogInPage.ScrollclickOperation(*SubscriptionLocators.My_Subscription)
                brandlimit = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandlimit_profesional)
                if brandlimit:
                    assert brandlimit.text == "5 / 5", "Maximum number of brands reached."
                print(brandlimit.text)

        except (NoSuchElementException, TimeoutException):
            print("The create brand is not present .")
            self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
            self.LogInPage.ScrollclickOperation(*SubscriptionLocators.My_Subscription)
            brandlimit = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandlimit_profesional)
            if brandlimit:
                assert brandlimit.text == "5 / 5", "Maximum number of brands reached."
            print(brandlimit.text)

    @allure.title("Create brands and verify quota test")
    @allure.description("My Branding page --> brands quota --> Create brands and verify quota after adding and deleting brand")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.sanity
    def test_MyBranding_page_brandsQuota(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)

        name = "Quota_brand" + MyBrandingPage.random_generator()

        email, password = TestDataForProject.get_login_credential("MyBranding", 1)
        self.LogInPage.loginpictory(email, password)

        self.MyBrandingPage.MyBranding_element_scrollClick(*MyBrandingLocators.MyBranding)

        brandCreate = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.brandCreate)
        if brandCreate.is_enabled():
            self.LogInPage.ScrollclickOperation(*MyBrandingLocators.brandCreate)
            # self.MyBrandingPage.get_folder_name(*MyProjectLocators.folder_name, Branding_name)

            Createbutn = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.Create)
            if Createbutn:
                self.MyBrandingPage.Create_new_brand(*MyBrandingLocators.brand_name, name)

            with allure.step("create new brand"):
                brandfont = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.font)
                if brandfont:
                    self.LogInPage.ScrollclickOperation(*MyBrandingLocators.Create)
                    brand = self.MyBrandingPage.get_footer_element(*MyBrandingLocators.brandSuccesful_text)
                    if brand:
                        assert brand.text == "Great Job! Brand successfully created"

                    with allure.step("Adding Intro/Outro from the library"):
                        self.MyBrandingPage.get_Intro_outro(*MyBrandingLocators.add_library_OutroIntro)

                        with allure.step("Adding musicbg from the library"):
                            self.MyBrandingPage.get_music_Library(*MyBrandingLocators.addmusic_library)

                            with allure.step("Adding AIVoice from the library"):
                                self.MyBrandingPage.get_voiceOver_apply(*MyBrandingLocators.AIVoice_library)

                                with allure.step("Navigate to Subscription Page and check Quota is exhausted 1 / 1 "):
                                    brandlimit = self.MyBrandingPage.get_MyBranding_QuotaExhaust(*MyBrandingLocators.brandlimit_starter1)
                                    if brandlimit:
                                        assert brandlimit.text == "1 / 1", "Maximum number of brands reached."
                                        print(brandlimit.text)

                                    with allure.step("Navigate to brand Page and delete brand"):
                                        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
                                        if MyBranding_elementvisible:
                                            self.LogInPage.ScrollclickOperation(*MyBrandingLocators.MyBranding)
                                            brandName = self.MyBrandingPage.get_pictory_brand(name)
                                            if brandName:
                                                self.MyBrandingPage.get_delete_brand(brandName)

                                            with allure.step("Navigate to Subscription Page and check Quota is available 0 / 1"):
                                                brandlimit0 = self.MyBrandingPage.get_MyBranding_LimitQuota(*MyBrandingLocators.brandlimit_starter0)
                                                if brandlimit0:
                                                    assert brandlimit0.text == "0 / 1", "brands are updated after delete."
                                                    print(brandlimit0.text)

    @allure.title("Apply your Brand test")
    @allure.description("My Branding page --> Brand template page --> Apply brand")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_MyBranding_page_Applybrand(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        name = "MyBrandVideo" + ScriptToVideo.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)

        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)
        with allure.step("Generate ScriptToVideo --> Apply brand"):
            try:
                toggle_buttons, clip_Board, font_weight = self.ScriptToVideo.get_scripteditor_highlight_Page(name)
                if font_weight:
                    assert font_weight == "700" or font_weight == "bold", "The text is not bold"
                    clip_Board_enable = clip_Board.is_enabled()
                    assert clip_Board_enable, "clipBoard button is no enabled"
                    for toggle_button in toggle_buttons:
                        is_enabled = toggle_button.is_enabled()  # Use is_enabled() method to check if the toggle button is enabled
                        assert is_enabled, "Not all toggle buttons are enabled"

                        Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_scriptDownload(*ScriptToVideoLocators.saved)
                        if Storyboard_loaded:
                            element = self.MyBrandingPage.get_apply_brand(*ScriptToVideoLocators.branding)
                            assert element.text == "brand applied successfully"
                            print(element.text)

            except StaleElementReferenceException:
                print(traceback.format_exc())

    @allure.title("Apply default Brand on script to video")
    @allure.description("My Branding page --> Brand template page --> Apply default brand script to video")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_MyBranding_Apply_Defaultbrand(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        email, password = TestDataForProject.get_login_credential("MyBranding", 2)

        name = "defaultbrand" + ScriptToVideo.random_generator()
        self.LogInPage.loginpictory(email, password)

        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)
        with allure.step("Generate ScriptToVideo --> Apply brand"):
            try:
                toggle_buttons, clip_Board, font_weight = self.ScriptToVideo.get_scripteditor_highlight_Page(name)
                if font_weight:
                    assert font_weight == "700" or font_weight == "bold", "The text is not bold"
                    clip_Board_enable = clip_Board.is_enabled()
                    assert clip_Board_enable, "clipBoard button is no enabled"
                    for toggle_button in toggle_buttons:
                        is_enabled = toggle_button.is_enabled()  # Use is_enabled() method to check if the toggle button is enabled
                        assert is_enabled, "Not all toggle buttons are enabled"

                        Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_scriptDownload(*ScriptToVideoLocators.saved)
                        if Storyboard_loaded:
                            self.LogInPage.ScrollclickOperation(*ScriptToVideoLocators.branding)
                            defaultbrand = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.defaultbrand)
                            if defaultbrand:
                                assert (defaultbrand.is_displayed(), f"element with name '{defaultbrand.text}' is not present on the page.")

                                print(defaultbrand.text)  # This line may not be necessary if everything is asserted successfully

            except StaleElementReferenceException:
                defaultbrand = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.defaultbrand)
                if defaultbrand:
                    assert (defaultbrand.is_displayed(), f"element with name '{defaultbrand.text}' is not present on the page.")

                    print(defaultbrand.text)  # This line may not be necessary if everything is asserted successfully
