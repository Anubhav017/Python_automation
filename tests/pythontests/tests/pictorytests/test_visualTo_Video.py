import pytest
import allure

from locator.locators import VisualVideoLocators
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.VisualToVideoPage import VisualVideo
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Visual Video  Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestVisualVideo:
    email, password = TestDataForProject.get_login_credential("VisualToVideo", 0)

    @allure.title("Visual to video text test")
    @allure.description("Visual to Video generate --> Visual to video test")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Visual_video_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.VisualVideo = VisualVideo(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # Perform actions on the element
        Visual = self.VisualVideo.loader_invisible_visualelement(*VisualVideoLocators.visual_txt)  # click on recent projects
        if Visual:
            assert (Visual.is_displayed(), f"element with name '{Visual.text}' is not present on the page.")

        print(Visual.text)

    @allure.title("Visual to video generate proceed buton element")
    @allure.description("Visual to Video --> proceed buton")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Visual_video_Page_proceed_element(self):
        self.LogInPage = LogInPage(self.driver)
        self.VisualVideo = VisualVideo(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # Perform actions on the element
        proceed_btn = self.VisualVideo.loader_invisible_visualelement(*VisualVideoLocators.proceed)  # click on recent projects
        if proceed_btn:
            assert (proceed_btn.is_displayed(), f"element with name '{proceed_btn.text}' is not present on the page.")

        print(proceed_btn.text)

    @allure.title("Visual to video drag drop text test")
    @allure.description("Visual to Video drag drop --> Visual to video drag drop test")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Visual_video_dragdrop(self):
        self.LogInPage = LogInPage(self.driver)
        self.VisualVideo = VisualVideo(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # Perform actions on the element
        dropfiles = self.VisualVideo.loader_invisible_visualelement(*VisualVideoLocators.dropfiles)  # get element
        if dropfiles:
            assert (dropfiles.is_enabled(), f"element with name '{dropfiles.text}' is not present on the page.")

        print(dropfiles.text)
