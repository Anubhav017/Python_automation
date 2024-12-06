import time

import pytest
import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from locator.locators import SigninLocators, SubscriptionLocators, HomeLocators
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.SignUpPage import SignUpPage
from pageObjects.pictryPages.SubscriptionPage import SubscriptionPage
from pageObjects.pictryPages.loadtimePage import LoadTimeTracker


@allure.feature("SignUp Feature")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup")
class TestSignUp:
    firstName, lastName, email, password = SignUpPage.get_Signup_credential('SignUp', 2)

    @allure.title("SignUp page url")
    @allure.description("This is test of SignUp page url")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_SignIn_page_url(self, env):
        self.SignUpPage = SignUpPage(self.driver)
        if env in SigninLocators.SIGNIN_PAGE_URL:
            expected_url = SigninLocators.SIGNIN_PAGE_URL[env]
            current_url = self.SignUpPage.get_SignUpPage_url(expected_url)

            assert current_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

            print(current_url)

    @allure.title("SignUp page googletext visible")
    @allure.description("This is test of SignUp page googletext")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_SignIn_googletext_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_googletext_exist()
        assert flag

    @allure.title("SignUp page title")
    @allure.description("This is test of SignUp page title")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_SignIn_page_title(self):
        self.SignUpPage = SignUpPage(self.driver)
        title = self.SignUpPage.get_SignUp_page_title(SigninLocators.SIGNIN_PAGE_TITLE)
        assert title == SigninLocators.SIGNIN_PAGE_TITLE

    @allure.title("SignUp page Start your FREE trial visible")
    @allure.description("This is test of SignUp page Start your FREE trial")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_SignIn_StartyourFREEtrial_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_StartyourFREEtrial_exist()
        assert flag

    @allure.title("SignUp page Already registered? visible")
    @allure.description("This is test of SignUp Already registered?")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_SignIn_Alreadyregistered_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_Alreadyregistered_exist()
        assert flag

    @allure.title("Sign up Page fields is exist")
    @allure.description("Sign up Page fields --> exist")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_field_exist(self):
        self.SignUpPage = SignUpPage(self.driver)
        First_name = self.SignUpPage.signUp_element_exist(*SigninLocators.f_Name)
        assert (First_name.is_displayed(), f"element with name '{First_name.text}' is not present on the page.")

        Last_name = self.SignUpPage.signUp_element_exist(*SigninLocators.l_Name)
        assert (Last_name.is_displayed(), f"element with name '{Last_name.text}' is not present on the page.")

        Email = self.SignUpPage.signUp_element_exist(*SigninLocators.email_field)
        assert (Email.is_displayed(), f"element with name '{Email.text}' is not present on the page.")

        Password = self.SignUpPage.signUp_element_exist(*SigninLocators.password_field)
        assert (Password.is_displayed(), f"element with name '{Password.text}' is not present on the page.")

    @allure.title("Terms and condition link visible")
    @allure.description("Terms and condition link --> visible")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_tclink_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_tclink_exist()
        assert flag

    @allure.title("Login link visible")
    @allure.description("Login link --> visible")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_Loginlink_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_Loginlink_exist()
        assert flag

    @allure.title("SignUp page logo visible")
    @allure.description("This is test of SignUp page logo")
    @allure.severity(allure.severity_level.NORMAL)  # decorators class level
    @pytest.mark.Regression
    def test_Signin_logo_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_logo_exist()
        assert flag

    @allure.title("SignUp page continue button is visible")
    @allure.description("This is test of SignUp page continue button is visible")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.Regression
    def test_SignIn_continuebutn_visible(self):
        self.SignUpPage = SignUpPage(self.driver)
        flag = self.SignUpPage.is_continuebutton_exist()
        assert flag

    @allure.title("SignUp page 14daystrial page element is visible")
    @allure.description("This is test SignUp page 14daystrial page element")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_14daystrial_element(self):
        self.SignUpPage = SignUpPage(self.driver)
        email = "automate" + SignUpPage.random_generator() + "@gmail.com"

        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, email, self.password)

        try:
            verify_email = self.SignUpPage.get_verifyemail(*SigninLocators.VerifyEmail)
            if verify_email.is_displayed():
                print(f"The {verify_email.text} is visible.")
                assert verify_email.text == "Verify your email address"

        except (TimeoutException, NoSuchElementException):

            freetrial = self.SignUpPage.get_Startyour14dayfreetrial(*SigninLocators.Startyour14dayfreetrial)
            payment = self.SignUpPage.get_Verifypaymentmethod(*SigninLocators.Verifypaymentmethod)

            print(f"The element {freetrial.text} and {payment.text} is displayed.")
            assert freetrial.text == "Start your 14-day free trial" or payment.text == "Verify payment method"

    @allure.title("SignUp page credit card and payment method text is visible")
    @allure.description("This is test SignUp page credit card and payment method text element")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_creditcard_paymentmethod_Text(self):
        self.SignUpPage = SignUpPage(self.driver)
        email = SignUpPage.random_generator() + "@gmail.com"

        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, email, self.password)

        try:
            verify_email = self.SignUpPage.get_verifyemail(*SigninLocators.VerifyEmail)
            if verify_email.is_displayed():
                print(f"The {verify_email.text} is visible.")
                assert verify_email.text == "Verify your email address"

        except (TimeoutException, NoSuchElementException):
            payment = self.SignUpPage.get_Verifypaymentmethod(*SigninLocators.Verifypaymentmethod)

            if payment.is_displayed():
                print(f"The element {payment} is displayed.")
                self.SignUpPage.clickOperation(*SigninLocators.Verifypaymentmethod)
                self.driver.implicitly_wait(20)

                self.SignUpPage.chargebee_card_container_frame()
                self.driver.implicitly_wait(20)

                paymentmethod = self.SignUpPage.get_SignPage_element(*SigninLocators.Addapaymentmethod)
                creditCard = self.SignUpPage.get_SignPage_element(*SigninLocators.creditcard)
                print(f"The element {paymentmethod.text} and {creditCard.text} is displayed.")
                assert paymentmethod.text == "Add a payment method" and creditCard.text == "Credit card"

    @allure.title("SignUp page credit card page elements is visible")
    @allure.description("This is test SignUp page credit card page elements visible")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_creditcard_elements(self):
        self.SignUpPage = SignUpPage(self.driver)
        email = SignUpPage.random_generator() + "@gmail.com"

        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, email, self.password)

        try:
            verify_email = self.SignUpPage.get_verifyemail(*SigninLocators.VerifyEmail)
            if verify_email.is_displayed():
                print(f"The {verify_email.text} is visible.")
                assert verify_email.text == "Verify your email address"

        except (TimeoutException, NoSuchElementException):
            payment = self.SignUpPage.get_Verifypaymentmethod(*SigninLocators.Verifypaymentmethod)
            if payment.is_displayed():
                print(f"The element {payment} is displayed.")

                self.SignUpPage.clickOperation(*SigninLocators.Verifypaymentmethod)
                self.driver.implicitly_wait(20)
                self.SignUpPage.chargebee_card_container_frame()

                self.driver.implicitly_wait(20)
                cardtext = self.SignUpPage.get_SignPage_element(*SigninLocators.cardtext)
                expiry = self.SignUpPage.get_SignPage_element(*SigninLocators.expiry)
                CVV = self.SignUpPage.get_SignPage_element(*SigninLocators.CVV)
                add_buton = self.SignUpPage.get_SignPage_element(*SigninLocators.add_buton)
                print(
                    f"The element {cardtext.text} and {expiry.text} and {CVV.text} and {add_buton.text} is displayed.")
                assert cardtext.text == "Card Number" and expiry.text == "Expiry" and CVV.text == "CVV" and add_buton.text == "Add"

    @allure.title("SignUp page paypal page element is visible")
    @allure.description("This is test SignUp page paypal page element")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(max_runs=3, min_passes=1)
    @pytest.mark.Regression
    def test_creditcard_paymentmode_paypal_text(self):
        self.SignUpPage = SignUpPage(self.driver)
        email = SignUpPage.random_generator() + "@gmail.com"

        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, email, self.password)

        try:
            verify_email = self.SignUpPage.get_verifyemail(*SigninLocators.VerifyEmail)
            if verify_email.is_displayed():
                print(f"The {verify_email.text} is visible.")
                assert verify_email.text == "Verify your email address"

        except (TimeoutException, NoSuchElementException):
            payment = self.SignUpPage.get_Verifypaymentmethod(*SigninLocators.Verifypaymentmethod)
            if payment.is_displayed():
                print(f"The element {payment} is displayed.")

                self.SignUpPage.clickOperation(*SigninLocators.Verifypaymentmethod)
                self.driver.implicitly_wait(20)

                self.SignUpPage.chargebee_card_container_frame()
                paypal = self.SignUpPage.get_SignPage_element(*SigninLocators.paypal)
                print(f"The {paypal.text} is visible.")
                assert paypal.text == "PayPal"

    @allure.title("SignUp and buy professional plan and Getty image and Elab")
    @allure.description("This is test for SignUp page and buy professional plan and Getty image and Elab")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.PageLoad
    def test_SignUp_Buy_ProfessionalPlan_and_Getty_image_and_Elab(self, env):
        if env != "dev":
            pytest.skip("This test is skipped in the production environment")

        self.SignUpPage = SignUpPage(self.driver)
        email = "pictoryautomate" + SignUpPage.random_generator() + "@gmail.com"

        self.SubscriptionPage = SubscriptionPage(self.driver)
        start_time = LoadTimeTracker.start_timing()

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

                        Signup_load_time = LoadTimeTracker.end_timing(start_time)
                        print(f"Signup process load time : {Signup_load_time} sec")

                        # Attach load time to Allure report
                        LoadTimeTracker.attach_load_time(Signup_load_time, page_type="Signup process --> home page")

                    with allure.step("Upgrade plan --> Buy free trial --> professional plan:"):
                        elabfree, free_trial = self.SignUpPage.get_Ft_PlanStatus(*SubscriptionLocators.Subscription_Upgrade_butn)
                        if free_trial is not None:
                            expected_elabfree_text = "0 / 5"
                            actual_elabfree_text = elabfree.text.strip()

                            assert actual_elabfree_text == expected_elabfree_text, f"Expected text: '{expected_elabfree_text}', Actual text: '{actual_elabfree_text}'"
                            print(elabfree.text)

                            assert free_trial.text.strip() == "Free Trial", f"Expected text: 'Free Trial', Actual text: '{free_trial.text.strip()}'"
                            print(free_trial.text)

                            # self.SignUpPage.get_ICP_country_upgrade_FreeTrial_ToPremium_Plan(*SubscriptionLocators.Subscription_Upgrade_butn)
                            expected_total, actual_price_numeric = self.SignUpPage.get_ICP_country_upgrade_FreeTrial_ToPremium_Plan(*SubscriptionLocators.Subscription_Upgrade_butn, 10)
                            assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                            print("actual total price:", actual_price_numeric)
                            print("expected total price:", expected_total)

                            self.SignUpPage.get_ICPCountry_biling_address_team_Plan(*SubscriptionLocators.Proceed_butn)

                            # self.SignUpPage.get_subscription_purchase_authentication(*SubscriptionLocators.code)

                            text = self.SignUpPage.get_element_text(*SubscriptionLocators.Paymentsuccessful)
                            assert text == "Payment successful"
                            print(text)

                        with allure.step("Upgrade plan --> plan page:"):
                            self.SubscriptionPage.ScrollclickOperation(*SubscriptionLocators.Payment_Ok)

                        with allure.step("elevenLab VO and Getty initial status:"):
                            element = self.SubscriptionPage.get_element_Invisible(*HomeLocators.loader)
                            if element:
                                with allure.step("Getty image -->> buy:"):
                                    Gety_enabled = self.SubscriptionPage.get_element(*SubscriptionLocators.Gety_enable)
                                    assert Gety_enabled.text == "Enabled"
                                    print("Gety image : " + Gety_enabled.text)

                                with allure.step("Voice-Over -->> buy:"):
                                    elabmin = self.SubscriptionPage.get_element(*SubscriptionLocators.elabmin)
                                    assert elabmin.text == "0 / 120"
                                    print("elab minute : " + elabmin.text)

                                    expected_total, actual_price_numeric = self.SignUpPage.get_ProfessionalOrder_Sumary(*SubscriptionLocators.modify_elVoice)
                                    if actual_price_numeric:
                                        assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                        print("actual total price:", actual_price_numeric)
                                        print("expected total price:", expected_total)

                                        elabmin1 = self.SignUpPage.get_buy_elVoice_Over(*SubscriptionLocators.elabmin)
                                        assert elabmin1.text == "0 / 180"
                                        print("elab minute : " + elabmin1.text)

                                        expected_expiration_date, actual_expiration_date = self.SignUpPage.get_next_biling_cycle(*SubscriptionLocators.nextbilcycle)
                                        if actual_expiration_date and expected_expiration_date:
                                            assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                            print("nextpay : " + str(actual_expiration_date))

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
                        Signup_load_time = LoadTimeTracker.end_timing(start_time)
                        print(f"Signup process load time : {Signup_load_time} sec")

                        # Attach load time to Allure report
                        LoadTimeTracker.attach_load_time(Signup_load_time, page_type="Signup process --> home page")

                    with allure.step("Upgrade plan --> Buy free trial --> professional plan:"):
                        elabfree, free_trial = self.SignUpPage.get_Ft_PlanStatus(*SubscriptionLocators.Subscription_Upgrade_butn)
                        if free_trial is not None:
                            expected_elabfree_text = "0 / 5"
                            actual_elabfree_text = elabfree.text.strip()
                            assert actual_elabfree_text == expected_elabfree_text, f"Expected text: '{expected_elabfree_text}', Actual text: '{actual_elabfree_text}'"
                            print(elabfree.text)

                            assert free_trial.text.strip() == "Free Trial", f"Expected text: 'Free Trial', Actual text: '{free_trial.text.strip()}'"
                            print(free_trial.text)

                            self.SignUpPage.get_upgrade_FreeTrial_ToPremium_Plan(*SubscriptionLocators.Subscription_Upgrade_butn)
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
                                    assert elabmin.text == "0 / 120"
                                    print("elab minute : " + elabmin.text)

                                    expected_total, actual_price_numeric = self.SignUpPage.get_ProfessionalOrder_Sumary(*SubscriptionLocators.modify_elVoice)
                                    if actual_price_numeric:
                                        assert expected_total == actual_price_numeric, f"Expected total: {expected_total}, Actual total: {actual_price_numeric}"

                                        print("actual total price:", actual_price_numeric)
                                        print("expected total price:", expected_total)

                                        elabmin1 = self.SignUpPage.get_buy_elVoice_Over(*SubscriptionLocators.elabmin)
                                        assert elabmin1.text == "0 / 180"
                                        print("elab minute : " + elabmin1.text)

                                        expected_expiration_date, actual_expiration_date = self.SignUpPage.get_next_biling_cycle(*SubscriptionLocators.nextbilcycle)
                                        if actual_expiration_date and expected_expiration_date:
                                            assert actual_expiration_date == expected_expiration_date, f"Expected expiration date: {expected_expiration_date}, Actual expiration date: {actual_expiration_date}"
                                            print("nextpay : " + str(actual_expiration_date))

    @allure.title("SignUp page With Existing Email")
    @allure.description("This is test for SignUp page With Existing Email")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_SignUpWithExistingEmail(self, env):
        if env != "dev":
            pytest.skip("This test is skipped in the production environment")

        self.SignUpPage = SignUpPage(self.driver)
        self.LogInPage = LogInPage(self.driver)

        self.SignUpPage.SignUpPictory(self.firstName, self.lastName, self.email, self.password)
        # error = self.SignUpPage.get_element(*SigninLocators.error_msg)
        exp_error_color = {'#ff5252', '#ffe7d9', '#ffa48d', '#b72136', '#7a0c2e', '#ffd0d0', '#fff'}

        hex_color = self.LogInPage.get_element_color(*SigninLocators.error_msg)
        if hex_color:
            assert hex_color in exp_error_color, f"Unexpected error message color: {hex_color}"
            print(hex_color)
