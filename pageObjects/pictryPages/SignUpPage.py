import random
import re
import string
import time
import traceback
from datetime import datetime, timedelta
import allure
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import email_listener
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
import request
from locator.locators import SigninLocators, SubscriptionLocators, LoginLocators, HomeLocators
from base.BasePage import BasePage
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.SubscriptionPage import SubscriptionPage
from utilities.XlUtils import get_cell_data


class SignUpPage(BasePage):

    def __init__(self, driver):  # constructor of SignIn page class
        super().__init__(driver)
        self.scrollToclick_element(*SigninLocators.sign_link)
        self.SubscriptionPage = SubscriptionPage(self.driver)

    def get_SignUpPage_url(self, current_url):  # This is used to get SignIn Url of SignIn Page
        return self.get_url(current_url)

    def is_logo_exist(self):  # This is used to get Logo of login Page
        return self.is_visible(*SigninLocators.LOGO_VISIBLE)

    @staticmethod
    def get_Signup_credential(sheet_name, row):
        path = LogInPage.get_path_dev_test(LogInPage.env)  # Call the method to get the file path
        firstName = get_cell_data(path, sheet_name, row, 1)
        lastName = get_cell_data(path, sheet_name, row, 2)
        email = get_cell_data(path, sheet_name, row, 3)
        password = get_cell_data(path, sheet_name, row, 4)

        return firstName, lastName, email, password

    def is_tclink_exist(self):  # This is used to get Forgot password link of login Page
        return self.is_visible(*SigninLocators.Terms_and_condition_Link)

    def is_Loginlink_exist(self):  # This is used to get Forgot password link of login Page
        return self.is_visible(*SigninLocators.login_link)

    def get_element_scrollClick(self, by_locname, locator):
        try:
            if self.is_loader_invisible(*LoginLocators.loader):
                print("loader is Invisible")
                return self.scrollToclick_element(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def is_googletext_exist(self):  # This is used to get Continue with Google text of SignIn Page
        return self.is_visible(*SigninLocators.CONTINUE_WITH_GOOGLE_TEXT)

    def signUp_element_exist(self, by_locname, locator):
        if self.is_visible(by_locname, locator):
            return self.do_element(by_locname, locator)

    def get_SignUp_page_title(self, title):  # This is used to get SignIn Title of SignIn Page
        return self.get_title(title)

    def get_elements(self, by_locname, locator):  # This is used to get element On Subscription Page
        if self.is_visible(by_locname, locator):
            return self.get_webelement(by_locname, locator)

    def get_Ft_PlanStatus(self, by_locname, locator):
        element = self.do_element_DOM(by_locname, locator)
        if element:
            self.scrollToclick_element_DOM(by_locname, locator)
            elabfree = self.do_element(*SubscriptionLocators.elabmin)
            ft_user = self.do_element(*SubscriptionLocators.Ft_user)
            return elabfree, ft_user

    def get_ICP_country_upgrade_FreeTrial_ToPremium_Plan(self, by_locname, locator, val):
        self.get_element_scrollClick(*SubscriptionLocators.Professional_BuyNow_butn)
        self.scrollToclick_element_DOM(by_locname, locator)
        self.get_element_scrollClick(*SubscriptionLocators.Professional_BuyNow_butn)
        if self.is_visible(*SubscriptionLocators.elabs_plan_price):
            return self.SubscriptionPage.get_elabs_starter_price(*SubscriptionLocators.elabs_plan_price, val)

    def get_ICPCountry_biling_address_team_Plan(self, by_locname, locator):
        self.clickOperation(by_locname, locator)
        element_Invisible = self.is_loader_invisible(*LoginLocators.loader)
        if element_Invisible:
            self.add_ICP_country_billingaddress('adrs', 'Hyderabad', 123456)

    def get_upgrade_FreeTrial_ToPremium_Plan(self, by_locname, locator):
        self.get_element_scrollClick(*SubscriptionLocators.Professional_BuyNow_butn)
        self.scrollToclick_element_DOM(by_locname, locator)
        self.get_element_scrollClick(*SubscriptionLocators.Professional_BuyNow_butn)
        self.clickOperation(*SubscriptionLocators.Proceed_butn)

        element_Invisible = self.is_loader_invisible(*LoginLocators.loader)
        if element_Invisible:
            self.add_billingaddress('ad', 'Hyderabad', 123456)

    def get_subscription_purchase_authentication(self, by_locname, locator):
        iframe = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located((By.ID, "Cardinal-CCA-IFrame")))
        if iframe:
            self.driver.switch_to.frame(iframe)
            if self.is_visible(by_locname, locator):
                self.do_send_keys(by_locname, locator, "1234")
                if self.is_visible(*SubscriptionLocators.Submit):
                    self.scrollToclick_element(*SubscriptionLocators.Submit)
                    self.driver.switch_to.default_content()

    def is_StartyourFREEtrial_exist(self):  # This is used to get Start your FREE trial text of SignIn Page
        return self.is_visible(*SigninLocators.StartyourFREEtrial)

    def get_Startyour14dayfreetrial(self, by_locname, locator):
        return self.do_element(by_locname, locator)

    def get_card_detail(self, by_locname, locator):
        self.chargebee_card_container_frame()
        if self.is_visible(by_locname, locator):
            add_buton = self.do_element(by_locname, locator)
            if add_buton:
                self.is_clickable(by_locname, locator)
                Continue = self.do_element(*SigninLocators.Continue)
                if Continue:
                    self.scrollToclick_element(*SigninLocators.Continue)

    def do_clickOnquestionairePage(self):
        buton = self.do_element_DOM(*SigninLocators.buton)
        if buton:
            self.scrollToclick_element_DOM(*SigninLocators.buton)

    def get_elabs_professional_price(self, by_locname, locator):
        gety_Image, elabs_price, starter_plan_price = SignUpPage.get_Plan_price('Price', 11)

        if self.is_visible(by_locname, locator):
            actual_price = self.do_element(by_locname, locator)

            actual_price_text = actual_price.text
            number_substring = re.search(r'\d+', actual_price_text).group()

            actual_price_numeric = int(number_substring)
            return (elabs_price + gety_Image + starter_plan_price), actual_price_numeric

    def get_ProfessionalOrder_Sumary(self, by_locname, locator):
        if self.is_visible(by_locname, locator):
            elab = self.do_element(by_locname, locator)
            if elab.is_enabled():
                self.scrollToclick_element(by_locname, locator)
                # elVoice = self.do_element(*SubscriptionLocators.elVoice_plan)
                # if elVoice.is_enabled():
                if self.is_visible(*SubscriptionLocators.add_On):
                    try:
                        time.sleep(2)
                        self.is_clickable(*SubscriptionLocators.add_On)
                        return self.get_elabs_professional_price(*SubscriptionLocators.elabs_plan_price)

                    except StaleElementReferenceException:
                        return self.get_elabs_professional_price(*SubscriptionLocators.elabs_plan_price)

    def get_buy_elVoice_Over(self, by_locname, locator):
        if self.is_visible(*SubscriptionLocators.Proceed_butn_renew):
            self.is_clickable(*SubscriptionLocators.Proceed_butn_renew)
            self.scrollToclick_element_DOM(*SubscriptionLocators.Proceed_popup)
            element_visible = self.is_loader_invisible(*HomeLocators.loader)
            if element_visible:
                self.scrollToclick_element(*SubscriptionLocators.Payment_Ok)
                # self.scrollToclick_element(*SubscriptionLocators.Okay)

                element_visible1 = self.is_loader_invisible(*HomeLocators.loader)
                if element_visible1:
                    elabmin1 = self.do_element(by_locname, locator)
                    return elabmin1

    def get_next_biling_cycle(self, by_locname, locator):
        if self.is_visible(by_locname, locator):
            expiration_date_element = self.do_element(by_locname, locator)

            print(type(expiration_date_element))  # Print the type of the element
            actual_expiration_date = expiration_date_element.text

            expected_expiration_date = datetime.now() + timedelta(days=365)
            expected_date = expected_expiration_date.date()

            formatted_date = expected_date.strftime("%d %b %Y")

            return formatted_date, actual_expiration_date

    def get_startpictory(self, by_locname, locator):
        self.scrollToclick_element(by_locname, locator)

    def get_Verifypaymentmethod(self, by_locname, locator):  # This is used to get Upgrade link of Subscription Page
        return self.do_element(by_locname, locator)

    def add_ICP_country_billingaddress(self, Address, City,
                                       Zip):  # This is used to get Payment information detail On Subscription Page
        iframe = self.driver.find_element('xpath', "//*[@id='root']/iframe")
        self.driver.switch_to.frame(iframe)

        # self.scrollToclick_element(*SubscriptionLocators.button_payment)
        try:
            if self.is_visible(*SubscriptionLocators.Billing_Address):
                self.do_send_keys(*SubscriptionLocators.Billing_Address, Address)
                self.do_send_keys(*SubscriptionLocators.Billing_City, City)
                self.do_send_keys(*SubscriptionLocators.Billing_Zip, Zip)
                self.do_send_keys(*SubscriptionLocators.State_biling, "Andhra Pradesh")
                time.sleep(5)
                self.select_dropdown_ByvisibleText(*SubscriptionLocators.Billing_Country, "India")
                self.select_dropdown_ByvisibleText(*SubscriptionLocators.Billing_State, "Andhra Pradesh")
                self.is_clickable(*SubscriptionLocators.button_next)
                if self.is_visible(*SigninLocators.credit_card):
                    self.is_clickable(*SigninLocators.credit_card)
                    if self.is_visible(*SigninLocators.Card_Number):
                        self.ICP_country_cards_Page()
        except StaleElementReferenceException:
            print("exception handled")
            if self.is_visible(*SigninLocators.Card_Number):
                self.ICP_country_cards_Page()

    def ICP_country_cards_Page(self):  # This is used to get Payment information detail On Subscription Page
        # self.chargebee_card_container_frame()
        try:
            expiration_date = "12/26"  # Example: MM/YY
            month, year = expiration_date.split('/')

            self.do_send_keys(*SigninLocators.First, 'Automation')
            self.do_send_keys(*SigninLocators.Last, 'testing')
            time.sleep(2)
            self.do_send_keys(*SigninLocators.Card_Number, "4111111111111111")
            time.sleep(2)
            self.do_send_keys(*SigninLocators.Card_Number, Keys.ENTER)
            # self.driver.find_element(By.XPATH, '/html/body').click()

            self.do_send_keys(*SigninLocators.month_input, month)
            self.do_send_keys(*SigninLocators.year_input, year)
            self.do_send_keys(*SigninLocators.CVV_Cards, 123)

            next_butn = self.do_element(*SubscriptionLocators.next)
            if next_butn:
                self.is_clickable(*SubscriptionLocators.next)
                totalpay = self.do_element(*SigninLocators.totalpay)
                if totalpay:
                    self.is_clickable(*SigninLocators.totalpay)
                    # WebDriverWait(self.driver, 60).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='Cardinal-CCA-IFrame']")))

                    """
                    iframe = self.do_element(*SubscriptionLocators.otp_code)
                    if iframe:
                        self.driver.switch_to.frame(iframe)
                        code = self.do_element(*SubscriptionLocators.code)
                        if code:
                            # Use JavaScript to scroll to the code input field
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", code)
                            if self.is_visible(*SubscriptionLocators.code):
                                self.do_send_keys(*SubscriptionLocators.code, "1234")
                                if self.is_visible(*SubscriptionLocators.Submit):
                                    self.scrollToclick_element(*SubscriptionLocators.Submit)
                    
                    """

                    self.driver.switch_to.default_content()

        except StaleElementReferenceException:
            print("exception handled")
            totalpay = self.do_element(*SigninLocators.totalpay)
            if totalpay:
                self.is_clickable(*SigninLocators.totalpay)

                """
                iframe = WebDriverWait(self.driver, 120).until(
                    ec.visibility_of_element_located((By.XPATH, "//iframe[@id='Cardinal-CCA-IFrame']")))
                self.driver.switch_to.frame(iframe)
                code = self.do_element(*SubscriptionLocators.code)
                if code:
                    # Use JavaScript to scroll to the code input field
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", code)
                    if self.is_visible(*SubscriptionLocators.code):
                        self.do_send_keys(*SubscriptionLocators.code, "1234")
                        if self.is_visible(*SubscriptionLocators.Submit):
                            self.scrollToclick_element(*SubscriptionLocators.Submit)
                """

                self.driver.switch_to.default_content()

    def cards_Page(self, by_locname, locator):  # This is used to get Payment information detail On Subscription Page
        if self.is_visible(by_locname, locator):
            self.is_clickable(by_locname, locator)
            self.chargebee_card_container_frame()
        try:
            expiration_date = "12/26"  # Example: MM/YY
            month, year = expiration_date.split('/')

            if self.is_visible(*SigninLocators.First):
                self.do_send_keys(*SigninLocators.First, 'Automation')
                self.do_send_keys(*SigninLocators.Last, 'testing')
                time.sleep(2)
                self.do_send_keys(*SigninLocators.Card_Number, "4111111111111111")
                time.sleep(2)
                self.do_send_keys(*SigninLocators.Card_Number, Keys.ENTER)
                # self.driver.find_element(By.XPATH, '/html/body').click()

                self.do_send_keys(*SigninLocators.month_input, month)
                self.do_send_keys(*SigninLocators.year_input, year)
                self.do_send_keys(*SigninLocators.CVV_Cards, 123)

                add_buton = self.do_element(*SigninLocators.add_buton)
                if add_buton:
                    self.is_clickable(*SigninLocators.add_buton)
                    Continue = self.do_element(*SigninLocators.Continue)
                    if Continue:
                        self.scrollToclick_element(*SigninLocators.Continue)

        except NoSuchElementException:
            print("exception handled")

    def get_element(self, by_locname, locator):  # This is used to get element On Subscription Page
        if self.is_visible(by_locname, locator):
            return self.do_element(by_locname, locator)

    def ScrollviewOperation(self, by_locname, locator):  # This is used to perform scroll and click to button
        try:
            if self.is_visible(by_locname, locator):
                return self.scrollToview_element(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def get_verifyemail(self, by_locname, locator):  # This is used to get Upgrade link of Subscription Page
        if self.is_visible(by_locname, locator):
            return self.do_element(by_locname, locator)

    def is_continuebutton_exist(self):  # This is used to get click at continue button of SignIn Page
        return self.is_visible(*SigninLocators.cnt_bn)

    def ScrollclickOperation(self, by_locname, locator):  # This is used to perform scroll and click to button
        try:
            if self.is_visible(by_locname, locator):
                return self.scrollToclick_element(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def get_element_text(self, by_locname, locator):  # This is used to get element On Subscription Page
        if self.is_visible(by_locname, locator):
            return self.do_element_text(by_locname, locator)

    def get_SignPage_element(self, by_locname, locator):  # This is used to get element On Subscription Page
        return self.do_element(by_locname, locator)

    def clickOn_action_Perform(self, by_locname, locator):
        return self.do_action_scrollTo_Click(by_locname, locator)

    def clickOperation(self, by_locname, locator):  # This is used to perform click to button
        try:
            if self.is_visible(by_locname, locator):
                self.is_clickable(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def chargebee_card_container_frame(self):
        iframe = self.driver.find_element('xpath', "//iframe[contains(@class, 'chargebee-card-container')]")
        self.driver.switch_to.frame(iframe)

    def card_detail_Page(self, Card, expiry_Month, expiry_Year,
                         Cvv):  # This is used to get Payment information detail On Subscription Page

        try:
            self.is_visible(SigninLocators.Card_Number)
            self.do_send_keys(SigninLocators.Card_Number, Card)
            self.do_send_keys(SigninLocators.expiry_Month, expiry_Month)
            self.do_send_keys(SigninLocators.expiry_Year, expiry_Year)
            self.do_send_keys(SigninLocators.Cvv_Number, Cvv)

        except NoSuchElementException:
            print("exception handled")

    @staticmethod
    def get_Plan_price(sheet_name, row):
        path = LogInPage.get_path_dev_test(LogInPage.env)  # Call the method to get the file path
        gety_Image = get_cell_data(path, sheet_name, row, 1)
        elabs_price = get_cell_data(path, sheet_name, row, 2)
        plan_price = get_cell_data(path, sheet_name, row, 3)

        if gety_Image is not None and elabs_price is not None and plan_price is not None:
            return gety_Image, elabs_price, plan_price

    def autocard_suggest(self):
        search = self.driver.find_element(By.XPATH, "//*[starts-with(@id, 'number')]")
        search.clear()
        search.send_keys('4111 ')
        time.sleep(5)
        auto_complete = self.driver.find_elements(By.XPATH, "//div[starts-with(@class, 'cb-pmcard__details')]")
        auto_complete[0].click()

    def get_Page_Load(self):
        return self.do_element_Page_Load()

    def is_Alreadyregistered_exist(self):  # This is used to get Already registered ? text of SignIn Page
        return self.is_visible(*SigninLocators.Alreadyregistered)

    # Set your email, password, what folder you want to listen to, and where to save attachments
    @staticmethod
    def email_listen():
        emailtrigger = "pictoryautomate@gmail.com"
        app_password = "swnz ogvx wtyo wokf"
        folder = "Inbox"

        subject = "Welcome to Pictory!"  # Specify the subject you want to filter emails by

        polling_interval = 10  # Poll every 10 seconds
        max_polling_duration = 3600  # Maximum time to keep polling (in seconds), e.g., 1 hour

        start_time = time.time()

        # Initialize otp with a default value
        otp = None

        while time.time() - start_time < max_polling_duration:
            try:

                el = email_listener.EmailListener(emailtrigger, app_password, folder, "")
                el.login()
                messages = el.scrape()
                otp_pattern = r'\b\d{6}\b'

                print(f"type of messages: {type(messages)}")  # Debugging output
                for key, message in messages.items():
                    if subject in message['Subject']:
                        body = message['Plain_Text']  # Access the email body
                        otp_matches = re.findall(otp_pattern, body)
                        for otp in otp_matches:
                            return otp
                        break
            except Exception as e:
                print(f"Error: {e}")

            time.sleep(polling_interval)

        print("No OTP found.")  # Debugging output
        return None

    @allure.step("sign with email: '1'")
    def SignUpPictory(self, firstName, lastName, email, password):  # This is used to SignIn in Pictory app
        try:
            script = """
                // Set and trigger change for first name input
                var firstNameElement = document.querySelector('#firstNameField');
                var lastFirstNameValue = firstNameElement.value;
                firstNameElement.value = arguments[0];
                
                var firstNameTracker = firstNameElement._valueTracker;
                if (firstNameTracker) {
                    firstNameTracker.setValue(lastFirstNameValue);
                }
                var firstNameEvent = new Event('input', { bubbles: true });
                firstNameElement.dispatchEvent(firstNameEvent);
            
                // Set and trigger change for last name input
                var lastNameElement = document.querySelector('#lastNameField');
                var lastLastNameValue = lastNameElement.value;
                lastNameElement.value = arguments[1];
                
                var lastNameTracker = lastNameElement._valueTracker;
                if (lastNameTracker) {
                    lastNameTracker.setValue(lastLastNameValue);
                }
                var lastNameEvent = new Event('input', { bubbles: true });
                lastNameElement.dispatchEvent(lastNameEvent);
            
                // Set and trigger change for email input
                var emailElement = document.querySelector('#emailField');
                var lastEmailValue = emailElement.value;
                emailElement.value = arguments[2];
                
                var emailTracker = emailElement._valueTracker;
                if (emailTracker) {
                    emailTracker.setValue(lastEmailValue);
                }
                var emailEvent = new Event('input', { bubbles: true });
                emailElement.dispatchEvent(emailEvent);
            
                // Set and trigger change for password input
                var passElement = document.querySelector('#outlined-adornment-password');
                var lastPassValue = passElement.value;
                passElement.value = arguments[3];
                
                var passTracker = passElement._valueTracker;
                if (passTracker) {
                    passTracker.setValue(lastPassValue);
                }
                var passInputEvent = new Event('input', { bubbles: true });
                passElement.dispatchEvent(passInputEvent);
            """

            self.driver.execute_script(script, firstName, lastName, email, password)

            """
            self.do_send_keys(*SigninLocators.f_Name, firstName)
            self.do_send_keys(*SigninLocators.l_Name, lastName)
            self.do_send_keys(*SigninLocators.email_field, email)
            self.do_send_keys(*SigninLocators.password_field, password)
            
            """
            self.is_continuebutton_exist()
            self.is_clickable(*SigninLocators.cnt_bn)
            time.sleep(4)
            # self.driver.find_element(*SigninLocators.password).send_keys(password, Keys.ENTER)

        except StaleElementReferenceException:
            print(traceback.format_exc())

    @staticmethod
    def random_generator(size=4,
                         chars=string.ascii_lowercase + string.digits):  # This is used to get random mail of SignIn Page
        return ''.join(random.choice(chars) for x in range(size))
