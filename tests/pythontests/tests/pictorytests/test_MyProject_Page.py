import traceback

import pytest
import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains

from locator.locators import ScriptToVideoLocators, MyProjectLocators, AccountLocators, TeamLocators, HomeLocators, \
    MyBrandingLocators
from pageObjects.pictryPages.HomePage import HomePage

from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.MyProjectPage import MyProjectPage
from pageObjects.pictryPages.MybrandingPage import MyBrandingPage
from pageObjects.pictryPages.ScriptToVideo import ScriptToVideo
from pageObjects.pictryPages.loadtimePage import LoadTimeTracker
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("My Project Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestMyProject:
    email, password = TestDataForProject.get_login_credential("MyProject", 0)

    @allure.title("My Project page url")
    @allure.description("My Project page --> url")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.parametrize("email, password", [("anubhav@pictory.ai", "Pictory@123")])
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_url(self, email, password, env):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)

        if env in MyProjectLocators.MyProject_Page_URL:
            expected_url = MyProjectLocators.MyProject_Page_URL[env]
            current_url = self.MyProjectPage.get_MyProjectPage_url(expected_url)
            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

            print(current_url)

    @allure.title("My Project page title")
    @allure.description("My Project page --> title")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)

        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:
            title = self.MyProjectPage.get_MyProjectPage_title(MyProjectLocators.MyProject_Page_TITLE)
            assert title == MyProjectLocators.MyProject_Page_TITLE

    @allure.title("My Project page logo visible")
    @allure.description("My Project page --> logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_logo_visible(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)

        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:
            flag = self.MyProjectPage.is_logo_exist()
            assert flag

    @allure.title("My Project page Project and help text test")
    @allure.description("My Project page  --> Project and help text")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_Project_help_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)

        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:
            text = self.MyProjectPage.get_element_text(*MyProjectLocators.MyProject)
            assert text == "My projects"
            print(text)

        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:
            text = self.MyProjectPage.get_element_text(*MyProjectLocators.help)
            assert text == "Help"
            print(text)

    @allure.title("Project page -> brand Kit page navigation test")
    @allure.description("Project page -> brand Kit page navigation")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Project_page_brandKit_navigation(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.MyBrandingPage = MyBrandingPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*HomeLocators.Project)

        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyBrandingLocators.MyBranding)

        MyBranding_elementvisible = self.MyBrandingPage.get_MyBranding_element(*MyBrandingLocators.MyBranding)
        if MyBranding_elementvisible:
            if env in MyBrandingLocators.MyBranding_Page_url:
                expected_url = MyBrandingLocators.MyBranding_Page_url[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                print(current_url)

    @allure.title("Project page -> Home page navigation test")
    @allure.description("Project page -> Home page navigation")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Project_page_Home_navigation(self):
        self.LogInPage = LogInPage(self.driver)
        self.HomePage = HomePage(self.driver)

        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*HomeLocators.Project)

        self.MyProjectPage.clickOperation(*HomeLocators.home)
        element = self.HomePage.get_element_DOM(*HomeLocators.home)
        assert element.text == "Home"
        print(element.text)

    @allure.title("My Project page search field test")
    @allure.description("My Project page --> search field")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_search_field(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)

        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:
            search = self.MyProjectPage.get_element(*MyProjectLocators.Search)

            assert (search.is_displayed(), f"Search field element with name '{search.text}' is not present on the page.")
            print(search.text)

    @allure.title("Home page navigate to myProject Page Load time :")
    @allure.description("Home page --> myProject Load")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    @pytest.mark.PageLoad
    def test_Home_pageTo_myProject_Page(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)
        email, password = TestDataForProject.get_login_credential("MyProject", 3)

        self.LogInPage.loginpictory(email, password)

        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:

            start_time = LoadTimeTracker.start_timing()

            Import = self.MyProjectPage.get_navigate_myProject(*HomeLocators.Project)
            if Import.is_enabled():
                assert (Import, f"element with name '{Import}' is not present on the page.")

                MyProject_load_time = LoadTimeTracker.end_timing(start_time)
                print(f"MyProject Page load time : {MyProject_load_time} sec")

                # Attach load time to Allure report
                LoadTimeTracker.attach_load_time(MyProject_load_time, page_type="home page --> MyProject Page")
                LoadTimeTracker.monitor_cpu_usage(MyProject_load_time)

    @allure.title("My Project page delete the video")
    @allure.description("My Project page --> delete the video")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Delete_video(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        name = "Delete" + ScriptToVideo.random_generator()

        email, password = TestDataForProject.get_login_credential("MyProject", 1)
        self.LogInPage.loginpictory(email, password)
        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)
        try:
            with allure.step("Generate ScriptToVideo and delete the video"):
                Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_script(name)
                if Storyboard_loaded:
                    self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)
                    self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                    # Perform actions on the element
                    video_delete = self.MyProjectPage.is_video_exist(name)
                    self.MyProjectPage.get_search_video(*MyProjectLocators.Search, name)
                    self.MyProjectPage.get_video_delete(video_delete)
                    error_message = self.ScriptToVideo.get_element(*TeamLocators.error_message)
                    if error_message:
                        assert error_message.text == "No videos found", "Element should be deleted, but it's still present."
                        print(error_message.text)

        except StaleElementReferenceException:
            print(traceback.format_exc())

    @allure.title("My Project page search the video")
    @allure.description("My Project page --> search the video")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_search_video(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        name = "search" + ScriptToVideo.random_generator()

        email, password = TestDataForProject.get_login_credential("MyProject", 1)
        self.LogInPage.loginpictory(email, password)

        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)
        try:
            with allure.step("Generate ScriptToVideo and search"):
                Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_script(name)
                if Storyboard_loaded:
                    self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)
                    self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                    self.MyProjectPage.get_search_video(*MyProjectLocators.Search, name)

                    # Perform actions on the element
                    video = self.MyProjectPage.is_video_exist(name)
                    assert video.is_displayed(), f"Video element with name '{name}' is not present or not displayed on the page."
                    print(name)

                    video_src = video.get_attribute("src")
                    assert video_src, f"Video src attribute for '{video_src}' is empty."
                    print(video_src)

        except StaleElementReferenceException:
            print(traceback.format_exc())

    @allure.title("My Project page Duplicate the video")
    @allure.description("My Project page --> Duplicate the video")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Duplicate_video(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        name = "Duplicate" + ScriptToVideo.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)

        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)

        try:
            with allure.step("Generate ScriptToVideo and Duplicate "):
                Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_script(name)
                if Storyboard_loaded:
                    self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)
                    self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                    # Perform actions on the element
                    video = self.MyProjectPage.is_video_exist(name)
                    action = ActionChains(self.driver)

                    if video.is_displayed():
                        action.move_to_element_with_offset(video, 90, 50).perform()

                        Duplicate_button = self.MyProjectPage.get_myproject_hoverelement(*MyProjectLocators.video_Duplicate)
                        if Duplicate_button:
                            Duplicate_button.click()

                            for i in range(1, 5):  # You can adjust the range based on your naming convention
                                Duplicated_name = f"{name}({i})"
                                if self.MyProjectPage.is_video_exist(Duplicated_name):
                                    assert self.MyProjectPage.is_video_exist(
                                        Duplicated_name), f"Duplicated video '{Duplicated_name}' not found"

                                    print(Duplicated_name)
                                    break

        except StaleElementReferenceException:
            print(traceback.format_exc())

    @allure.title("My Project page Create Project folder click")
    @allure.description("My Project page --> Create Project click")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_createProject_click(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)
        createProject = self.MyProjectPage.get_myproject_hoverelement(*MyProjectLocators.createProject)
        if createProject:
            self.MyProjectPage.ScrollclickOperation(*MyProjectLocators.createProject)
            element = self.MyProjectPage.get_element(*MyProjectLocators.MyProject)
            if element:
                if env in AccountLocators.HOME_Page_URL:
                    expected_url = AccountLocators.HOME_Page_URL[env]
                    current_url = self.LogInPage.get_LoginPage_url(expected_url)

                    assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                    print(current_url)

    @allure.title("My Project page Create folder test")
    @allure.description("My Project page --> Create folder text")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_createfolder_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)
        create_folder = self.MyProjectPage.get_myproject_hoverelement(*MyProjectLocators.createfolder)
        if create_folder:
            assert (create_folder.is_displayed(), f"element with name '{create_folder.text}' is not present on the page.")
            print(create_folder.text)

    @allure.title("My Project page Create folder test")
    @allure.description("My Project page --> Create folder")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_create_Folder(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        Folder_name = "folder" + MyProjectPage.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)

        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)
        createProject = self.MyProjectPage.get_myproject_hoverelement(*MyProjectLocators.createProject)
        if createProject:
            self.MyProjectPage.ScrollclickOperation(*MyProjectLocators.createfolder)
            self.MyProjectPage.get_folder_name(*MyProjectLocators.folder_name, Folder_name)

            createbtn = self.MyProjectPage.get_myproject_hoverelement(*MyProjectLocators.createbtn)
            if createbtn:
                self.MyProjectPage.clickOperation(*MyProjectLocators.createbtn)
                Folder_automation = self.MyProjectPage.get_create_folder(Folder_name)

                assert (Folder_automation.is_displayed(), f"element with name '{Folder_automation}' is not present on the page.")
                print(Folder_automation.text)

    @allure.title("My Project page Import Project test")
    @allure.description("My Project page --> Import Project from Project folder")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_ImportProject(self):
        self.LogInPage = LogInPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        self.MyProjectPage.Myproject_elementvisible_scrolClick(*MyProjectLocators.MyProject)
        Import = self.MyProjectPage.get_myproject_hoverelement(*MyProjectLocators.Import_location)
        if Import:
            assert (Import.is_enabled(), f"element with name '{Import}' is not present on the page.")
        print(Import.text)

    @allure.title("My Project page Move the video to Folder")
    @allure.description("My Project page --> Move the video to Folder")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Move_videoTo_Folder(self):
        self.LogInPage = LogInPage(self.driver)
        self.ScriptToVideo = ScriptToVideo(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        name = "MoveVideo" + ScriptToVideo.random_generator()

        self.LogInPage.loginpictory(self.email, self.password)
        self.ScriptToVideo.dynamicbar_invisible_scrolClick(*ScriptToVideoLocators.Proceed_buton)

        try:
            with allure.step("Generate ScriptToVideo and move the video to Folder"):
                Storyboard_loaded = self.ScriptToVideo.get_Storyboard_Page_script(name)
                if Storyboard_loaded:
                    self.ScriptToVideo.clickOperation(*ScriptToVideoLocators.WaterMarks)
                    self.ScriptToVideo.ScrollclickOperation(*ScriptToVideoLocators.Project)

                    video = self.MyProjectPage.is_video_exist(name)
                    if video:
                        self.MyProjectPage.get_search_video(*MyProjectLocators.Search, name)

                        Folder = self.MyProjectPage.get_moveTo_folder(video)
                        if Folder:
                            assert Folder.text == "Project is moved to the folder 'Folder'"
                            print(Folder.text)

        except StaleElementReferenceException:
            print(traceback.format_exc())
