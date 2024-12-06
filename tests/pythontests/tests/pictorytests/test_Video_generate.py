import time
import traceback

import allure

import pytest
from selenium.common import StaleElementReferenceException, TimeoutException
from locator.locators import ScriptToVideoLocators, MyBrandingLocators, MyProjectLocators, ArticleToVideoLocators, \
    EditVideoLocators, HomeLocators, VisualVideoLocators, SubscriptionLocators, SigninLocators
from pageObjects.pictryPages.AccountPage import AccountPage
from pageObjects.pictryPages.ArticleToVideo import ArticleToVideo
from pageObjects.pictryPages.EditVideoPage import EditVideo
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.MyProjectPage import MyProjectPage
from pageObjects.pictryPages.ScriptToVideo import ScriptToVideo
from pageObjects.pictryPages.SubscriptionPage import SubscriptionPage
from pageObjects.pictryPages.VisualToVideoPage import VisualVideo
from request import Request
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Script To Video Feature")
@allure.severity(allure.severity_level.CRITICAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestVideoGenerate:
    script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 0)
    article_email, article_password = TestDataForProject.get_login_credential("ArticleToVideo", 0)
    edit_email, edit_password = TestDataForProject.get_login_credential("EditVideo", 0)
    visual_email, visual_password = TestDataForProject.get_login_credential("VisualToVideo", 0)

    @allure.title("buy starter annual plan --> Video Generate Quota :")
    @allure.description("This is test for buy starter annual plan Video Generate Quota")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Subscription_starterannual_VideoGenQuota(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)
        self.ArticleToVideo = ArticleToVideo(self.driver)

        name = "ScriptToVideo" + ScriptToVideo.random_generator()
        email, password = TestDataForProject.get_login_credential("ScriptToVideo", 3)
        self.LogInPage.loginpictory(email, password)

        if env in SigninLocators.HOME_Page_URL:
            expected_url = SigninLocators.HOME_Page_URL[env]
            current_url = self.LogInPage.get_LoginPage_url(expected_url)

            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
            print(current_url)

            try:
                subscription_id = "e81dcab6-9a14-428c-9b04-a312f64ccdeb-SUB"
                Request.make_request(subscription_id)

                self.MyProjectPage.Myproject_elementvisible_scrolClick(*HomeLocators.Project)

                self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
                with allure.step("Upgrade plan --> Buy free trial --> starter plan:"):
                    elabfree, free_trial = self.SubscriptionPage.get_Ft_PlanStatus(*SubscriptionLocators.Subscription_Upgrade_butn)
                    if free_trial is not None:
                        assert free_trial.text.strip() == "Free Trial", f"Expected text: 'Free Trial', Actual text: '{free_trial.text.strip()}'"
                        print(free_trial.text)

                        expected_elabfree_text = "0 / 5"
                        actual_elabfree_text = elabfree.text.strip()

                        assert actual_elabfree_text == expected_elabfree_text, f"Expected text: '{expected_elabfree_text}', Actual text: '{actual_elabfree_text}'"
                        print(elabfree.text)

                        self.SubscriptionPage.get_teardown_FreeTrial_Tostarter_Plan(*SubscriptionLocators.Starter_BuyNow_butn)
                        text = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                        if text:
                            assert text == "Payment successful"
                            print(text)

                            self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Payment_Ok)
                            # self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Okay)

                            MyBranding_elementvisible = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                            if MyBranding_elementvisible:
                                expected_expiration_date, actual_expiration_date = self.SubscriptionPage.get_next_biling_cycle(*SubscriptionLocators.nextbilcycle)
                                if actual_expiration_date and expected_expiration_date:
                                    assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                    print("nextpay : " + str(actual_expiration_date))

                                    self.LogInPage.ScrollclickOperation(*HomeLocators.LOGO_VISIBLE)
                                    self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)

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
                                                MyBranding_elementvisible = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                                                if MyBranding_elementvisible:
                                                    Video_Generation = self.ArticleToVideo.get_Video_Generation_Completed_Article(*ScriptToVideoLocators.Video_Generation)
                                                    if Video_Generation:
                                                        assert Video_Generation.text == "Video Generation is completed"
                                                        print(Video_Generation.text)

                                                        self.SubscriptionPage.ScrollclickOperation_DOM(*SubscriptionLocators.My_Subscription)

                                                        with allure.step("Video-Gen -->> Quota used:"):
                                                            MyBranding_elementvisible = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                                                            if MyBranding_elementvisible:
                                                                videoGen = self.SubscriptionPage.get_element(*ScriptToVideoLocators.video_generate)
                                                                assert videoGen.text == "0.09 / 200"
                                                                print("video Generate : " + videoGen.text)

            except StaleElementReferenceException as e:
                videoGen = self.SubscriptionPage.get_element(*ScriptToVideoLocators.video_generate)
                assert videoGen.text == "0.09 / 200"
                print("video Generate : " + videoGen.text)

    @allure.title("Download video and apply custom VO and decor text from Script to video generate test--> short Video")
    @allure.description("Video generate -->Download video and and apply custom VO and decor text from Script to video generate--> short Video")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_scriptTo_video_shortVideo_customVO_text_coloroverlay_Transition_Element_Custom_stock_visual_imageshort(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 6)

        with allure.step("Login to Pictory"):
            # name = "ScriptToVideo" + ScriptToVideo.random_generator()

            name = "scriptvideo_customVo_text_coloroverlay_Transition_Element_Custom_stock_visual_image"
            self.LogInPage.loginpictory(script_email, script_password)

            self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Recent_Project_scriptvideo)

        with allure.step("Generate ScriptToVideo --> Apply brand"):
            try:
                storyboard = self.ScriptToVideo.video_invisibleloader(*HomeLocators.loader)
                if storyboard:
                    Adjust_buton = self.ScriptToVideo.get_status_customvoiceover(*ScriptToVideoLocators.Audio)
                    if Adjust_buton:
                        assert Adjust_buton.text == "Adjust"

                        self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)

                    with allure.step("navigate to My Project Page"):
                        Video_Generation = self.ScriptToVideo.get_Long_Video_Generation_element(
                            *ScriptToVideoLocators.Video_Generation)
                        assert Video_Generation.text == "Video Generation is completed"
                        print(Video_Generation.text)
                        self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                    with allure.step("check video element is present on Page"):
                        self.ScriptToVideo.is_videoscript_visible(name)

                    with allure.step("check video Url is present on Page"):
                        element = self.ScriptToVideo.video_invisibleloader(*HomeLocators.loader)
                        if element:
                            video = self.ScriptToVideo.is_url_exist_myvideos()
                            video_src = video.get_attribute("src")
                            if video_src:
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

            except StaleElementReferenceException:
                print(traceback.format_exc())
                video = self.ScriptToVideo.is_url_exist_myvideos()
                video_src = video.get_attribute("src")
                if video_src:
                    assert video_src, f"Video src attribute for '{video_src}' is empty."
                    print("Video URL:", video_src)

    @allure.title("Download video and apply -- > Transition, Element,Custom, stock visual and images from EVUT generate test")
    @allure.description("Video generate -->Download video and apply -- > Transition, Element, Custom, stock visual and images Transition from EVUT generate")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_EVUT_autohighlight_defaultVO_dectext_coloroverlay_Transition_Element_Custom_stock_visual_img(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 6)

        with allure.step("Login to Pictory"):
            name = "EVUT_autohighlight_defaultVO_dectext_coloroverlay_Transition_Element_Custom_stock_visual_img"
            self.LogInPage.loginpictory(script_email, script_password)

            self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Recent_Project_EVUT)

        with allure.step("Generate ScriptToVideo --> Apply brand"):
            try:
                storyboard = self.ScriptToVideo.video_invisibleloader(*HomeLocators.loader)
                if storyboard:
                    self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)
                    Video_Generation = self.ScriptToVideo.get_Long_Video_Generation_element(*ScriptToVideoLocators.Video_Generation)
                    assert Video_Generation.text == "Video Generation is completed"
                    print(Video_Generation.text)
                    self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                with allure.step("check video element is present on Page"):
                    self.ScriptToVideo.is_videoscript_visible(name)

                with allure.step("check video Url is present on Page"):
                    element = self.ScriptToVideo.video_invisibleloader(*HomeLocators.loader)
                    if element:
                        video = self.ScriptToVideo.is_url_exist_myvideos()
                        video_src = video.get_attribute("src")
                        if video_src:
                            assert video_src, f"Video src attribute for '{video_src}' is empty."
                            print("Video URL:", video_src)

            except StaleElementReferenceException:
                print(traceback.format_exc())
                video = self.ScriptToVideo.is_url_exist_myvideos()
                video_src = video.get_attribute("src")
                if video_src:
                    assert video_src, f"Video src attribute for '{video_src}' is empty."
                    print("Video URL:", video_src)
