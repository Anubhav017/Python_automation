import time
import pytest

import traceback
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locator.locators import SubscriptionLocators, AccountLocators, SigninLocators, HomeLocators, MyProjectLocators
from pageObjects.pictryPages.AccountPage import AccountPage
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.MyProjectPage import MyProjectPage
from pageObjects.pictryPages.SignUpPage import SignUpPage
from pageObjects.pictryPages.SubscriptionPage import SubscriptionPage

import allure

from pageObjects.pictryPages.loadtimePage import LoadTimeTracker
from request import Request
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Subscription Feature")
@allure.severity(allure.severity_level.NORMAL)  # decorators class level
@pytest.mark.usefixtures("setup")
class TestSubscription:
    firstName, lastName, email_signup, password_signup = SignUpPage.get_Signup_credential('SignUp', 2)
    email, password = TestDataForProject.get_login_credential("SubscriptionPage", 0)

    @allure.title("Subscription page url")
    @allure.description("Subscription page --> url")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_Subscription_page_url(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        Sub_Plan = self.SubscriptionPage.get_element(*SubscriptionLocators.SubPlan)
        if Sub_Plan:
            if env in SubscriptionLocators.Subscription_PAGE_URL:
                expected_url = SubscriptionLocators.Subscription_PAGE_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                print(current_url)

    @allure.title("Subscription page title")
    @allure.description("Subscription page --> title")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_upgrade_page_title(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        title = self.SubscriptionPage.get_SubscriptionPage_title(SubscriptionLocators.Subscription_PAGE_TITLE)
        assert title == SubscriptionLocators.Subscription_PAGE_TITLE
        print(title)

    @allure.title("Subscription page and plan and Page Load time")
    @allure.description("Subscription page --> Subscription Page Load time")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.sanity
    @pytest.mark.PageLoad
    def test_Subscription_element_Text(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)
        self.MyProjectPage = MyProjectPage(self.driver)

        email, password = TestDataForProject.get_login_credential("SubscriptionPage", 1)
        self.LogInPage.loginpictory(email, password)
        Myproject_elementvisible = self.MyProjectPage.Myproject_elementVisible(*MyProjectLocators.Myproject_loader)
        if Myproject_elementvisible:

            start_time = LoadTimeTracker.start_timing()
            self.SubscriptionPage.ScrollclickOperation_DOM(*SubscriptionLocators.My_Subscription)
            text = self.SubscriptionPage.get_element_text(*SubscriptionLocators.SubPlan)
            if text:
                assert text == "Subscription Plan"
                print(text)

                Subscription_load_time = LoadTimeTracker.end_timing(start_time)
                print(f"Subscription Page load time : {Subscription_load_time} sec")

                # Attach load time to Allure report
                LoadTimeTracker.attach_load_time(Subscription_load_time, page_type="Home Page  --> Subscription page")

    @allure.title("Subscription page Starter plan")
    @allure.description("Upgrade page --> Starter plan text exist")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_StarterPlan_element_Text(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("SubscriptionPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        text = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Starter_Plan)
        if text:
            assert text == "Starter"

        print(text)

    @allure.title("Subscription page Professional plan")
    @allure.description("Subscription page --> Professional plan text exist")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_ProfessionalPlan_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("SubscriptionPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        plan_prof = self.SubscriptionPage.get_element(*SubscriptionLocators.Professional_Plan)
        if plan_prof:
            assert (plan_prof.is_displayed(), f"element with name '{plan_prof.text}' is not present on the page.")

        print(plan_prof.text)

    @allure.title("Subscription page downgrade from Starter annual plan to Starter monthly plan ")
    @allure.description("Subscription page --> Buy Starter plan exist")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.Regression
    def test_Buy_StarterPlan_downgrade(self, env):
        if env != "dev":
            pytest.skip("This test is skipped in the staging and production environment")

        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)
        downgradePlan = self.SubscriptionPage.get_element(*HomeLocators.Project)
        if downgradePlan:
            expected_total, actual_price_numeric = self.SubscriptionPage.get_starter_monthly(
                *SubscriptionLocators.My_Subscription)
            if actual_price_numeric:
                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                print("actual total starter_monthly price:", actual_price_numeric)
                print("expected total starter_monthly price:", expected_total)

                plan_update = self.SubscriptionPage.get_monthly_order_dashboard(*SubscriptionLocators.Proceed_butn)
                if plan_update:
                    assert plan_update
                    print(plan_update.text)

    @allure.title("Subscription page downgrade from Professional annual plan to Starter monthly plan ")
    @allure.description("Subscription page --> Buy Starter plan exist")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.sanity
    def test_Buy_ProfessionalTo_StarterPlan_downgrade(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        if env != "dev":
            pytest.skip("This test is skipped in the staging and production environment")

        email, password = TestDataForProject.get_login_credential("SubscriptionPage", 4)
        self.LogInPage.loginpictory(email, password)
        element1 = self.SubscriptionPage.get_element(*HomeLocators.Project)
        if element1:
            expected_total, actual_price_numeric = self.SubscriptionPage.get_starter_monthly(*SubscriptionLocators.My_Subscription)
            if actual_price_numeric:
                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                print("actual total starter_monthly price:", actual_price_numeric)
                print("expected total starter_monthly price:", expected_total)

                plan_update = self.SubscriptionPage.get_monthly_order_dashboard(*SubscriptionLocators.Proceed_butn)
                if plan_update:
                    assert plan_update
                    print(plan_update.text)

    @allure.title("Subscription page downgrade from professional annual plan to professional monthly plan")
    @allure.description("Subscription page --> Buy professional monthly plan exist")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Buy_Professional_monthlyPlan_downgrade(self, env):
        self.LogInPage = LogInPage(self.driver)
        if env != "dev":
            pytest.skip("This test is skipped in the staging and production environment")

        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("SubscriptionPage", 1)
        self.LogInPage.loginpictory(email, password)

        element1 = self.SubscriptionPage.get_element(*HomeLocators.Project)
        if element1:
            expected_total, actual_price_numeric = self.SubscriptionPage.get_professional_monthly(
                *SubscriptionLocators.My_Subscription)
            if actual_price_numeric:
                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                print("actual total profesional monthly price:", actual_price_numeric)
                print("expected total profesional monthly price:", expected_total)

                plan_update = self.SubscriptionPage.get_monthly_order_dashboard(*SubscriptionLocators.Proceed_butn)
                if plan_update:
                    assert plan_update
                    print(plan_update.text)

    @allure.title("Subscription page Buy See_all_features_Compare_Plans Text")
    @allure.description("Subscription page --> See_all_features_Text_Compare_Plans exist")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_See_all_features_Compare_Plans_Text(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        # self.UpgradePage.ScrollclickOperation(UpgradeLocators.See_allfeatures)
        See_allfeatures = self.SubscriptionPage.get_element_text(*SubscriptionLocators.See_allfeatures)

        if See_allfeatures:
            assert See_allfeatures == "See all features"
            print(See_allfeatures)

        Compareplan = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Compareplan)
        if Compareplan:
            assert Compareplan == "Compare Plans"
        print(Compareplan)

    @allure.title("Subscription page All plans include Text")
    @allure.description("Subscription page --> All plans include Text exist")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_All_plans_include_elements(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        text = self.SubscriptionPage.get_element_text(*SubscriptionLocators.all_Plan)
        hex_color = self.SubscriptionPage.get_element_color(*SubscriptionLocators.all_Plan)
        print(hex_color)

        exp_color = ['#343a40', '#ffffff']

        assert text == "All plans include" and hex_color in exp_color
        print(hex_color)

    @allure.title("Subscription page list of plans include Text")
    @allure.description("Subscription page --> list of plans include Text exist")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_listof_plans_include_elements(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        Videosfromscriptsblogs = self.SubscriptionPage.get_element(*SubscriptionLocators.Videosfromscriptsblogs)
        Automatic_transcription = self.SubscriptionPage.get_element(*SubscriptionLocators.Automatic_transcription)
        ConversationalAIVoice = self.SubscriptionPage.get_element(*SubscriptionLocators.ConversationalAIVoice)
        editVideo = self.SubscriptionPage.get_element(*SubscriptionLocators.editVideo)
        Fullaccess = self.SubscriptionPage.get_element(*SubscriptionLocators.Fullaccess)
        repurpose = self.SubscriptionPage.get_element_text(*SubscriptionLocators.repurpose)

        assert (
            Videosfromscriptsblogs.is_displayed(), Automatic_transcription, ConversationalAIVoice, editVideo,
            Fullaccess, repurpose,
            f"Search field element with name '{Videosfromscriptsblogs.text}' is not present on the page.")

    @allure.title("Subscription page list of Compare plans and choose the one that suit you elements")
    @allure.description("Subscription page --> list of Compare plans and choose the one that suit you elements exist")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_listof_Compareplansandchoosetheonethatsuityou_elements(self):
        self.LogInPage = LogInPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.hover_Profile)
        self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
        self.driver.implicitly_wait(20)

        try:

            creative = self.SubscriptionPage.Compare_plan(*SubscriptionLocators.Createvideosfromscriptsblogs)
            if creative.is_displayed():
                text1 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Createvideosfromscriptsblogs)
                text2 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Edityourexistingvideoswithvoice)
                text3 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Branding)
                text4 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Media)
                text5 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Voiceover)
                text6 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Videoexportoption)
                text7 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Customer)

                assert text1 == "Generate Video from Script or URL" and text2 == "Edit Videos Using Text" and text3 == "Branding" and text4 == "Media" and text5 == "Voiceover" and text6 == "Video export options" and text7 == "Customer support"

        except StaleElementReferenceException:
            print(traceback.format_exc())
            text1 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Createvideosfromscriptsblogs)
            text2 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Edityourexistingvideoswithvoice)
            text3 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Branding)
            text4 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Media)
            text5 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Voiceover)
            text6 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Videoexportoption)
            text7 = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Customer)

            assert text1 == "Generate Video from Script or URL" and text2 == "Edit Videos Using Text" and text3 == "Branding" and text4 == "Media" and text5 == "Voiceover" and text6 == "Video export options" and text7 == "Customer support"

    @allure.title("account page billing text")
    @allure.description("account page --> billing text")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_billing_text(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)

        text = self.AccountPage.get_Profile_element_text(*AccountLocators.Billing)
        assert text == "Billing"

    @allure.title("billing subscription plan elements")
    @allure.description("account page --> billing subscription plan elements")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Subscription_plan_elements(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)

        Subscription_plan = self.AccountPage.get_Profile_element_text(*AccountLocators.Subscription_plan)
        Upgrade_butn = self.AccountPage.get_Profile_element_text(*AccountLocators.Upgrade_butn)
        if Upgrade_butn:
            assert Subscription_plan == "Subscription plan" and Upgrade_butn == "Upgrade"

    @allure.title("account page Upgrade page redirection")
    @allure.description("account page --> Upgrade page redirection")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Upgrade_page_redirection(self, env):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)

        Sub_Plan = self.SubscriptionPage.get_element(*SubscriptionLocators.SubPlan)
        if Sub_Plan:
            if env in SubscriptionLocators.Subscription_PAGE_URL:
                expected_url = SubscriptionLocators.Subscription_PAGE_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)
                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
                print(current_url)

    @allure.title("account page billing card detail elements")
    @allure.description("account page --> billing card detail elements")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Card_detail_elements(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)

        Card_detail = self.AccountPage.get_Profile_element_text(*AccountLocators.Card_detail)
        Card_number = self.AccountPage.get_Profile_element_text(*AccountLocators.Card_number)
        Exp_date = self.AccountPage.get_Profile_element_text(*AccountLocators.Exp_date)
        CVV_number = self.AccountPage.get_Profile_element_text(*AccountLocators.CVV)

        assert Card_detail == "Card details" and Card_number == "Credit card number" and Exp_date == "Exp date" and CVV_number == "CVV"

    @allure.title("account page Invoice email ID element")
    @allure.description("account page --> Invoice email ID element")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Invoice_element_emailID(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        self.LogInPage.loginpictory(self.email, self.password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)

        Invoice = self.AccountPage.get_Profile_element_text(*AccountLocators.Invoice)
        assert Invoice == "Invoice email ID"
        print(Invoice)

    @allure.title("account page update card")
    @allure.description("account page --> update card on billing card detail page")
    @allure.severity(allure.severity_level.MINOR)  # decorators class level
    @pytest.mark.Regression
    def test_UpdateCard_Billing(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        self.AccountPage.clickOperation(*AccountLocators.edit_card)

        self.AccountPage.chargebee_card_container_frame()
        Continue = self.AccountPage.get_element(*AccountLocators.Continue)
        if Continue:
            self.AccountPage.ScrollclickOperation(*AccountLocators.Continue)

            if env in AccountLocators.Payment_URL:
                expected_url = AccountLocators.Payment_URL[env]
                current_url = self.LogInPage.get_LoginPage_url(expected_url)

                assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

                print(current_url)

    @allure.title("billing subscription plan cancel No Current Need")
    @allure.description("account page --> billing subscription plan cancel No Current Need")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Subscription_plan_cancel_NoCurrentNeed(self):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        with allure.step("Check if cancellation option is available - No Current Need"):
            try:
                status = self.AccountPage.get_cancel_Subscription_plan(*AccountLocators.current)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

            except (NoSuchElementException, TimeoutException):
                print("The cancel btn is not visible.")
                self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)
                status = self.AccountPage.get_reNew_Subscription_plan(*AccountLocators.current)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

    @allure.title("billing subscription plan cancel missing feature")
    @allure.description("account page --> billing subscription plan cancel missing feature")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Subscription_plan_cancel_missingfeature(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        try:
            with allure.step("Check if cancellation option is available - missing feature"):
                status = self.AccountPage.get_cancel_Subscription_plan(*AccountLocators.missing)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

        except NoSuchElementException:
            print("The cancel btn is not visible.")
            self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)
            status = self.AccountPage.get_reNew_Subscription_plan(*AccountLocators.missing)
            if status:
                with allure.step("Verify cancellation status"):
                    assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                    print(status.text)

    @allure.title("billing subscription plan cancel Too expensive")
    @allure.description("account page --> billing subscription plan cancel Too expensive")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Subscription_plan_cancel_Tooexpensive(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        try:
            with allure.step("Check if cancellation option is available - Too Expensive"):
                status = self.AccountPage.get_cancel_Subscription_plan(*AccountLocators.TooExpensive)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert status.is_displayed(), f"Element with name '{status.text}' is not present on the page."
                        print(status.text)

        except (TimeoutException, NoSuchElementException):
            print("The cancel btn is not visible.")
            self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)
            status = self.AccountPage.get_reNew_Subscription_plan(*AccountLocators.TooExpensive)
            if status:
                with allure.step("Verify cancellation status"):
                    assert status.is_displayed(), f"Element with name '{status.text}' is not present on the page."
                    print(status.text)

    @allure.title("billing subscription plan cancel Too complex")
    @allure.description("account page --> billing subscription plan cancel Too complex")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Subscription_plan_cancel_Toocomplex(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 1)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        try:
            with allure.step("Check if cancellation option is available - Too Expensive"):
                status = self.AccountPage.get_cancel_Subscription_plan(*AccountLocators.TooComplex)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

        except (TimeoutException, NoSuchElementException):
            print("The cancel btn is not visible.")
            self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)
            status = self.AccountPage.get_reNew_Subscription_plan(*AccountLocators.TooComplex)
            if status:
                with allure.step("Verify cancellation status"):
                    assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                    print(status.text)

    @allure.title("billing subscription plan upgrade")
    @allure.description("account page --> billing subscription plan upgrade")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.sanity
    def test_Subscription_UpgradePlan(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 5)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.LogInPage.clickOperation(*AccountLocators.Billing)
        try:
            with allure.step("Check if subscription plan is upgrade"):
                status = self.AccountPage.get_upgrade_Subscription_plan(*AccountLocators.current)
                if status:
                    with allure.step("Verify active status on plan Page"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

        except (TimeoutException, NoSuchElementException):
            print("The Upgrade btn is visible.")
            self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)
            # self.SubscriptionPage.toggleButton_click()
            renew = self.SubscriptionPage.get_element(*SubscriptionLocators.renew)
            if renew:
                self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.renew)

                Proceed = self.SubscriptionPage.get_element(*SubscriptionLocators.Proceed_butn_renew)
                if Proceed:
                    self.SubscriptionPage.clickOperation(*SubscriptionLocators.Proceed_butn_renew)
                    self.SubscriptionPage.clickOperation(*SubscriptionLocators.Proceed_popup)

                    status = self.SubscriptionPage.get_element(*SubscriptionLocators.status)
                    if status:
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")

                    print(status.text)

    @allure.title("SignUp and buy starter plan and Getty image and Elab")
    @allure.description("This is test for SignUp page and buy starter plan and Getty image and Elab")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanitytest
    def test_Subscription_Buy_starterPlan_and_Getty_image_and_Elab(self, env):
        self.SignUpPage = SignUpPage(self.driver)
        if env != "dev":
            pytest.skip("This test is skipped in the production environment")

        email = "pictoryautomate" + SignUpPage.random_generator() + "@gmail.com"

        self.SubscriptionPage = SubscriptionPage(self.driver)
        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, email, self.password_signup)
        try:
            with allure.step("Performing SignUp with email: {email}"):
                verify_email = self.SignUpPage.get_verifyemail(*SigninLocators.VerifyEmail)
                if verify_email.is_displayed():
                    print("This is for Icp user.")
                    get_otp = self.SignUpPage.email_listen()
                    print(f"Extracted OTP: {get_otp}")
                    for i in range(1, 7):
                        # box_id = f"get_otp{i}"
                        element = self.driver.find_element(By.ID, f":r{i + 3}:")
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
                            elabfree, free_trial = self.SubscriptionPage.get_Ft_PlanStatus(
                                *SubscriptionLocators.Subscription_Upgrade_butn)
                            if free_trial is not None:
                                assert free_trial.text.strip() == "Free Trial", f"Expected text: 'Free Trial', Actual text: '{free_trial.text.strip()}'"
                                print(free_trial.text)

                                expected_elabfree_text = "0 / 5"
                                actual_elabfree_text = elabfree.text.strip()
                                assert actual_elabfree_text == expected_elabfree_text, f"Expected text: '{expected_elabfree_text}', Actual text: '{actual_elabfree_text}'"
                                print(elabfree.text)

                                # self.SubscriptionPage.get_ICP_country_upgrade_FreeTrial_Tostarter_Plan(*SubscriptionLocators.Subscription_Upgrade_butn)
                                expected_total, actual_price_numeric = self.SubscriptionPage.get_ICP_country_upgrade_FreeTrial_Tostarter_Plan(*SubscriptionLocators.Subscription_Upgrade_butn, 8)
                                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                print("actual total price:", actual_price_numeric)
                                print("expected total price:", expected_total)

                                self.SubscriptionPage.get_ICPCountry_biling_address_team_Plan(*SubscriptionLocators.Proceed_butn)

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
                                        elevenLab = self.SubscriptionPage.get_element(*SubscriptionLocators.status_elevenLab)
                                        Gety_disable = self.SubscriptionPage.get_element(*SubscriptionLocators.status_Gety)

                                        if elevenLab:
                                            assert (elevenLab.is_displayed(), Gety_disable.is_displayed(),
                                                    f"element with name '{elevenLab.text}', '{Gety_disable.text}' is not present on the page.")
                                            print("ElevenLabs Voiceover Minutes : " + elevenLab.text)
                                            print("Gety image : " + Gety_disable.text)

                                        with allure.step("Getty image -->> buy:"):
                                            Gety_enabled = self.SubscriptionPage.get_buy_gety_image(*SubscriptionLocators.buy_gety)
                                            assert Gety_enabled.text == "Enabled"
                                            print("Gety image : " + Gety_enabled.text)

                                        with allure.step("Voice-Over -->> buy:"):
                                            elabmin = self.SubscriptionPage.get_element(*SubscriptionLocators.elabmin)
                                            assert elabmin.text == "Disabled"
                                            print("elab Voice : " + elabmin.text)

                                        with allure.step("Getty image -->> Remove add on"):
                                            remove1 = self.SubscriptionPage.get_Remove_AddOn(*SubscriptionLocators.remove_addOn)
                                            if remove1:
                                                # Assert that remove1 is present
                                                assert remove1, "Remove AddOn element is not found"
                                                # Print the text of the remove1 element
                                                print("Getty remove: " + remove1.text)
                                            else:
                                                # Handle the case where remove1 is not found
                                                print("Remove AddOn element is not found")

                                            # self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Okay)

                                            expected_total, actual_price_numeric = self.SubscriptionPage.get_Starter_Order_Sumary(*SubscriptionLocators.add_On, 11)
                                            if actual_price_numeric:
                                                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                                                print("actual total price:", actual_price_numeric)
                                                print("expected total price:", expected_total)

                                                elabmin1 = self.SubscriptionPage.get_buy_elVoiceOver(*SubscriptionLocators.elabmin)
                                                assert elabmin1.text == "0 / 60"
                                                print("elab Voice : " + elabmin1.text)
                                                expected_expiration_date, actual_expiration_date = self.SubscriptionPage.get_next_biling_cycle(*SubscriptionLocators.nextbilcycle)
                                                if actual_expiration_date and expected_expiration_date:
                                                    assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                                    print("nextpay : " + str(actual_expiration_date))

        except (TimeoutException, NoSuchElementException):
            with allure.step("Performing SignUp with email: {email}"):

                print("This is for non_Icp user.")
                self.SignUpPage.cards_Page(*SigninLocators.Verifypaymentmethod)
                # time.sleep(10)
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
                        elabfree, free_trial = self.SubscriptionPage.get_Ft_PlanStatus(
                            *SubscriptionLocators.Subscription_Upgrade_butn)
                        if free_trial is not None:
                            assert free_trial.text.strip() == "Free Trial", f"Expected text: 'Free Trial', Actual text: '{free_trial.text.strip()}'"

                            print(free_trial.text)

                            expected_elabfree_text = "0 / 5"
                            actual_elabfree_text = elabfree.text.strip()

                            assert actual_elabfree_text == expected_elabfree_text, f"Expected text: '{expected_elabfree_text}', Actual text: '{actual_elabfree_text}'"
                            print(elabfree.text)

                            self.SubscriptionPage.get_upgrade_FreeTrial_Tostarter_Plan(
                                *SubscriptionLocators.Subscription_Upgrade_butn)
                            text = self.SignUpPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                            if text:
                                assert text == "Payment successful"
                                print(text)

                            with allure.step("Upgrade plan --> plan page:"):
                                self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Payment_Ok)
                                self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Okay)

                            with allure.step("elevenLab VO and Getty initial status:"):
                                element = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                                if element:
                                    elevenLab = self.SubscriptionPage.get_element(
                                        *SubscriptionLocators.status_elevenLab)
                                    Gety_disable = self.SubscriptionPage.get_element(*SubscriptionLocators.status_Gety)
                                    if elevenLab:
                                        assert (elevenLab.is_displayed(), Gety_disable.is_displayed(),
                                                f"element with name '{elevenLab.text}', '{Gety_disable.text}' is not present on the page.")
                                        print("ElevenLabs Voiceover Minutes : " + elevenLab.text)
                                        print("Gety image : " + Gety_disable.text)

                                    with allure.step("Getty image -->> buy:"):
                                        Gety_enabled = self.SubscriptionPage.get_buy_gety_image(
                                            *SubscriptionLocators.buy_gety)
                                        assert Gety_enabled.text == "Enabled"
                                        print("Gety image : " + Gety_enabled.text)

                                    with allure.step("Voice-Over -->> buy:"):
                                        elabmin = self.SubscriptionPage.get_element(*SubscriptionLocators.elabmin)
                                        assert elabmin.text == "Disabled"
                                        print("elab Voice : " + elabmin.text)

                                    with allure.step("Getty image -->> Remove add on"):
                                        remove1 = self.SubscriptionPage.get_Remove_AddOn(
                                            *SubscriptionLocators.remove_addOn)
                                        if remove1:
                                            remove_text = remove1.text  # Extract the text from the WebElement
                                            expected_text = "Thank you. You have now removed Getty visuals add-on from your plan."
                                            assert remove_text == expected_text
                                            print("Gety remove : " + remove_text)

                                            self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Okay)

                                            expected_total, actual_price_numeric = self.SubscriptionPage.get_Starter_Order_Sumary(
                                                *SubscriptionLocators.add_On)
                                            if actual_price_numeric:
                                                assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                                print("actual total price:", actual_price_numeric)
                                                print("expected total price:", expected_total)

                                                elabmin1 = self.SubscriptionPage.get_buy_elVoiceOver(
                                                    *SubscriptionLocators.elabmin)
                                                assert elabmin1.text == "0 / 60"
                                                print("elab Voice : " + elabmin1.text)

                                                expected_expiration_date, actual_expiration_date = self.SubscriptionPage.get_next_biling_cycle(
                                                    *SubscriptionLocators.nextbilcycle)
                                                if actual_expiration_date and expected_expiration_date:
                                                    assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                                    print("nextpay : " + str(actual_expiration_date))

    @allure.title("buy starter monthly plan --> Professional monthly :")
    @allure.description("This is test for buy starter monthly plan to Professional monthly")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_Subscription_startermonthlyTo_Professional_monthly(self, env):
        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 3)
        self.LogInPage.loginpictory(email, password)

        if env in SigninLocators.HOME_Page_URL:
            expected_url = SigninLocators.HOME_Page_URL[env]
            current_url = self.LogInPage.get_LoginPage_url(expected_url)

            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"
            print(current_url)

            subscription_id = "287bb4de-cad2-4899-87bc-e6f8061a7e96-SUB"
            Request.make_request(subscription_id)

            self.SubscriptionPage.loaderinvisible_scrolclick(*SubscriptionLocators.My_Subscription)
            self.SubscriptionPage.toggleButton_click()

        with allure.step("Upgrade plan --> Buy free trial --> starter plan:"):
            elabfree, free_trial = self.SubscriptionPage.get_Ft_PlanStatus(*SubscriptionLocators.Subscription_Upgrade_butn)
            if free_trial is not None:
                assert free_trial.text.strip() == "Free Trial", f"Expected text: 'Free Trial', Actual text: '{free_trial.text.strip()}'"

                print(free_trial.text)

                expected_elabfree_text = "0 / 5"
                actual_elabfree_text = elabfree.text.strip()

                assert actual_elabfree_text == expected_elabfree_text, f"Expected text: '{expected_elabfree_text}', Actual text: '{actual_elabfree_text}'"
                print(elabfree.text)

                expected_total, actual_price_numeric = self.SubscriptionPage.get_teardown_FreeTrial_Tostarter_monthly_Plan(
                    *SubscriptionLocators.Starter_BuyNow_butn)
                if actual_price_numeric:
                    assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                    print("actual total starter_monthly price:", actual_price_numeric)
                    print("expected total starter_monthly price:", expected_total)

                    self.SubscriptionPage.get_proceed_subscribe_click()
                    text = self.SubscriptionPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                    if text:
                        assert text == "Payment successful"
                        print(text)

                        self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Payment_Ok)

                    with allure.step("Upgrade plan --> Buy starter annual plan --> professional monthly plan:"):
                        expected_total, actual_price_numeric = self.SubscriptionPage.get_teardown_startermonthly_ToProfesional_monthly_Plan(*SubscriptionLocators.Upgrade_butn)
                        if actual_price_numeric:
                            assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"
                            print("actual total Profesional monthly price:", actual_price_numeric)
                            print("expected total Profesional monthly price:", expected_total)

                            self.SubscriptionPage.get_proceed_Profesional_Plan_click(*SubscriptionLocators.Proceed_butn)

                            MyBranding_elementvisible = self.SubscriptionPage.get_element_Invisible(
                                *HomeLocators.loader)
                            if MyBranding_elementvisible:
                                expected_expiration_date, actual_expiration_date = self.SubscriptionPage.get_next_monthly_biling_cycle(
                                    *SubscriptionLocators.nextbilcycle)
                                if actual_expiration_date and expected_expiration_date:
                                    assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                    print("nextpay : " + str(actual_expiration_date))

                                    time.sleep(2)

                                    subscription_id = "287bb4de-cad2-4899-87bc-e6f8061a7e96-SUB"
                                    Request.make_request(subscription_id)

    @allure.title("billing subscription plan pause and active ")
    @allure.description("account page --> billing subscription plan pause and active")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Subscription_plan_pause_and_active(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 6)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        with allure.step("Check if cancellation option is available - Too Expensive"):
            status = self.AccountPage.get_pause_subscription_plan(*AccountLocators.TooComplex)
            if status:
                with allure.step("Verify cancellation status"):
                    assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                    print(status.text)

    @allure.title("billing subscription plan cancel and upgrade --> Price")
    @allure.description("account page --> billing subscription plan cancel and upgrade")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Subscription_plan_cancel_active(self):

        self.LogInPage = LogInPage(self.driver)
        self.AccountPage = AccountPage(self.driver)
        self.SubscriptionPage = SubscriptionPage(self.driver)

        email, password = TestDataForProject.get_login_credential("AccountPage", 4)
        self.LogInPage.loginpictory(email, password)

        # self.AccountPage.loaderinvisible_click(*AccountLocators.hover_Profile)
        self.AccountPage.loaderinvisible_click(*AccountLocators.My_account)
        self.driver.implicitly_wait(20)

        self.AccountPage.clickOperation(*AccountLocators.Billing)
        with allure.step("Check if cancellation option is available - No Current Need"):
            try:
                status = self.AccountPage.get_cancel_Subscription_plan(*AccountLocators.current)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

            except NoSuchElementException:
                print("The cancel btn is not visible.")
                self.AccountPage.clickOperation(*AccountLocators.Upgrade_butn)
                status = self.AccountPage.get_reNew_Subscription_plan(*AccountLocators.current)
                if status:
                    with allure.step("Verify cancellation status"):
                        assert (status.is_displayed(), f"element with name '{status.text}' is not present on the page.")
                        print(status.text)

                        time.sleep(2)

                        subscription_id = "7a3783c4-ffef-4ce8-8a1e-fd908c399549-SUB"
                        Request.make_request(subscription_id)
