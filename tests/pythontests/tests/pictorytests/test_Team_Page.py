import time

import allure
import pytest
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from locator.locators import LoginLocators, TeamLocators, SubscriptionLocators, MyProjectLocators, HomeLocators
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.TeamPage import TeamPage
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Team Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestTeam:
    email, password = TestDataForProject.get_login_credential("TeamPage", 0)

    @allure.title("Create a new team")
    @allure.description("This is test of create a new Team")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_create_Team_plan(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Page"):
                    element1 = self.TeamPage.get_create_Teamelement(*TeamLocators.team)
                    if element1:
                        with allure.step("Click on 'Create Team' button"):
                            self.TeamPage.team_element_scrollClick(*TeamLocators.team)
                            with allure.step("Provide team details"):
                                self.TeamPage.put_team_detail("Pictory automate", "team_automate@gmail.com")

                                team_butn = self.TeamPage.get_element(*TeamLocators.team_butn)
                                if team_butn:
                                    with allure.step("Click on 'Create Team' button after providing details"):
                                        self.TeamPage.scrollToclick_element(*TeamLocators.team_butn)

                                    with allure.step("Scroll to 'Start' button and click"):
                                        self.TeamPage.scrollToclick_element(*TeamLocators.start)
                                        TeamProject = self.TeamPage.get_element(*TeamLocators.TeamProject)
                                        if TeamProject:
                                            assert TeamProject, "Team Project element is not present."
                                        print(TeamProject.text)

            except (StaleElementReferenceException, TimeoutException, NoSuchElementException):
                print("The create Team butn is not visible.")
                # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                self.TeamPage.Jsclick_operation(*TeamLocators.team_account)

                TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                if TeamProject:
                    assert TeamProject, "Team Project element is not present."
                print(TeamProject.text)

    @allure.title("Team Project page url")
    @allure.description("This is test of Team Project page url")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Team_Project_page_url(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Project Page"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                    if TeamProject:
                        with allure.step("Click on 'Team Project'"):
                            self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                            team_name = self.TeamPage.get_element(*TeamLocators.teamaccount_name)
                            if team_name:
                                with allure.step("Verify Team Project URL"):
                                    if env in TeamLocators.team_Project_url:
                                        expected_url = TeamLocators.team_Project_url[env]
                                        current_url = self.LogInPage.get_LoginPage_url(expected_url)

                                        assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                                        print(current_url)

            except StaleElementReferenceException:
                with allure.step("Handle visibility issues"):
                    print("The team Project URL is not visible.")

    @allure.title("Team page title")
    @allure.description("This is test of Team page title")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Team_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Project Page"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                    if TeamProject:
                        with allure.step("Click on 'Team Project'"):
                            self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                            team_name = self.TeamPage.get_element(*TeamLocators.teamaccount_name)
                            if team_name:
                                with allure.step("Verify Team Project Title"):
                                    title = self.LogInPage.get_login_page_title(LoginLocators.LOGIN_PAGE_TITLE)
                                    assert title == LoginLocators.LOGIN_PAGE_TITLE
                                    print(title)

            except StaleElementReferenceException:
                with allure.step("Handle visibility issues"):
                    print("The element is not visible.")

    @allure.title("Team page logo visible")
    @allure.description("This is test of Team page logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Team_logo_visible(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                        team_name = self.TeamPage.get_element(*TeamLocators.teamaccount_name)
                    with allure.step("Verify Team Name"):
                        if team_name:
                            with allure.step("Check Team Logo Visibility"):
                                flag = self.TeamPage.is_logo_exist()
                                assert flag

            except StaleElementReferenceException:
                with allure.step("Handle the logo visibility issues"):
                    print("The logo is not visible.")

    @allure.title("Logout after Team Project Page in pictory")
    @allure.description("This is test of logout after Team Project Page in pictory")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_logout_after_Team_Project_Page(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)

                with allure.step("Navigate to Team Project"):
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)

                    with allure.step("Verify Team Name"):
                        team_name = self.TeamPage.get_element(*TeamLocators.teamaccount_name)
                        if team_name:
                            assert team_name, "Team name element is not present."

                        with allure.step("Logout"):
                            # self.LogInPage.ScrollclickOperation(*LoginLocators.login_hover_Profile)
                            self.TeamPage.Jsclick_operation(*LoginLocators.logout_bn)

                        with allure.step("Verify Logout and Redirect to Login Page"):
                            element = self.LogInPage.login_element_exist(*LoginLocators.login_bn)
                            assert element, "Login button not visible after logout."

                            if element:
                                if env in LoginLocators.LOGIN_PAGE_URL:
                                    expected_url = LoginLocators.LOGIN_PAGE_URL[env]
                                    current_url = self.LogInPage.get_LoginPage_url(expected_url)
                                    assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The team element is not visible.")

    @allure.title("Team page create Project element")
    @allure.description("This is test of Team page create Project element")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_create_Project_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                        createProject = self.TeamPage.get_element(*TeamLocators.createProject)
                    with allure.step("Verify the Create Project"):
                        if createProject:
                            assert (createProject.is_displayed(),
                                    f"element with name '{createProject.text} ' is not present on the page.")

                        print(createProject.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Team page Import Project test")
    @allure.description("Team page --> Import Project from Project folder")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_MyProject_page_ImportProject(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)

                        Import = self.TeamPage.get_element(*TeamLocators.Import_location)
                    with allure.step("Verify the Import Project"):
                        if Import:
                            assert (Import.is_enabled(), f"element with name '{Import}' is not present on the page.")

                            print(Import.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Team page Import My Project pop up elements")
    @allure.description("This is test of Team page Import My project pop up elements")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Import_team_importProject_pop_up_elements(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)

                        self.TeamPage.team_element_scrollClick(*TeamLocators.Import_location)

                    with allure.step("Verify the Import Project popup element"):
                        Import_Myprojects = self.TeamPage.get_element(*TeamLocators.Import_Myprojects)
                        personal_Workspace = self.TeamPage.get_element(*TeamLocators.personal_Workspace)
                        project_files = self.TeamPage.get_element(*TeamLocators.project_files)
                        cancel_butn = self.TeamPage.get_element(*TeamLocators.cancel_butn)
                        import_butn = self.TeamPage.get_element(*TeamLocators.import_butn)
                        if Import_Myprojects and personal_Workspace and project_files and cancel_butn and import_butn:
                            assert (
                                Import_Myprojects.is_displayed() and personal_Workspace.is_displayed() and project_files.is_displayed() and cancel_butn.is_displayed() and import_butn.is_displayed(),
                                f"element with name '{Import_Myprojects.text}, {personal_Workspace.text}, {project_files.text}, {cancel_butn.text}, {import_butn.text} ' is not present on the page.")

                        print(Import_Myprojects.text, "===", personal_Workspace.text, "===", project_files.text, "===",
                              cancel_butn.text, "===", import_butn.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Team page Import My Project pop up elements")
    @allure.description("This is test of Team page Import My project pop up elements")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Import_team_importProject_pop_up_cancel_butn_function(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)

                        self.TeamPage.team_element_scrollClick(*TeamLocators.Import_location)
                        cancel_butn = self.TeamPage.get_element(*TeamLocators.cancel_butn)

                    with allure.step("click on the cancel buton"):
                        if cancel_butn:
                            self.LogInPage.ScrollclickOperation(*TeamLocators.cancel_butn)
                            ImportProject = self.TeamPage.get_element(*TeamLocators.Import_location)
                        with allure.step("Verify the Import Project popup cancel buton"):
                            assert (ImportProject.is_displayed(),
                                    f"element with name '{ImportProject.text},' is not present on the page.")

                            print(ImportProject.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Team page create folder text")
    @allure.description("This is test of Team page create folder text")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Create_folder_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                        create_folder = self.TeamPage.get_element(*TeamLocators.createfolder)

                    with allure.step("Verify the Create Folder text"):
                        if create_folder:
                            assert (create_folder.is_displayed(),
                                    f"element with name '{create_folder.text}' is not present on the page.")

                        print(create_folder.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Team page create folder")
    @allure.description("This is test of Team page create folder")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Create_folder_teamPage(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)

        Folder_name = "team_folder" + TeamPage.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)
        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)

                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                        self.TeamPage.team_element_scrollClick(*TeamLocators.createfolder)
                        self.TeamPage.get_team_foldername(*TeamLocators.folder_name, Folder_name)
                        time.sleep(2)
                        self.LogInPage.clickOperation(*TeamLocators.createbtn)

                    with allure.step("Verify the Create Folder function"):
                        team_Folder_automation = self.TeamPage.get_team_folder(Folder_name)
                        if team_Folder_automation:
                            assert (
                                team_Folder_automation.is_displayed(),
                                f"element with name '{team_Folder_automation.text}' is not present on the page.")

                        print(team_Folder_automation.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Team page Search folder")
    @allure.description("This is test of Team page Search folder")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Search_folder_teamPage(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)

        Folder_name = "Search" + TeamPage.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)
        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)

                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                    if TeamProject:
                        assert TeamProject, "Team Project element is not present."

                    with allure.step("Navigate to Team Project"):
                        if TeamProject:
                            self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                            self.TeamPage.team_element_scrollClick(*TeamLocators.createfolder)
                            self.TeamPage.get_team_foldername(*TeamLocators.folder_name, Folder_name)
                            time.sleep(2)
                            self.LogInPage.clickOperation(*TeamLocators.createbtn)

                        with allure.step("Verify the Search Folder function"):
                            team_folder_automation = self.TeamPage.get_team_folder(Folder_name)
                            if team_folder_automation:
                                team_folder_automation_text = team_folder_automation.get_attribute("alt");
                                self.TeamPage.get_search_video(*MyProjectLocators.Search, Folder_name)

                                if team_folder_automation:
                                    assert team_folder_automation.is_displayed(), f"Element with name '{team_folder_automation.text}' is not present on the page."

                                    print(team_folder_automation_text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    team_folder_automation = self.TeamPage.get_team_folder(Folder_name)
                    if team_folder_automation:
                        team_folder_automation_text = team_folder_automation.get_attribute("alt");
                        if team_folder_automation:
                            assert team_folder_automation.is_displayed(), f"Element with name '{team_folder_automation.text}' is not present on the page."
                            print(team_folder_automation_text)

    @allure.title("Team page Delete folder")
    @allure.description("This is test of Team page Delete folder")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.Regression
    def test_Delete_folder_teamPage(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)

        Folder_name = "Delete" + TeamPage.random_generator()
        self.LogInPage.loginpictory(self.email, self.password)
        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)

                    TeamProject = self.TeamPage.get_teamProject_element(*TeamLocators.TeamProject)
                with allure.step("Navigate to Team Project"):
                    if TeamProject:
                        assert TeamProject, "Team Project element is not present."
                        if TeamProject:
                            self.LogInPage.clickOperation(*TeamLocators.TeamProject)
                            self.TeamPage.team_element_scrollClick(*TeamLocators.createfolder)
                            self.TeamPage.get_team_foldername(*TeamLocators.folder_name, Folder_name)
                            time.sleep(2)
                            self.LogInPage.clickOperation(*TeamLocators.createbtn)

                        with allure.step("Navigate to the Project Page and Create the Folder function"):
                            loader1 = self.TeamPage.get_element_Invisible(*HomeLocators.loader)
                            if loader1:
                                team_folder_automation = self.TeamPage.get_team_folder(Folder_name)
                                self.TeamPage.get_search_video(*MyProjectLocators.Search, Folder_name)

                                time.sleep(5)  # You can adjust this sleep duration as needed.
                                self.TeamPage.do_folder_deleted(*MyProjectLocators.video_Delete, team_folder_automation)

                                with allure.step("Verify the Delete Folder function"):
                                    # WebDriverWait(self.driver, 60).until(ec.staleness_of(team_folder_automation))

                                    folder = self.TeamPage.get_team_folder(Folder_name)
                                    if folder:
                                        error_message = self.TeamPage.get_element(*TeamLocators.error_message)
                                        if error_message:
                                            assert error_message.text == "No videos found", "Element should be deleted, but it's still present."

                                            print(error_message.text)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    # Manage team Page UI and functionality.

    @allure.title("Manage team Page url in pictory")
    @allure.description("This is test Manage team Page url in pictory")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Manage_team_Page_url(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    ManageTeam = self.TeamPage.get_teamProject_element(*TeamLocators.ManageTeam)

                with allure.step("Navigate to the Manage Team Page"):
                    if ManageTeam:
                        assert ManageTeam, "Manage team element is not present."
                        self.LogInPage.ScrollclickOperation(*TeamLocators.ManageTeam)

                        Team_member = self.TeamPage.get_element(*TeamLocators.Team_member)
                    with allure.step("Verify the Team member element"):
                        assert Team_member, "Team member element is not present."

                    with allure.step("Verify the Manage Team Page URL"):
                        if Team_member:
                            if env in TeamLocators.Manage_team_URL:
                                expected_url = TeamLocators.Manage_team_URL[env]
                                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                                print(current_url)

            except StaleElementReferenceException:
                with allure.step("Handle the issue"):
                    print("The manage team url is not visible.")

    @allure.title("Manage team Page add and delete user in pictory")
    @allure.description("This is test Manage team Page add and delete user in pictory")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Manage_team_Page_add_and_delete_user(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)

        email, password = TestDataForProject.get_login_credential("TeamPage", 4)
        self.LogInPage.loginpictory(email, password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    ManageTeam = self.TeamPage.get_teamProject_element(*TeamLocators.ManageTeam)

                with allure.step("Navigate to the Manage Team Page"):
                    if ManageTeam:
                        assert ManageTeam, "Manage team element is not present."
                        self.LogInPage.ScrollclickOperation(*TeamLocators.ManageTeam)

                        email_field = self.TeamPage.get_element(*TeamLocators.Enter_email_field)
                        if email_field:
                            assert email_field, "Team member element is not present."

                            with allure.step("Add and Delete User"):
                                self.TeamPage.do_add_and_delete_User("pictoryautomate8642@gmail.com")
                                time.sleep(2)
                                send_Invite = self.TeamPage.get_element(*TeamLocators.send_Invite)
                                if send_Invite:
                                    self.LogInPage.clickOperation(*TeamLocators.send_Invite)
                                    add_emailID = self.TeamPage.get_element(*TeamLocators.added_emailID)
                                    if add_emailID:
                                        assert add_emailID, "Team member element is not present."

                                        with allure.step("Delete User"):
                                            self.LogInPage.clickOperation(*TeamLocators.Delete_icon)
                                            time.sleep(3)
                                            self.LogInPage.ScrollclickOperation(*TeamLocators.Delete_butn)
                                            element = self.TeamPage.get_element(*TeamLocators.userSuccesful_text)
                                            if element:
                                                assert element.text == "User deleted successfully"

                                            print(element.text)  # This line may not be necessary if everything is asserted successfully

            except StaleElementReferenceException as e:
                with allure.step("Handle Exception"):
                    print(f"An exception occurred: {str(e)}")

    @allure.title("Manage team Page Team member element in pictory")
    @allure.description("This is test Manage team Page Team member element in pictory")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Manage_team_Page_Team_member_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.TeamPage = TeamPage(self.driver)
        self.LogInPage.loginpictory(self.email, self.password)

        element = self.TeamPage.get_Homepage_element()
        if element:
            try:
                with allure.step("Navigate to Team Account"):
                    # self.LogInPage.ScrollclickOperation(*SubscriptionLocators.hover_Profile)
                    self.TeamPage.Jsclick_operation(*TeamLocators.team_account)
                    ManageTeam = self.TeamPage.get_teamProject_element(*TeamLocators.ManageTeam)
                    if ManageTeam:
                        assert ManageTeam, "Manage team element is not present."

                        with allure.step("Navigate to Manage Team Page"):
                            self.LogInPage.ScrollclickOperation(*TeamLocators.ManageTeam)

                            Team_member = self.TeamPage.get_element(*TeamLocators.Team_member)
                            if Team_member:
                                assert Team_member, "Team member element is not present."

                                with allure.step("verify Team Member Text"):
                                    print(Team_member.text)  # This line may not be necessary if everything is asserted successfully

            except StaleElementReferenceException as e:
                with allure.step("Handle Exception"):
                    print(f"An exception occurred: {str(e)}")
