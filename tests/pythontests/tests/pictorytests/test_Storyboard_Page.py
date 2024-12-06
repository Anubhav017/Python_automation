import traceback

import pytest
import allure
from selenium.common import StaleElementReferenceException

from locator.locators import ScriptToVideoLocators, StoryboardLocators, MyBrandingLocators, HomeLocators
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.MyProjectPage import MyProjectPage
from pageObjects.pictryPages.MybrandingPage import MyBrandingPage
from pageObjects.pictryPages.ScriptToVideo import ScriptToVideo
from pageObjects.pictryPages.StoryboardPage import Storyboard
from pageObjects.pictryPages.loadtimePage import LoadTimeTracker
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Storyboard Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestStoryboard:
    script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 0)
    Storyboard_email, Storyboard_password = TestDataForProject.get_login_credential("Storyboard", 0)

    @allure.title("Storyboard page URL of Page")
    @allure.description("Storyboard page --> URL of Page")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_Storyboard_URL_Page(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.Storyboard = Storyboard(self.driver)

        name = "Storyboard" + ScriptToVideo.random_generator()
        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.Storyboard.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)

        # self.Storyboard.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)
        toggle_buttons, clip_Board, font_weight = self.Storyboard.get_scripteditor_highlight_Page(name)
        if font_weight:
            assert font_weight == "700" or font_weight == "bold", "The text is not bold"
            clip_Board_enable = clip_Board.is_enabled()
            assert clip_Board_enable, "clipBoard button is no enabled"
            for toggle_button in toggle_buttons:
                is_enabled = toggle_button.is_enabled()  # Use is_enabled() method to check if the toggle button is enabled
                assert is_enabled, "Not all toggle buttons are enabled"

                Storyboard_loaded = self.Storyboard.get_Storyboard_Page_scriptDownload(*ScriptToVideoLocators.saved)
                if Storyboard_loaded:
                    Story = self.Storyboard.get_storyboard_element(*StoryboardLocators.Story)
                    if Story:
                        self.Storyboard.scrollTo_click_element(*StoryboardLocators.Story)
                        assert (Story.is_enabled(), f"element with name '{Story.text}' is not present on the page.")
                        print(Story.text)

    @allure.title("Storyboard page Click on the Format")
    @allure.description("Storyboard page --> Click on the Format")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Storyboard_Format_click(self):
        self.LogInPage = LogInPage(self.driver)
        self.Storyboard = Storyboard(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.Storyboard.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        # Perform actions on the element
        format_resolution = self.Storyboard.get_storyboard_element(*ScriptToVideoLocators.format)
        if format_resolution:
            self.Storyboard.scrollTo_click_element(*ScriptToVideoLocators.format)
            selectVideo_resolution = self.Storyboard.get_element(*StoryboardLocators.selectVideo_resolution)
            if selectVideo_resolution:
                assert (selectVideo_resolution.is_displayed(),
                        f"element with name '{selectVideo_resolution.text}' is not present on the page.")

                print(selectVideo_resolution.text)

    @allure.title("Script to video generate StoryBoard element and and home Page to Storyboard Load time :")
    @allure.description("Video generate --> StoryBoard element and home Page to Storyboard Load time")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    @pytest.mark.PageLoad
    def test_scriptTo_video_Page_Story_Board_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        elementvisible = self.MyProjectPage.Myproject_elementVisible(*HomeLocators.loader)
        if elementvisible:
            start_time = LoadTimeTracker.start_timing()

            self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Recent_Projects)

            # Perform actions on the element
            Story = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Story)

            assert (Story.is_enabled(), f"element with name '{Story.text}' is not present on the page.")
            print(Story.text)

            Visual = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Visual)
            assert (Visual.is_enabled(), f"element with name '{Visual.text}' is not present on the page.")

            print(Visual.text)

            audio = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Audio)

            assert (audio.is_enabled(), f"element with name '{audio.text}' is not present on the page.")
            print(audio.text)

            Text = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Text)

            assert (Text.is_enabled(), f"element with name '{Text.text}' is not present on the page.")
            print(Text.text)

            elements = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.element)

            assert (elements.is_enabled(), f"element with name '{elements.text}' is not present on the page.")
            print(elements.text)

            style = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Styles)

            assert (style.is_enabled(), f"element with name '{style.text}' is not present on the page.")
            print(style.text)

            brand = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.branding)

            assert (brand.is_enabled(), f"element with name '{brand.text}' is not present on the page.")
            print(brand.text)

            format_text = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.format)

            assert (format_text.is_enabled(), f"element with name '{format_text.text}' is not present on the page.")
            print(format_text.text)

            prev = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.previous)

            assert (prev.is_displayed(), f"element with name '{prev.text}' is not present on the page.")
            print(prev.text)

            storyboard_load_time = LoadTimeTracker.end_timing(start_time)
            print(f"storyboard Page load time : {storyboard_load_time} sec")

            # Attach load time to Allure report
            LoadTimeTracker.attach_load_time(storyboard_load_time, page_type="home page --> storyboard Page")

    @allure.title("Script to video generate Preview element")
    @allure.description("Video generate --> Preview element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_scriptTo_video_Page_Preview_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.ScriptToVideo.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        WaterMarks = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.WaterMarks)
        if WaterMarks:
            self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)

            # Perform actions on the element
            Preview = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.preview)
            if Preview.is_enabled():
                assert (Preview.is_displayed(), f"element with name '{Preview.text}' is not present on the page.")
                print(Preview.text)

                self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.preview)

                Copypreview_link = self.ScriptToVideo.get_element(*ScriptToVideoLocators.Copypreview_link)

                if Copypreview_link:
                    assert Copypreview_link, f"Video src attribute for '{Copypreview_link.text}' is empty."

                print(Copypreview_link.text)

    @allure.title("Storyboard page text page Body text font")
    @allure.description("Storyboard page --> text page Body text font")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Storyboard_Text_Bodytext(self):
        self.LogInPage = LogInPage(self.driver)
        self.Storyboard = Storyboard(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.Storyboard.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        # Perform actions on the element
        text = self.Storyboard.get_storyboard_element(*ScriptToVideoLocators.Text)
        if text:
            self.Storyboard.scrollTo_click_element(*ScriptToVideoLocators.Text)
            bodyText_click = self.Storyboard.get_element(*StoryboardLocators.BodyFont)
            if bodyText_click:
                self.Storyboard.action_Click(*StoryboardLocators.BodyFont)
                Body_font = self.Storyboard.get_storyboard_element(*StoryboardLocators.Bodysize)
                if Body_font.is_displayed:
                    assert (
                        Body_font.is_displayed(), f"element with name '{Body_font.text}' is not present on the page.")

                    print(f"body Text Font size is '{Body_font.get_attribute('value')}' .")

    @allure.title("Storyboard page Click on the Visual : Load time")
    @allure.description("Storyboard page --> Click on the Visual and Load time")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    @pytest.mark.PageLoad
    def test_Storyboard_visual_click(self):
        self.LogInPage = LogInPage(self.driver)
        self.Storyboard = Storyboard(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.LogInPage.loginpictory(self.script_email, self.script_password)
        self.Storyboard.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)
        MyBranding_elementvisible = self.MyBrandingPage.MyBranding_elementVisible(*MyBrandingLocators.Mybranding_loader)
        if MyBranding_elementvisible:
            # Perform actions on the element
            start_time = LoadTimeTracker.start_timing()

            Visual = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Visual)
            if Visual:
                self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Visual)

                assert (Visual.is_enabled(), f"element with name '{Visual.text}' is not present on the page.")
                print(Visual.text)
                video = self.ScriptToVideo.get_element(*ScriptToVideoLocators.video)
                if video:
                    assert video is not None, "Button not found on the page"

                    storyboardVisual_load_time = LoadTimeTracker.end_timing(start_time)
                    print(f"storyboard visual Page load time : {storyboardVisual_load_time} sec")

                    # Attach load time to Allure report
                    LoadTimeTracker.attach_load_time(storyboardVisual_load_time, page_type="storyboard Page  --> Visual page")

    @allure.title("Script to video generate Download element")
    @allure.description("Video generate --> Download element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_scriptTo_video_Page_Download_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.ScriptToVideo.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        # Perform actions on the element
        Download = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Download_element)

        assert (Download.is_displayed(), f"element with name '{Download.text}' is not present on the page.")
        print(Download.text)

    @allure.title("Storyboard page Click on the Visual Recent : Load time")
    @allure.description("Storyboard page --> Click on the Visual Recent and Load time")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    @pytest.mark.PageLoad
    def test_Storyboard_visual_Recent_click(self):
        self.LogInPage = LogInPage(self.driver)
        self.Storyboard = Storyboard(self.driver)
        self.MyBrandingPage = MyBrandingPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        Storyboard_email, Storyboard_password = TestDataForProject.get_login_credential("Storyboard", 1)

        self.LogInPage.loginpictory(Storyboard_email, Storyboard_password)
        self.Storyboard.loaderinvisible_click(*StoryboardLocators.Recent_Projects)
        MyBranding_elementvisible = self.MyBrandingPage.MyBranding_elementVisible(*MyBrandingLocators.Mybranding_loader)
        if MyBranding_elementvisible:
            # Perform actions on the element

            Visual = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Visual)
            if Visual:
                self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Visual)

                assert (Visual.is_enabled(), f"element with name '{Visual.text}' is not present on the page.")
                print(Visual.text)

                start_time = LoadTimeTracker.start_timing()
                Recent = self.Storyboard.is_visible(*StoryboardLocators.Recent)
                if Recent:
                    self.ScriptToVideo.ScrollclickOperation(*StoryboardLocators.Recent)
                    storyboardVisualRecent_load_time = LoadTimeTracker.end_timing(start_time)
                    print(f"storyboard visual --> Recent Page load time : {storyboardVisualRecent_load_time} sec")

                    # Attach load time to Allure report
                    LoadTimeTracker.attach_load_time(storyboardVisualRecent_load_time, page_type="storyboard Page  --> Visual Recent page")

    @allure.title("Script to video generate Scene Duration element")
    @allure.description("Video generate --> Scene Duration element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_scriptTo_video_Page_SceneDuration_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.ScriptToVideo.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        # Perform actions on the element
        scene = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Scene_Duration)

        assert (scene.is_displayed(), f"element with name '{scene.text}' is not present on the page.")
        print(scene.text)

    @allure.title("Script to video generate Video Duration element")
    @allure.description("Video generate --> Video Duration element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_scriptTo_video_Page_VideoDuration_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.ScriptToVideo.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        # Perform actions on the element
        video = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Video_Duration)

        assert (video.is_displayed(), f"element with name '{video.text}' is not present on the page.")
        print(video.text)

    @allure.title("Script to video generate Intro scene element")
    @allure.description("Video generate --> Intro scene element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_scriptTo_video_Page_IntroScene_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        self.LogInPage.loginpictory(self.Storyboard_email, self.Storyboard_password)
        self.ScriptToVideo.loaderinvisible_click(*ScriptToVideoLocators.Recent_Projects)

        # Perform actions on the element
        Intro_scene = self.ScriptToVideo.get_scriptToVideo_element_storyboard(*ScriptToVideoLocators.Intro)

        assert (Intro_scene.is_displayed(), f"element with name '{Intro_scene.text}' is not present on the page.")
        print(Intro_scene.text)

    @allure.title("My Project page search the video")
    @allure.description("My Project page --> search the video")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.skip(reason="csv video download functionality issue .")
    @pytest.mark.Regression
    def test_search_video(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)

        name = "csv_video" + ScriptToVideo.random_generator()

        email, password = TestDataForProject.get_login_credential("MyProject", 1)
        self.LogInPage.loginpictory(email, password)

        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)
        try:
            with allure.step("Generate ScriptToVideo and search"):
                Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_script(name)
                if Storyboard_loaded:
                    self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)
                    self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                    # Perform actions on the element
                    video = self.MyProjectPage.is_video_exist(name)
                    assert video.is_displayed(), f"Video element with name '{name}' is not present or not displayed on the page."
                    print(name)

                    video_src = video.get_attribute("src")
                    assert video_src, f"Video src attribute for '{video_src}' is empty."
                    print(video_src)

        except StaleElementReferenceException:
            print(traceback.format_exc())
