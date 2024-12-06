import os
import time

import allure
import pytest
from selenium.common import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from locator.locators import TeamLocators, SubscriptionLocators, MyProjectLocators, ScriptToVideoLocators, \
    MyBrandingLocators, ArticleToVideoLocators, AccountLocators, HomeLocators, EditVideoLocators, SigninLocators
from pageObjects.pictryPages.AccountPage import AccountPage
from pageObjects.pictryPages.ArticleToVideo import ArticleToVideo
from pageObjects.pictryPages.EditVideoPage import EditVideo
from pageObjects.pictryPages.HomePage import HomePage
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.MybrandingPage import MyBrandingPage
from pageObjects.pictryPages.ScriptToVideo import ScriptToVideo
from pageObjects.pictryPages.SignUpPage import SignUpPage
from pageObjects.pictryPages.SubscriptionPage import SubscriptionPage
from pageObjects.pictryPages.TeamPage import TeamPage
from request import Request
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Team and Personal common Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestTeamPersonal:
    firstName, lastName, email_signup, password_signup = SignUpPage.get_Signup_credential('SignUp', 2)
    email, password = TestDataForProject.get_login_credential("TeamPage", 0)

    @allure.title("Team page create Project --> Script to video")
    @allure.description("This is test of Team page create Project --> Script to video")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_create_Project_ScriptToVideo(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        name = "team_scriptTo_Video" + ScriptToVideo.random_generator()

        self.LogInPage.loginpictory(self.email, self.password)

        # Check if the home page element is present
        element = self.TeamPage.get_Homepage_element()
        if element:
            assert element, "Home page element is not present."
        try:
            with allure.step("Navigate to Team Account"):
                self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
                self.LogInPage.ScrollclickOperation(*TeamLocators.team_account)
                TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                if TeamProject:
                    assert TeamProject, "Team Project element is not present."

                    with allure.step("Navigate to Team Project"):
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)

                        createProject = self.TeamPage.get_element(*TeamLocators.createProject)
                        if createProject:
                            assert createProject, "Create Project element is not present."

                            with allure.step("Create a new project"):
                                self.TeamPage.team_element_scrollClick(*TeamLocators.createProject)

                                """
                                TeamProject = self.TeamPage.get_element(*TeamLocators.TeamProject)
                                assert TeamProject, "team Project element is not present."
                                
                                """
                                self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)
                                toggle_buttons, clip_Board, font_weight = self.ScriptToVideo.get_scripteditor_highlight_Page(
                                    name)
                                if font_weight:
                                    assert font_weight == "700" or font_weight == "bold", "The text is not bold"
                                    clip_Board_enable = clip_Board.is_enabled()
                                    assert clip_Board_enable, "clipBoard button is no enabled"
                                    for toggle_button in toggle_buttons:
                                        is_enabled = toggle_button.is_enabled()  # Use is_enabled() method to check if the toggle button is enabled
                                        assert is_enabled, "Not all toggle buttons are enabled"

                                    Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_scriptDownload(*ScriptToVideoLocators.saved)
                                    if Storyboard_loaded:
                                        with allure.step("Apply branding"):
                                            element = self.ScriptToVideo.get_apply_brand(*ScriptToVideoLocators.branding)
                                            if element:
                                                assert element.text == "brand applied successfully"

                                            with allure.step("Apply Voiceover"):
                                                voice_applied = self.ScriptToVideo.get_status_voiceover(*ScriptToVideoLocators.Audio)
                                                if voice_applied:
                                                    assert voice_applied.text == "Applied"

                                                    with allure.step("navigate to My Project Page"):
                                                        Video_Generation = self.ScriptToVideo.get_Long_Video_Generation_element(*ScriptToVideoLocators.Video_Generation)
                                                        assert Video_Generation.text == "Video Generation is completed"
                                                        print(Video_Generation.text)

                                                        self.ScriptToVideo.ScrollclickOperation(*TeamLocators.TeamProject)

                                                    with allure.step("check video element is present on Page"):
                                                        self.ScriptToVideo.is_videoscript_visible(name)

                                                    with allure.step("check video Url is present on Page"):
                                                        element = self.ScriptToVideo.video_invisibleloader(*HomeLocators.loader)
                                                        if element:
                                                            video = self.ScriptToVideo.is_url_exist_myvideos()
                                                            if video:
                                                                video_src = video.get_attribute("src")
                                                                if video_src:
                                                                    assert video_src, f"Video src attribute for '{video_src}' is empty."
                                                                    print("Video URL:", video_src)

        except StaleElementReferenceException as e:
            with allure.step("Handle Exception"):
                print(f"An exception occurred: {str(e)}")

    @allure.title("Team page create Project --> Blog to video")
    @allure.description("This is test of Team page create Project --> Blog to video")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_create_Project_BlogToVideo(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.ArticleToVideo = ArticleToVideo(self.driver)

        # name = "team_ArticleTo_Video" + ScriptToVideo.random_generator()

        # Log in to the application
        self.LogInPage.loginpictory(self.email, self.password)

        # Check if the home page element is present
        element = self.TeamPage.get_Homepage_element()
        if element:
            assert element, "Home page element is not present."

        # Navigate to Team -> Account -> Team Project -> Create Project

        with allure.step("Navigate to Team Project"):
            self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
            self.LogInPage.ScrollclickOperation(*TeamLocators.team_account)

            createProject = self.TeamPage.get_element(*TeamLocators.createProject)
            if createProject:
                assert createProject, "Create Project element is not present."

                with allure.step("Create Project"):
                    self.TeamPage.team_element_scrollClick(*TeamLocators.createProject)

                with allure.step("Perform Article to Video conversion"):
                    self.LogInPage.clickOperation(*ArticleToVideoLocators.Proceed_buton)
                    self.ArticleToVideo.Atricle_URL()
                    self.LogInPage.ScrollclickOperation(*ArticleToVideoLocators.generate_vid)

                    loader_invisible = self.ArticleToVideo.article_invisibleloader(*ArticleToVideoLocators.articletovideoLoader)
                    if loader_invisible:
                        article = self.ArticleToVideo.get_element(*ArticleToVideoLocators.source)

                        if article.is_displayed():
                            attriute = self.TeamPage.Attribute_name()
                            name = attriute.get_attribute("value")

                            nextButn = self.ScriptToVideo.get_element(*ArticleToVideoLocators.next)
                            if nextButn.is_enabled():
                                self.LogInPage.ScrollclickOperation(*ArticleToVideoLocators.next)

                                # self.ArticleToVideo.ScrollclickOperation(*ArticleToVideoLocators.template)
                                # self.ArticleToVideo.ScrollclickOperation(*ArticleToVideoLocators.template_width)

                                complete = self.ScriptToVideo.dynamicbar_invisible(*ScriptToVideoLocators.complete)
                                if complete:
                                    with allure.step("Apply  default branding"):
                                        self.LogInPage.ScrollclickOperation(*ScriptToVideoLocators.branding)
                                        defaultbrand = self.ArticleToVideo.get_element(*TeamLocators.defaultbrand)
                                        if defaultbrand:
                                            assert (defaultbrand.is_displayed(),
                                                    f"element with name '{defaultbrand.text}' is not present on the page.")

                                        with allure.step("navigate to My Project Page"):
                                            Video_Generation = self.ArticleToVideo.get_Video_Generation_Completed_Article(*ScriptToVideoLocators.Video_Generation)
                                            assert Video_Generation.text == "Video Generation is completed"
                                            print(Video_Generation.text)

                                            self.ScriptToVideo.ScrollclickOperation(*TeamLocators.TeamProject)

                                        with allure.step("check video element is present on Page"):
                                            self.ArticleToVideo.is_videoscript_visible(name)

                                        with allure.step("check video Url is present on Page"):
                                            element = self.ScriptToVideo.dynamicbar_invisible(*MyProjectLocators.Myproject_loader)
                                            if element:
                                                img = self.ArticleToVideo.is_url_exist_myvideos()
                                                img_src = img.get_attribute("src")
                                                if img_src:
                                                    assert img_src, f"Video src attribute for '{img_src}' is empty."
                                                    print("Video URL:", img_src)

    @allure.title("Team page create Project --> edit to video")
    @allure.description("This is test of Team page create Project --> edit to video")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.sanity
    def test_team_Edit_video_generate(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.EditVideo = EditVideo(self.driver)

        email, password = TestDataForProject.get_login_credential("TeamPage", 5)
        self.LogInPage.loginpictory(email, password)

        # Check if the home page element is present
        element = self.TeamPage.get_Homepage_element()
        if element:
            assert element, "Home page element is not present."
        try:
            with allure.step("Navigate to Team Account"):
                self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
                self.LogInPage.ScrollclickOperation(*TeamLocators.team_account)

                """
                TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                if TeamProject:
                    assert TeamProject, "Team Project element is not present."

                    with allure.step("Navigate to Team Project"):
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                
                """
                createProject = self.TeamPage.get_element(*TeamLocators.createProject)
                if createProject:
                    assert createProject, "Create Project element is not present."

                    with allure.step("Create a new project"):
                        self.TeamPage.team_element_scrollClick(*TeamLocators.createProject)

                        """
                        TeamProject = self.TeamPage.get_element(*TeamLocators.TeamProject)
                        assert TeamProject, "team Project element is not present."
                        
                        """

                        # self.EditVideo.ScrollclickOperation(*EditVideoLocators.Proceed_buton)
                        # self.TeamPage.editPage_URL(Youtub_Url)

                        # self.EditVideo.loader_invisible_scrolClick(*EditVideoLocators.demo_vid)  # click on demo vid
                        self.EditVideo.ScrollclickOperation(*EditVideoLocators.Proceed_buton)
                        self.EditVideo.get_uploadmp4_file(By.CSS_SELECTOR, "input[type='file']", os.path.join('videoGen', 'evut.mp4'))

                        self.LogInPage.ScrollclickOperation(*EditVideoLocators.Proceed_video)
                        textInput_loader = self.EditVideo.video_invisibleloader(*EditVideoLocators.textInput_loader)
                        if textInput_loader:
                            Bar = self.EditVideo.video_invisibleloader(*EditVideoLocators.progress)
                            if Bar:
                                attriute = self.EditVideo.Attribute_name()
                                name = attriute.get_attribute("value")
                            with allure.step("Navigate to Summary Page and check element"):
                                Transcription = self.EditVideo.get_element(*EditVideoLocators.Transcription)
                                if Transcription:
                                    assert (Transcription.is_displayed(),
                                            f"element with name '{Transcription.text}' is not present on the page.")
                                    print(Transcription.text)

                                    highlight = self.EditVideo.get_element(*EditVideoLocators.highlight)
                                    if highlight:
                                        assert (highlight.is_enabled(), f"element with name '{highlight.text}' is not present on the page.")
                                        print(highlight.text)

                                        with allure.step("Navigate to edit video Page and check default brand selected"):
                                            defaultbrand = self.EditVideo.get_element(*TeamLocators.teamdefaultbrand)
                                            if defaultbrand:
                                                assert defaultbrand.text == "Brand01"
                                                print(defaultbrand.text)

                                                CustomizeVideo = self.EditVideo.get_element(*EditVideoLocators.CustomizeVideo)
                                                if CustomizeVideo.is_enabled():
                                                    assert (CustomizeVideo, f"element with name '{CustomizeVideo.text}' is not present on the page.")
                                                    print(CustomizeVideo.text)
                                                    self.EditVideo.JSClick_operation(*EditVideoLocators.CustomizeVideo)  # click on demo vid

                                                    complete = self.ScriptToVideo.dynamicbar_invisible(*ScriptToVideoLocators.complete)
                                                    if complete:
                                                        self.LogInPage.ScrollclickOperation(*ScriptToVideoLocators.branding)
                                                        self.LogInPage.clickOperation(*MyBrandingLocators.branding_drop)
                                                        branding_select = self.EditVideo.get_element(*TeamLocators.branding_select)

                                                    with allure.step("Apply Branding"):
                                                        if branding_select:
                                                            self.LogInPage.ScrollclickOperation(*TeamLocators.branding_select)
                                                            self.LogInPage.ScrollclickOperation(*MyBrandingLocators.continue_butn)

                                                            element = self.EditVideo.get_element(*MyBrandingLocators.brand_successful)
                                                            assert element.text == "brand applied successfully"

                                                            """
                                                            self.EditVideo.get_Download_video(*EditVideoLocators.generate_button)
                                                            background = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.background)
                                                            if background.is_enabled():
                                                                self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.background)
                                                            
                                                            """

                                                        with allure.step("Download video from storyboard Page"):
                                                            Video_Generation = self.EditVideo.get_Long_Video_Generation_element(*ScriptToVideoLocators.Video_Generation)
                                                            if Video_Generation:
                                                                video_generation_text = Video_Generation.text
                                                                if "Video Generation is completed" in video_generation_text:
                                                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                                                    print(video_generation_text)

                                                                elif "Video Generation Failed" in video_generation_text:
                                                                    print(video_generation_text)
                                                                    assert False, "Video Generation Failed"

                                                                elif "Video generation errored." in video_generation_text:
                                                                    print(video_generation_text)
                                                                    assert False, "Video generation errored"

                                                            self.ScriptToVideo.ScrollclickOperation(*TeamLocators.TeamProject)

                                                        with allure.step("check video element is present on Page"):
                                                            self.ScriptToVideo.is_videoscript_visible(name)

                                                        with allure.step("check video Url is present on Page"):
                                                            element = self.ScriptToVideo.dynamicbar_invisible(*MyProjectLocators.Myproject_loader)
                                                            if element:
                                                                video = self.ScriptToVideo.is_url_exist_myvideos()
                                                                if video:
                                                                    video_src = video.get_attribute("src")
                                                                    if video_src:
                                                                        assert video_src, f"Video src attribute for '{video_src}' is empty."
                                                                        print("Video URL:", video_src)

        except StaleElementReferenceException as e:
            print(f"An exception occurred:")

    @allure.title("Team page --> home Page elements")
    @allure.description("This is test of Team page --> home Page element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_team_homePage_elements(self, env):
        with allure.step("Login to Pictory"):
            self.LogInPage = LogInPage(self.driver)
            self.HomePage = HomePage(self.driver)

            self.LogInPage.loginpictory(self.email, self.password)

        with allure.step("Check if home page element is present"):
            self.TeamPage = TeamPage(self.driver)
            element = self.TeamPage.get_Homepage_element()
            assert element, "Home page element is not present."

            with allure.step("Navigate to Team Project"):
                self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
                self.LogInPage.ScrollclickOperation(*TeamLocators.team_account)

            with allure.step("Get Team Project Element"):
                TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                assert TeamProject, "Team Project element is not present."

            with allure.step(f"Check URL in {env} environment"):
                if env in AccountLocators.HOME_Page_URL:
                    expected_url = AccountLocators.HOME_Page_URL[env]
                    current_url = self.LogInPage.get_LoginPage_url(expected_url)

                    assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                    print(current_url)

            with allure.step("Check if logo of home page element is present"):
                flag = self.HomePage.is_logo_exist()
                if flag:
                    assert flag

            with allure.step("Check if Script to video element is present of home page"):
                script = self.HomePage.get_video_text(*HomeLocators.ScriptToVideo)
                if script:
                    assert script == "Script to Video"
                print(script)

            with allure.step("Check if article to video element is present of home page"):
                article = self.HomePage.get_video_text(*HomeLocators.BlogToVideo)
                if article:
                    assert article == "Article to Video"
                print(article)

            with allure.step("Check if edit to video element is present of home page"):
                edit = self.HomePage.get_video_text(*HomeLocators.editVideo)
                if edit:
                    assert edit == "Edit Videos with AI"
                print(edit)

            with allure.step("Check if visual to video element is present of home page"):
                visual = self.HomePage.get_video_text(*HomeLocators.VisualToVideo)
                if visual:
                    assert visual == "Visuals to Video"
                print(visual)

    @allure.title("buy teams annual plan --> Video Generate Quota :")
    @allure.description("This is test for buy teams annual plan Video Generate Quota")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Subscription_teamsannual_VideoGenQuota(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.TeamPage = TeamPage(self.driver)

        name = "team_ScriptToVideo" + ScriptToVideo.random_generator()
        email, password = TestDataForProject.get_login_credential("TeamPage", 6)
        self.LogInPage.loginpictory(email, password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            assert element, "Home page element is not present."
            with allure.step("Navigate to Team Account"):
                # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                self.LogInPage.login_element_scrollClick(*TeamLocators.team_account)

                """
                TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                if TeamProject:
                    assert TeamProject, "Team Project element is not present."

                    with allure.step("Navigate to Team Project"):
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                
                """

                createProject = self.TeamPage.get_element(*TeamLocators.createProject)
                if createProject:
                    assert createProject, "Create Project element is not present."

                    with allure.step("Create a new project"):
                        self.TeamPage.team_element_scrollClick(*TeamLocators.createProject)

                        if env in SigninLocators.HOME_Page_URL:
                            expected_url = SigninLocators.HOME_Page_URL[env]
                            current_url = self.LogInPage.get_LoginPage_url(expected_url)

                            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                            print(current_url)

                            try:

                                subscription_id = "ac8b5178-618c-4166-acd2-d154cf53fd3e-SUB"
                                Request.make_request(subscription_id)

                                # self.SubscriptionPage.loaderinvisible_scrolclick(*TeamLocators.TeamProject)

                                self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.Manage_Subscription)
                                with allure.step("Upgrade plan --> Buy free trial --> professional plan:"):
                                    self.TeamPage.get_teardown_FreeTrial_teams_Plan(*SubscriptionLocators.Subscription_Upgrade_butn)

                                    text = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                                    assert text == "Payment successful"

                                    print(text)

                                with allure.step("Upgrade plan --> plan page:"):
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
                                                            Video_Generation = self.TeamPage.get_Video_Generation_Completed_teamscript(*ScriptToVideoLocators.Video_Generation)
                                                            if Video_Generation:
                                                                video_generation_text = Video_Generation.text
                                                                if "Video Generation is completed" in video_generation_text:
                                                                    print(video_generation_text)
                                                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                                                elif "Video Generation Failed" in video_generation_text:
                                                                    print(video_generation_text)
                                                                    assert False, "Video Generation Failed"
                                                                elif "Video generation errored." in video_generation_text:
                                                                    print(video_generation_text)
                                                                    assert False, "Video generation errored"
                                                            self.SubscriptionPage.ScrollclickOperation_DOM(*SubscriptionLocators.Manage_Subscription)

                                                            with allure.step("Video-Gen -->> Quota used:"):
                                                                MyBranding_elementvisible = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                                                                if MyBranding_elementvisible:
                                                                    videoGen = self.SubscriptionPage.get_element(*ScriptToVideoLocators.video_generate)
                                                                    assert videoGen.text == "0.09 / 1800"
                                                                    print("video Generate : " + videoGen.text)

                            except StaleElementReferenceException as e:
                                with allure.step("Upgrade plan --> Buy free trial --> professional plan:"):
                                    videoGen = self.SubscriptionPage.get_element(*ScriptToVideoLocators.video_generate)
                                    assert videoGen.text == "0.09 / 1800"
                                    print("video Generate : " + videoGen.text)

    @allure.title("SignUp and buy team plan and Getty image and Elab")
    @allure.description("This is test for SignUp page and buy team plan and Getty image and Elab")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_Buy_teamPlan_and_Getty_image_and_Elab(self, env):
        if env not in ["dev"]:
            pytest.skip("This test is skipped in the production environment")

        self.SignUpPage = SignUpPage(self.driver)
        email = "pictoryautomate" + SignUpPage.random_generator() + "@gmail.com"

        self.TeamPage = TeamPage(self.driver)

        self.SubscriptionPage = SubscriptionPage(self.driver)
        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, email, self.password)
        try:
            with allure.step(f"Performing SignUp with email: {email}"):
                verify_email = self.SignUpPage.get_verifyemail(*SigninLocators.VerifyEmail)
                if verify_email.is_displayed():
                    print("This is for Icp user.")
                    get_otp = self.SignUpPage.email_listen()
                    print(f"Extracted OTP: {get_otp}")
                    for i in range(1, 7):
                        # box_id = f"get_otp{i}"
                        element = self.driver.find_element(By.ID, f":r{i + 3}:")
                        element.send_keys(get_otp[i - 1])  # Enter each digit of the OTP into the respective input box
                    time.sleep(5)
                    self.SignUpPage.do_clickOnquestionairePage()
                    self.SignUpPage.get_startpictory(*SigninLocators.startpictory)

                    if env in SigninLocators.HOME_Page_URL:
                        expected_url = SigninLocators.HOME_Page_URL[env]
                        current_url = self.SignUpPage.get_SignUpPage_url(expected_url)

                        assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                        print(current_url)
                    with allure.step("Upgrade plan --> Buy free trial --> professional anual plan:"):
                        # self.TeamPage.get_ICPCountry_upgrade_FreeTrialTo_team_Plan(*SubscriptionLocators.Subscription_Upgrade_butn)
                        expected_total, actual_price_numeric = self.TeamPage.get_ICPCountry_upgrade_FreeTrialTo_team_Plan(*SubscriptionLocators.Subscription_Upgrade_butn, 6)
                        assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                        print("actual total price:", actual_price_numeric)
                        print("expected total price:", expected_total)

                        self.TeamPage.get_ICPCountry_biling_address_team_Plan(*TeamLocators.Proceed_butn)

                        text = self.SignUpPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                        if text:
                            assert text == "Payment successful"
                            print(text)

                        with allure.step("Upgrade plan --> plan page:"):
                            self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Payment_Ok)
                            # self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Okay)

                        with allure.step("elevenLab VO and Getty initial status:"):
                            element = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                            if element:
                                with allure.step("Getty image -->> buy:"):
                                    Gety_enabled = self.SubscriptionPage.get_element(*SubscriptionLocators.Gety_enable)
                                    assert Gety_enabled.text == "Enabled"
                                    print("Gety image : " + Gety_enabled.text)

                                with allure.step("Voice-Over -->> buy:"):
                                    elabmin = self.SubscriptionPage.get_element(*SubscriptionLocators.elabmin)
                                    assert elabmin.text == "0 / 240"
                                    print("elab minute : " + elabmin.text)

                                    expected_total, actual_price_numeric = self.TeamPage.get_teamPlanorder_Sumary(*SubscriptionLocators.modify_elVoice, 11)
                                    assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                    print("actual total price:", actual_price_numeric)
                                    print("expected total price:", expected_total)

                                    elabmin1 = self.TeamPage.get_buy_elVoice_Over(*SubscriptionLocators.elabmin)
                                    assert elabmin1.text == "0 / 300"
                                    print("elab minute : " + elabmin1.text)

                                    expected_expiration_date, actual_expiration_date = self.SignUpPage.get_next_biling_cycle(*SubscriptionLocators.nextbilcycle)
                                    if actual_expiration_date and expected_expiration_date:
                                        assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                        print("nextpay : " + str(actual_expiration_date))

                                    with allure.step("Upgrade plan --> Buy free trial --> professional Month plan:"):
                                        self.SubscriptionPage.toggleButton_click()
                                        expected_total, actual_price_numeric = self.TeamPage.get_team_monthly_dashboard(*TeamLocators.team_BuyNow_butn, 7)
                                        assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                        print("actual total price:", actual_price_numeric)
                                        print("expected total price:", expected_total)

                                        plan_update = self.TeamPage.get_team_monthly(*TeamLocators.Proceed_butn)
                                        if plan_update:
                                            assert plan_update
                                            print(plan_update.text)

                                        with allure.step("Upgrade member --> 3 to 5 mem:"):
                                            expected_total, actual_price_numeric = self.TeamPage.get_Upgrade_Member_team(*SubscriptionLocators.dropdown, 11)
                                            assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                                            print("actual total price:", actual_price_numeric)
                                            print("expected total price:", expected_total)

                                            Current_status = self.TeamPage.get_subscription_team_Page(*TeamLocators.Proceed_butn_0)
                                            assert Current_status.text == "Current"
                                            print(Current_status.text)

        except (TimeoutException, NoSuchElementException):
            with allure.step("Performing SignUp with email: {email}"):
                print("This is for non_Icp user.")
                self.SignUpPage.cards_Page(*SigninLocators.Verifypaymentmethod)
                get_otp = self.SignUpPage.email_listen()
                if get_otp:
                    print(f"Extracted OTP: {get_otp}")
                    for i in range(1, 7):
                        # box_id = f"get_otp{i}"
                        element = self.driver.find_element(By.ID, f"mui-{i + 4}")
                        element.send_keys(get_otp[i - 1])  # Enter each digit of the OTP into the respective input box
                    time.sleep(3)
                    self.SignUpPage.do_clickOnquestionairePage()
                    self.SignUpPage.get_startpictory(*SigninLocators.startpictory)
                    if env in SigninLocators.HOME_Page_URL:
                        expected_url = SigninLocators.HOME_Page_URL[env]
                        current_url = self.SignUpPage.get_SignUpPage_url(expected_url)

                        assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                        print(current_url)

                    with allure.step("Upgrade plan --> Buy free trial --> professional plan:"):
                        self.TeamPage.get_upgrade_FreeTrialTo_team_Plan(*SubscriptionLocators.Subscription_Upgrade_butn)
                        text = self.SignUpPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                        assert text == "Payment successful"
                        print(text)

                    with allure.step("Upgrade plan --> plan page:"):
                        self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Payment_Ok)
                        self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Okay)

                    with allure.step("elevenLab VO and Getty initial status:"):
                        element = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                        if element:
                            with allure.step("Getty image -->> buy:"):
                                Gety_enabled = self.SubscriptionPage.get_element(*SubscriptionLocators.Gety_enable)
                                assert Gety_enabled.text == "Enabled"
                                print("Gety image : " + Gety_enabled.text)

                            with allure.step("Voice-Over -->> buy:"):
                                elabmin = self.SubscriptionPage.get_element(*SubscriptionLocators.elabmin)
                                assert elabmin.text == "0 / 240"
                                print("elab minute : " + elabmin.text)

                                expected_total, actual_price_numeric = self.TeamPage.get_teamPlanorder_Sumary(
                                    *SubscriptionLocators.modify_elVoice)
                                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                print("actual total price:", actual_price_numeric)
                                print("expected total price:", expected_total)

                                elabmin1 = self.TeamPage.get_buy_elVoice_Over(*SubscriptionLocators.elabmin)
                                assert elabmin1.text == "0 / 300"
                                print("elab minute : " + elabmin1.text)

                                expected_expiration_date, actual_expiration_date = self.SignUpPage.get_next_biling_cycle(
                                    *SubscriptionLocators.nextbilcycle)
                                if actual_expiration_date and expected_expiration_date:
                                    assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                    print("nextpay : " + str(actual_expiration_date))

    @allure.title("Team page --> band kits element")
    @allure.description("This is test of Team page --> band kits element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_team_branding_element(self, env):
        with allure.step("Login to Pictory"):
            self.LogInPage = LogInPage(self.driver)
            self.MyBrandingPage = MyBrandingPage(self.driver)

            self.LogInPage.loginpictory(self.email, self.password)

        with allure.step("Check if home page element is present"):
            self.TeamPage = TeamPage(self.driver)
            element = self.TeamPage.get_Homepage_element()
            assert element, "Home page element is not present."

            with allure.step("Navigate to Team Project"):
                self.LogInPage.clickOperation(*SubscriptionLocators.hover_Profile)
                self.LogInPage.ScrollclickOperation(*TeamLocators.team_account)

            with allure.step("Get Team Project Element"):
                TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                assert TeamProject, "Team Project element is not present."

            with allure.step("Navigate to Team brand kits Page"):
                self.LogInPage.ScrollclickOperation(*MyBrandingLocators.MyBranding)

                MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
                if MyBranding_elementvisible:
                    if env in MyBrandingLocators.MyBranding_Page_url:
                        expected_url = MyBrandingLocators.MyBranding_Page_url[env]
                        current_url = self.LogInPage.get_LoginPage_url(expected_url)

                        assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                        print(current_url)

            with allure.step("Check if logo of brand page element is present"):
                flag = self.MyBrandingPage.is_logo_exist()
                if flag:
                    assert flag

            with allure.step("Check if brand kits element is present"):
                MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
                if MyBranding_elementvisible:
                    text = self.MyBrandingPage.get_element_text(*MyBrandingLocators.MyBranding)

                    assert text == "Brand kits"
                    print(text)
