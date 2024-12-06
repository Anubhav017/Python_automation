from selenium.webdriver.common.by import By
import json

class_name = {
    'root': 'MuiTypography-root',
    'badge': 'MuiBadge-root',
    'body2': 'MuiTypography-body2',  # Added comma here
    'root_avatar': 'MuiAvatar-root',
    'avatar': 'MuiAvatar-circular',
    'def_avatar': 'MuiAvatar-colorDefault',
    'body1': 'MuiTypography-body1',  # Added comma here
    'text': 'MuiTypography-text_sm'
}

locator_xpath = By.XPATH
locator_Id = By.ID
locator_Css = By.CSS_SELECTOR

# Load the configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

dev_url = config['environments']['dev']['dev_url']


class LoginLocators:
    email_field = (f"{locator_xpath}", "//*[@id='mui-1']")
    password_field = (f"{locator_Id}", "outlined-adornment-password")
    login_bn = (f"{locator_xpath}", "//button[normalize-space()='Login']")

    login_Loader = (f"{locator_xpath}", "//div[@class='dot-flashing']")
    Email_field_Required = (f"{locator_xpath}", "//*[@id='mui-1-helper-text']")
    # loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")

    LOGIN_PAGE_URL = {
        "dev": f'{dev_url}/login',
        "staging": f'{dev_url}/login',
        "prod": f'{dev_url}/login',
        # Add more environments if needed
    }

    invalid_data_msg = (f"{locator_xpath}", "//span[contains(text() , 'Invalid username or password' )]")
    LOGIN_PAGE_TITLE = "Pictory.AI - Home of AI Video Editing Technology"
    HOME_Page_URL = f"{dev_url}/textinput"

    DEV_TC_PAGE_URL = "https://pictory.ai/terms-of-service"
    STAGING_TC_PAGE_URL = "https://pictory.ai/terms-of-service"
    PROD_TC_PAGE_URL = "https://pictory.ai/terms-of-service"

    sign_next = (By.LINK_TEXT, "Sign up")
    Gmail_Field = By.ID, "identifierId"
    Next = (f"{locator_xpath}", "//span[@jsname='V67aGc' and contains(text(), 'Next')]")
    Gmail_password = (f"{locator_xpath}", '//*[@name="Passwd"]')
    Next1 = (f"{locator_xpath}", "//span[@jsname='V67aGc' and contains(text(), 'Next')]")
    google_Continue = (f"{locator_xpath}", "//p[contains(text() , 'Continue with Google' )]")
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    Forgot_Link = f"{locator_xpath}", "//a[contains(text(), 'Forgot password?')]"
    Terms_and_condition_Link = f"{locator_xpath}", "//a[text()='Terms and Conditions']"
    Project = f"{locator_xpath}", "//span[text()='My projects']"
    # repurpose_homepage = f"{locator_xpath}", "//span[text()='Which content would you like to repurpose into videos?']"
    repurpose_homepage = f"{locator_xpath}", f"(//span[contains(@class, '{class_name.get('root')}')])[11]"

    Verifypaymentmethod = (f"{locator_xpath}", "//button[normalize-space() = 'Verify payment method']")
    Continue = (f"{locator_xpath}", "//div[text()='Continue →']")
    send = (f"{locator_xpath}", "//span[text()='resend']")
    login_hover_Profile = (f"{locator_Css}", f"div.MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault")
    logout_bn = (f"{locator_xpath}", "//span[text() = 'Log out']")


class SigninLocators:
    SIGNIN_PAGE_URL = {
        "dev": f'{dev_url}/signup',
        "staging": f'{dev_url}/signup',
        "prod": f'{dev_url}/signup',
        # Add more environments if needed
    }

    sign_link = By.LINK_TEXT, "Sign up"
    SIGNIN_PAGE_TITLE = "Pictory.AI - Home of AI Video Editing Technology"
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    error_msg = (f"{locator_xpath}", f"(//span[contains(@class, '{class_name.get('root')}')])[3]")

    eyeInvisible = (f"{locator_xpath}", "//button[@aria-label='toggle password visibility']//*[name()='svg']")

    sign_next = (By.LINK_TEXT, "Sign up")
    f_Name = (By.ID, 'mui-2')
    l_Name = (By.ID, 'mui-3')
    email_field = (By.ID, 'mui-4')
    login_link = By.LINK_TEXT, "Login"
    password_field = (By.ID, "outlined-adornment-password")
    cnt_bn = (f"{locator_xpath}", "//button[text()='Continue']")
    invalid_data_msg = (f"{locator_xpath}", "//div[@class='css-13gdvgk']")
    CONTINUE_WITH_GOOGLE_TEXT = (f"{locator_xpath}", "//P[text()='Continue with Google']")
    StartyourFREEtrial = (f"{locator_xpath}", "//span[text()='Start your FREE trial']")
    Alreadyregistered = (f"{locator_xpath}", "//span[text()='Already registered?']")
    Startyour14dayfreetrial = f"{locator_xpath}", f"//span[contains(@class, '{class_name.get('root')}')][1]"
    Verifypaymentmethod = f"{locator_Css}", "button.MuiButton-containedPrimary"
    VerifyEmail = f"{locator_Css}", f"span.{class_name.get('root')}.MuiTypography-h3_resp"

    Addapaymentmethod = By.ID, "cb-header-title"
    creditcard = f"{locator_xpath}", "//span[text()= 'Credit card']"

    totalpay = (f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Pay')]")

    # cards
    First = (By.ID, 'first_name')
    Last = (By.ID, 'last_name')
    Card_Number = (By.ID, 'number')
    month_input = (By.ID, 'exp_month')
    year_input = (By.ID, 'exp_year')
    CVV_Cards = (By.ID, 'cvv')

    Terms_and_condition_Link = f"{locator_xpath}", "//a[text()='Terms and Conditions']"

    SIGNUP_Verify = {
        "dev": f'{dev_url}/questionnaire',
        "staging": f'{dev_url}/questionnaire',
        "prod": f'{dev_url}/questionnaire',
        # Add more environments if needed
    }

    HOME_Page_URL = {
        "dev": f'{dev_url}/textinput',
        "staging": f'{dev_url}/textinput',
        "prod": f'{dev_url}/textinput',
        # Add more environments if needed
    }

    # credit card field
    cardtext = f"{locator_xpath}", "//label[text()=' Card Number']"
    expiry = f"{locator_xpath}", "//label[normalize-space() ='Expiry']"
    CVV = f"{locator_xpath}", "//label[normalize-space() ='CVV']"
    add_buton = f"{locator_xpath}", "//button[normalize-space() = 'Add']"

    CVVfield = (By.ID, "cvv")

    # paypal

    paypal = f"{locator_xpath}", "//span[text() ='PayPal']"

    # card info field
    Card_Numbers = (By.ID, "number")
    expiry_Month = (By.ID, "exp_month")
    expiry_Year = (By.ID, "exp_year")
    Country = (By.NAME, "country")
    Cvv_Number = (By.ID, "cvv")

    Continue = (f"{locator_xpath}", "//div[text()='Continue →']")
    # Personal_use = (f"{locator_xpath}", "//span[(text() = 'Other')]/following::input[@type='radio'][@value='top']")
    Purpose_test = (By.ID, "mui-11")
    Personal_use = (f"{locator_xpath}", "//span[normalize-space()='For personal use']")
    buton = (
        f"{locator_xpath}",
        "//div[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiListItemButton-root')][1]")
    startpictory = (f"{locator_xpath}", "//button[text()='Start using Pictory']")
    close = (f"{locator_xpath}", "//a[@role='button' and @aria-label='Close modal']")


class SubscriptionLocators:
    Subscription_PAGE_URL = {
        "dev": f'{dev_url}/plans',
        "staging": f'{dev_url}/plans',
        "prod": f'{dev_url}/plans',
        # Add more environments if needed
    }

    Subscription_PAGE_TITLE = "Pictory.AI - Home of AI Video Editing Technology"
    free_trial_text_Upgrade = (f"{locator_xpath}", "// *[ @class ='my-subscription-name']")
    login_bn1 = (f"{locator_xpath}", "//button[contains(text(), 'Login')]")

    renew = (f"{locator_xpath}",
             "//button[contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-textPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-textSizeMedium') and contains(@class, 'upgrade-button') and contains(@class, 'button') and contains(text(), 'Buy now')]")
    status = (f"{locator_xpath}", "//h5[text()  = 'Active']")
    email_field = (f"{locator_xpath}", "//*[@id= 'mui-1']")
    password_field = (By.ID, "outlined-adornment-password")
    Subscription_Upgrade_butn = (f"{locator_xpath}", "//button[normalize-space()='Upgrade']")
    SubPlan = (f"{locator_xpath}", "//h5[contains(text(), 'Subscription Plan')]")
    Professional_Plan = (f"{locator_xpath}", "//span[contains(text(), 'Professional')]")
    Upgrade_butn = (f"{locator_xpath}", "(//button[normalize-space()='Upgrade'])[2]")
    Starter_Plan = (f"{locator_xpath}", "//span[contains(text(), 'Starter')]")
    otp_code = (f"{locator_xpath}", "//iframe[@id='Cardinal-CCA-IFrame']")
    code = (f"{locator_xpath}", "//input[@name='challengeDataEntry']")
    Submit = (By.XPATH, "//input[@type='submit' and @value='SUBMIT']")

    # BuyNow_butn = (f"{locator_xpath}", "//button[contains(text(), 'Buy now')]")
    Starter_BuyNow_butn = (f"{locator_xpath}",
                           "(//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-text') and contains(@class, 'MuiButton-textPrimary') and contains(text(), 'Buy Now')])[1]")
    Proceed_butn = (f"{locator_xpath}",
                    "(//button[contains(@class, 'MuiButton-contained')])[4]")
    Proceed_butn_monthly = (f"{locator_xpath}",
                            "(//button[contains(@class, 'MuiButton-contained')])[5]")

    Proceed_butn_renew = (f"{locator_xpath}",
                          "(//button[contains(@class, 'MuiButton-contained')])[3]")

    Proceed_popup = (f"{locator_xpath}", "(//button[contains(text(), 'Proceed')])[2]")
    teamProceed_popup = (f"{locator_xpath}", "(//button[contains(text(), 'Proceed')])[1]")

    button_payment = (
        f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Proceed To Checkout')]")
    button_next = (f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Next')]")

    # Success_link = (f"{locator_xpath}", "//a[text()='Success']")
    Success_link = (f"{locator_Css}",
                    "#subscribe-container > form > div.row.css-2xzqzv > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div > div.d-flex.align-items-center.flex-wrap.mb-4 > div > a:nth-child(1)")

    Card_Numbers = (f"{locator_Css}", "input[placeholder='Card Number*']")
    expiry_Month = (f"{locator_xpath}",
                    "/html/body/div/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/select")
    expiry_Year = (f"{locator_xpath}",
                   "/html/body/div/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/select")
    payment = (f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Pay')]")

    # ok_buton = (f"{locator_xpath}", "(//button[contains(@class, 'MuiButton-containedPrimary') and @type='button'])[2]")

    Country = (By.NAME, "country")
    Cvv_Number = (f"{locator_Css}", "input[placeholder='CVV*']")
    State = (f"{locator_Css}", "input[placeholder='State*']")
    Zip_Code = (f"{locator_Css}", "input[placeholder='Zip*']")
    payment_text = (f"{locator_xpath}", "// label[text() = 'Payment Information']")

    subscribe_butn = (f"{locator_xpath}", "//span[text() = 'Subscribe']")
    Paymentsuccessful = (f"{locator_xpath}", "//span[text() = 'Payment successful']")

    Pictory_logo = (f"{locator_xpath}", "//img[contains(@alt, 'Pictory')]")
    Payment_Ok = (f"{locator_xpath}", "//button[text()='OK']")
    Okay = (f"{locator_xpath}", "//button[text()='Okay']")

    signUp_Next = (By.LINK_TEXT, "Sign up")
    hover_Profile = (
        f"{locator_Css}",
        f"div.{class_name.get('root_avatar')}.{class_name.get('avatar')}.{class_name.get('def_avatar')}")

    dropdown = (f"{locator_xpath}", "//div[contains(@class, 'MuiSelect-select')]")
    member_Upgrade = (f"{locator_xpath}", "(//span[contains(text(), 'Team members')])[5]")
    Current_status = (f"{locator_xpath}",
                      "//span[contains(@class, 'MuiChip-label') and contains(@class, 'MuiChip-labelSmall') and text()='Current']")
    My_Subscription = (f"{locator_xpath}", "//span[text() = 'My subscription']")
    Plan_confirmation = (f"{locator_xpath}", "//button[text() = 'Yes, switch']")
    Thank_you = (f"{locator_xpath}", "//span[contains(text(), 'Thank you!')]")

    Professional_starter_downgrade_plan = (By.XPATH,
                                           "//p[(contains(text(), 'Your Professional Annual plan will downgrade to Starter Monthly on') or "
                                           "contains(text(), 'Your Starter Annual plan will downgrade to Starter Monthly on') or "
                                           "contains(text(), 'Your Professional Annual plan will downgrade to Professional Monthly on')) and contains(text(), 'of')]")

    team_downgrade_plan = (f"{locator_xpath}",
                           "//p[contains(text(), 'Your Teams Annual plan will downgrade to Teams Monthly on') and contains(text(), 'of')]")
    Monthly_Premium = (f"{locator_xpath}", "(//button[text() = 'Monthly'])[1]")
    Premium_BuyNow_butn = (f"{locator_xpath}",
                           "(//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-text') and contains(@class, 'MuiButton-textPrimary') and contains(text(), 'Buy Now')])[2]")
    Professional_BuyNow_butn = (f"{locator_xpath}",
                                "(//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-text') and contains(@class, 'MuiButton-textPrimary') and contains(text(), 'Buy Now')])[2]")
    See_allfeatures = (f"{locator_xpath}", "//a[text()='See all features']")

    status_elevenLab = (f"{locator_xpath}", "(//h5[contains(@class, 'vertical-point-value') and text()='Disabled'])[1]")
    status_Gety = (f"{locator_xpath}", "(//h5[contains(@class, 'vertical-point-value') and text()='Disabled'])[2]")

    all_Plan = (f"{locator_xpath}", "//span[text()='All plans include']")
    Videosfromscriptsblogs = (f"{locator_xpath}", "//span[text()='Convert scripts, blogs, and web pages to video']")
    Automatic_transcription = (f"{locator_xpath}", "//span[text()='Automatically transcribe and caption videos']")
    ConversationalAIVoice = (f"{locator_xpath}", "//span[text()='Generate conversational AI voiceover']")
    editVideo = (f"{locator_xpath}", "//span[text()='Edit video recordings with text and create highlights']")
    Fullaccess = (f"{locator_xpath}", "//span[text()='Access millions of stock videos and images']")
    repurpose = (f"{locator_xpath}", "//span[text()='Repurpose video for multiple platforms at 1080p']")

    Compareplan = (f"{locator_xpath}", "//h3[contains(text(),'Compare Plans')]")
    Createvideosfromscriptsblogs = (f"{locator_xpath}", "//th[text()='Generate Video from Script or URL']")
    Edityourexistingvideoswithvoice = (f"{locator_xpath}", "//th[text()='Edit Videos Using Text ']")
    Branding = (f"{locator_xpath}", "//th[text()='Branding']")
    Media = (f"{locator_xpath}", "//th[text()='Media']")
    Voiceover = (f"{locator_xpath}", "//th[text()='Voiceover']")
    Videoexportoption = (f"{locator_xpath}", "//th[text()='Video export options']")
    Customer = (f"{locator_xpath}", "//th[text()='Customer support']")

    Premium_BuyNow_Upgrade = (f"{locator_xpath}",
                              "(//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-text') and contains(@class, 'MuiButton-textPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-textSizeMedium') and contains(@class, 'upgrade-button') and contains(@class, 'button')])[2]")
    # Billing address
    Billing_Country = (By.ID, "country")
    Billing_City = (By.ID, "city")
    State_biling = (By.ID, "state")
    Billing_State = (By.ID, "state_code")
    Billing_Zip = (By.ID, "zip")
    Billing_Address = (By.ID, "line1")

    # Gety image and eleven Lab VO
    modify_elVoice = (f"{locator_xpath}", "//button[contains(text(), 'Modify')]")
    elabmin = (f"{locator_xpath}", "(//h5[@class = 'vertical-point-value'])[7]")
    elVoice_plan = (f"{locator_xpath}", "//button[contains(text(), 'Upgrade Add-on')]")
    add_On = (f"{locator_xpath}", "//button[contains(text(), 'Buy Add-on')]")
    addOn_buton = (f"{locator_xpath}", "(//button[contains(text(), 'Buy Add-on')])[2]")

    Ft_user = (f"{locator_xpath}", "//h5[contains(@class, 'my-subscription-name') and text() = 'Free Trial']")
    elabs_plan_price = (
        f"{locator_xpath}", "(//span[contains(@class, 'MuiTypography-text_lg') and contains(text(), '$')])[2]")
    Manage_Subscription = (f"{locator_xpath}", "//span[text() = 'Manage subscription']")

    # Gety image and eleven Lab VO
    buy_gety = (f"{locator_xpath}", "//span[contains(text(), 'Buy Add-on')]")
    Gety_enable = (f"{locator_xpath}", "(//h5[contains(@class, 'vertical-point-value') and text()='Enabled'])[1]")
    remove_addOn_butn = (f"{locator_xpath}", "//button[normalize-space()='Remove add-on']")
    next = f"{locator_xpath}", "//span[normalize-space() = 'Next']"
    remove_addOn = (f"{locator_xpath}",
                    "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-text_sm') and contains(text(), 'Remove Add-on')]")
    removegety = (f"{locator_xpath}",
                  "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-text_2xl') and contains(@class, 'MuiTypography-text_2xl') and contains(text(), 'Thank you')]")
    Subscribe_plan_Pay = (f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Pay')]")
    # Subscribe_plan_S = (f"{locator_Css}", "span.cb-button__text")
    Subscribe_plan = (
        f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Subscribe')]")

    nextbilcycle = (f"{locator_xpath}", "(//h5[@class = 'vertical-point-value'])[2]")


class AccountLocators:
    Account_Page_URL = {
        "dev": f'{dev_url}/account-settings',
        "staging": f'{dev_url}/account-settings',
        "prod": f'{dev_url}/account-settings',
        # Add more environments if needed
    }

    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@class='css-0']")
    Continue = (f"{locator_xpath}", "//div[text()='Continue →']")

    Account_Page_TITLE = "Pictory.AI - Home of AI Video Editing Technology"

    HOME_Page_URL = {
        "dev": f'{dev_url}/textinput',
        "staging": f'{dev_url}/textinput',
        "prod": f'{dev_url}/textinput',
        # Add more environments if needed
    }

    Payment_URL = {
        "dev": f'{dev_url}/payment',
        "staging": f'{dev_url}/payment',
        "prod": f'{dev_url}/payment',
        # Add more environments if needed
    }

    hover_Profile = (f"{locator_Css}", f"div.MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault")
    My_account = (f"{locator_xpath}", "//span[text() = 'My account']")
    sign_next = (By.LINK_TEXT, "Sign up")
    Upload_Picture = (f"{locator_xpath}", "//a[text() = 'Upload Picture']")

    # profile page
    Full_Name = (f"{locator_xpath}", "//label[text() = 'Full name']")
    Email = (f"{locator_xpath}", "//label[text() = 'Email']")
    Phone = (f"{locator_xpath}", "//label[text() = 'Phone']")
    comapny_Name = (f"{locator_xpath}", "//label[text() = 'Company name']")
    Country = (f"{locator_xpath}", "//label[text() = 'Country']")
    Country_dropdown = (By.ID, "mui-component-select-country")
    Name_country = (f"{locator_xpath}", "//li[@data-value='India']")
    India = (f"{locator_xpath}", "//div[@id='mui-component-select-country' and text() = 'India']")

    save_Butn = (f"{locator_xpath}", "//button[normalize-space()='Save']")

    click_country = (By.ID, "mui-component-select-country")
    Mobile = (By.NAME, "phone")
    country = "Austria"
    select_Country = (f"{locator_xpath}", f"//*[contains(text(),'{country}')]")

    # billing
    change_PW = (f"{locator_xpath}", "//h3[normalize-space() = 'Change password']")
    checkbox_PW = (f"{locator_xpath}", "//input[@type='checkbox']")
    current_password = (f"{locator_xpath}", "//input[@name='oldPassword']")
    new_password = (f"{locator_xpath}", "//input[@name='newPassword']")
    confirm_password = (f"{locator_xpath}", "//input[@name='rePass']")

    edit_card = f"{locator_xpath}", "//button[text() = 'Edit card']"

    Subscription_PAGE_URL = f'{dev_url}/plans'
    Billing = (f"{locator_xpath}", "//button[text()='Billing']")
    Subscription_plan = (f"{locator_xpath}", "//span[text()='Subscription plan']")
    Free_Trial = (f"{locator_xpath}", "//p[text()='Free Trial']")
    Upgrade_butn = (f"{locator_xpath}", "//button[text()='Upgrade']")
    cancel = (f"{locator_xpath}", "//button[text()='Cancel']")
    current = (f"{locator_xpath}", "//button[text()='No current need']")
    missing = (f"{locator_xpath}", "//button[text()='Missing feature']")
    TooExpensive = (f"{locator_xpath}", "//button[text()='Too expensive']")
    TooComplex = (f"{locator_xpath}", "//button[text()='Too complex']")
    Other = (f"{locator_xpath}", "//button[text()='Other']")
    cancel_Plan = (f"{locator_xpath}", "//button[text()='Still, go ahead and cancel']")
    Cancel_subscription = (f"{locator_xpath}", "//button[text()='Cancel subscription']")
    pause = (f"{locator_xpath}", "//button[contains(text(), 'Pause my subscription')]")
    # loader = (f"{locator_xpath}", "//span[@role='progressbar']//*[name()='svg']")
    status_cancel = (f"{locator_xpath}", "//h5[contains(@class, 'vertical-point-value') and text()='Canceled']")
    loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")

    # Card details
    Card_detail = (f"{locator_xpath}", "//span[text()='Card details']")
    Card_number = (f"{locator_xpath}", "//label[text()='Credit card number']")
    Exp_date = (f"{locator_xpath}", "//label[text()='Exp date']")
    CVV = (f"{locator_xpath}", "//label[text()='CVV']")

    Invoice = (f"{locator_xpath}", "//h3[text()='Invoice email ID']")
    google_Continue = (f"{locator_xpath}", "//p[contains(text() , 'Continue with Google' )]")


class HomeLocators:
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    HOME_Page_TITLE = "Pictory.AI - Home of AI Video Editing Technology"
    HOME_Page_URL = f"{dev_url}/textinput"
    # WatchTutorial_Link = (f"{locator_xpath}", "//a[contains(text(), 'Watch tutorial')]")
    Project = (f"{locator_xpath}", "//span[text()='My projects']")

    loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    help = (f"{locator_xpath}", "//span[text()='Help']")
    hover_Profile = (f"{locator_Css}", f"div.MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault")
    My_account = (f"{locator_xpath}", "//span[text() = 'My account']")
    My_Subscription = (f"{locator_xpath}", "//span[text() = 'My subscription']")
    becomeAffiliate = (f"{locator_xpath}", "//span[text() = 'Become affiliate']")
    logout = (f"{locator_xpath}", "//span[text() = 'Log out']")

    ScriptToVideo = (f"{locator_xpath}", "//span[text()='Script ']")
    ArticleToVideo = (f"{locator_xpath}", "//span[text()='Article ']")
    editVideo = (f"{locator_xpath}", "//span[text()='Edit Video ']")
    VisualToVideo = (f"{locator_xpath}", "//span[text()='Visuals']")

    profileName = (f"{locator_xpath}", "//span[text()='Hello, ']")
    Affiliate = (f"{locator_xpath}", "//button[text()='Become an affiliate today']")


class ScriptToVideoLocators:
    Proceed_buton = (
        f"{locator_xpath}",
        "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'script-to-video-button')]")
    name = (f"{locator_Css}", "input[placeholder='Enter your video name']")
    content = (f"{locator_Css}", "p[data-placeholder='Start typing here, or paste your script using ctrl+v']")
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    Proceed_generate = (f"{locator_xpath}", "//button[text() = 'Proceed']")
    Project = (f"{locator_xpath}", "//span[text()='My projects']")
    template = (By.ID, "template_614b1f33-0ef1-4396-bbb0-615f47333cf2")
    template_width = (f"{locator_xpath}", "//div[@class = 'aspect-ratio-card  MuiBox-root css-0']")
    saved_Video = (f"{locator_xpath}", "//span[text()='AI in health domain']")
    # Arrow = (f"{locator_xpath}", "//*[@id='Icon-Arrow-Down']")
    Arrow = (By.ID, "Icon-Arrow-Down")
    voice_successful = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('body2')}')]")
    voice_applied = (f"{locator_xpath}",
                     f"//a[@id='voiceTrack1010']//span[contains(@class,'{class_name.get('root')}')][normalize-space()='Applied']")

    editor = (
        f"{locator_xpath}", "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-h4b')]")
    complete = (f"{locator_xpath}", "//h6[@class='increasing-txt']")
    ai_evolution_script = {
        "introduction": "Explore the fascinating journey of Artificial Intelligence, from its inception to present breakthroughs, showcasing its transformative impact on industries and daily life.",
        "healthcare_impact": "Delve into the evolving role of AI in healthcare, revolutionizing diagnostics, treatment plans, and reshaping the future of medical practices.",
        "business_transformation": "Uncover how AI drives business innovation, enhancing productivity, decision-making, and customer experiences, leading to a paradigm shift in corporate landscapes.",
        "ethical_considerations": "Examine the ethical dimensions of AI evolution, addressing concerns, and emphasizing responsible AI development to ensure a positive and inclusive technological future.",
        "education_revolution": "Discover how AI is transforming education, personalizing learning experiences, and making education more accessible worldwide.",
        "transportation_advancements": "Understand the impact of AI on transportation, from autonomous vehicles to smarter traffic management systems, and its role in improving safety and efficiency.",
        "environmental_sustainability": "Learn about the contributions of AI to environmental sustainability, helping to combat climate change and optimize resource use.",
        "entertainment_innovation": "Explore how AI is revolutionizing the entertainment industry, from content creation to personalized recommendations, enhancing user experiences.",
        "cybersecurity_measures": "Investigate the role of AI in cybersecurity, protecting data and infrastructure from threats, and its importance in maintaining digital security.",
        "future_prospects": "Reflect on the future prospects of AI, potential advancements, and the ongoing challenges that need to be addressed for its safe and ethical development."
    }

    WaterMarks = (f"{locator_xpath}", "//button[text()='Got it']")
    Download = (f"{locator_xpath}", "//a[text() = 'Download']")
    highlight_scripteditor = (f"{locator_xpath}", "//button[text()='Highlight']")
    bold = (f"{locator_xpath}", "//strong")
    clip_Board = (f"{locator_xpath}", "//button[contains(text(), 'Paste from clipboard')]")
    char_len = (f"{locator_xpath}", "(//span[contains(@class, 'MuiTypography-subtitle2b_resp')])[4]")

    # Voiceover
    apply_butn = (f"{locator_xpath}", "//a[@id='voiceTrack1010']//span[contains(@class,'')][normalize-space()='Apply']")
    Voice = (
        f"{locator_xpath}", "//span[contains(@class, 'MuiTypography-root MuiTypography-text_sm track-hd')]")
    voice_search = (f"{locator_xpath}", "//input[@placeholder='Search voices']")

    progress = (f"{locator_xpath}", "//div[@id='dynamic']")
    premiumapply_butn = (
        f"{locator_xpath}", "//a[@id='voiceTrack3023']//span[contains(@class,'')][normalize-space()='Apply']")
    premiumvoice_applied = (f"{locator_xpath}",
                            f"//a[@id='voiceTrack3023']//span[contains(@class,'{class_name.get('root')}')][normalize-space()='Applied']")

    Copypreview_link = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')} {class_name.get('body1')}') and contains(text(), 'Copy preview link')]")
    close = (By.ID, "closeIcon")

    saved = (f"{locator_xpath}", f"//p[contains(@class, '{class_name.get('root')}') and contains(text(), 'Saved')]")
    Recent_Projects = (f"{locator_xpath}", "//span[contains(text() , 'ScriptToVideo')]")
    Voiceover = (f"{locator_xpath}", "//button[contains(text(),'Voiceover')]")

    Story = f"{locator_xpath}", "//h4[text() = 'Story']"
    Visual = f"{locator_xpath}", "//h4[text() = 'Visuals']"
    Audio = f"{locator_xpath}", "//h4[text() = 'Audio']"
    Text = f"{locator_xpath}", "//h4[text() = 'Text']"
    element = f"{locator_xpath}", "//h4[text() = 'Elements']"
    Styles = f"{locator_xpath}", "//h4[text() = 'Styles']"
    branding = f"{locator_xpath}", "//h4[text() = 'Branding']"
    format = f"{locator_xpath}", "//h4[text() = 'Format']"
    previous = By.ID, "previous_button"

    preview = (f"{locator_xpath}", "//a[@id='btnPreview']")
    Download_element = f"{locator_xpath}", "//a[text() = 'Download']"
    Scene_Duration = f"{locator_xpath}", "//span[text() = 'Scene duration:']"
    Video_Duration = f"{locator_xpath}", "//span[text() = 'Video duration:']"
    Intro = By.ID, "SceneNumberId_1_1"
    Outro = By.ID, "SceneNumberId_5_1"
    right_scroll_click = f"{locator_Css}", "button.slide-btn.scroll-rightbtn[fdprocessedid='38l60j']"

    auto_visual = (f"{locator_xpath}",
                   "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'centered-in-container') and contains(@class, 'background-layer')]")
    background = (f"{locator_xpath}", "//button[normalize-space()='Run in background']")
    Video_Generation = (f"{locator_xpath}",
                        "//div[@role='alert' and contains(@class, 'Toastify__toast-body') and text()='Video Generation is completed']")
    Video_Generation_Progress = (f"{locator_xpath}",
                                 "//div[@role='alert' and @class='Toastify__toast-body' and text()='Video generation is in progress']")
    curentPlan = (
        f"{locator_Css}", "button.MuiButton-outlined.MuiButton-outlinedPrimary.MuiButton-sizeMedium[disabled]")

    Video_Generationprogress = (f"{locator_xpath}",
                                "//p[contains(@class, 'MuiTypography-body1') and contains(@class, 'font-size-4') and contains(@class, 'grey') and contains(@class, 'mt-0') and contains(@class, 'mb-0') and contains(@class, 'css-117rfk8') and contains(text(), 'Generating video.')]")

    # Layer
    addLayer = (f"{locator_xpath}", "(//span[@aria-label='Add as layer'])[2]")
    video = (f"{locator_xpath}", "(//button[contains(@class, 'MuiButton-root')])[3]")
    automate_buton = (
        f"{locator_xpath}", "//button[@class='btn btn-outline-secondary btn-sm' and contains(text(), 'ethical')]")
    opacitycircular = (
        f"{locator_xpath}", "//span[contains(@class, 'MuiSlider-thumb') and contains(@style, 'left: 100%')]")
    DuplicateLayer = (f"{locator_xpath}",
                      "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'MuiIconButton-colorGrey') and contains(@class, 'MuiIconButton-sizeSmall') and @aria-label='Duplicate']")
    DeleteLayer = (f"{locator_xpath}",
                   "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'MuiIconButton-sizeSmall') and @aria-label='Delete']")
    copyScene = (f"{locator_xpath}",
                 "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'MuiIconButton-sizeSmall') and @aria-label='Copy to all scenes']")

    video_generate = (f"{locator_xpath}", "(//h5[@class = 'vertical-point-value'])[3]")
    Plan_card = (By.CLASS_NAME, "vertical-point MuiBox-root css-0")


class MyProjectLocators:
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    MyProject_Page_TITLE = "Pictory.AI - Home of AI Video Editing Technology"

    MyProject_Page_URL = {
        "dev": f'{dev_url}/myvideos',
        "staging": f'{dev_url}/myvideos',
        "prod": f'{dev_url}/myvideos',
        # Add more environments if needed
    }

    Myproject_loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    # video_Delete = (f"{locator_Css}", "div[aria-label='Delete'] svg[data-testid='DeleteOutlinedIcon']")
    video_Delete = (
        f"{locator_Css}", "svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.hover-bg-black-10.css-109jpo8-MuiSvgIcon-root")

    video_Duplicate = (f"{locator_Css}", "div[aria-label='Duplicate'] svg[data-testid='ContentCopyOutlinedIcon']")
    help = (f"{locator_xpath}", "//span[text()='Help']")
    Search = (f"{locator_Css}", "input[placeholder='Search by name']")
    Delete = (f"{locator_xpath}", "//button[text()='Delete']")
    MyProject = f"{locator_xpath}", "//span[text()='My projects']"
    createProject = f"{locator_xpath}", "//button[text() = 'Create project']"

    branding_select = (f"{locator_xpath}",
                       "//span[contains(@class,'MuiTypography-root MuiTypography-text_sm')][normalize-space()='brand_template']")
    createfolder = f"{locator_xpath}", "//button[text() = 'Create folder']"
    folder_name = (f"{locator_Css}", "input[placeholder='Type here...']")
    video_MoveTo = (f"{locator_Css}", "svg[data-testid='DriveFileMoveOutlinedIcon']")
    createbtn = f"{locator_xpath}", "//button[text() = 'Create']"
    Import_location = f"{locator_xpath}", "//button[text() = 'Import projects']"


class ArticleToVideoLocators:
    Proceed_buton = (f"{locator_Css}", "button.MuiButton-containedPrimary[value='Proceed']")
    article = (By.ID, "txtURL")
    Recent_Projects = (
        f"{locator_xpath}",
        "//span[contains(text() , 'Providing the best environment for children to learn - Teacher')]")

    article_Url = "https://medium.com/@dmdhairyamishra/the-early-phase-of-ai-exploring-the-past-present-and-future-e3286df2a571"

    # Recent_Projects = (f"{locator_xpath}", "//span[contains(text() , 'ArticleToVideo')]")
    articletovideoLoader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    next = (f"{locator_xpath}", "//button[text() = 'Next']")
    Story = f"{locator_xpath}", "//h4[text() = 'Story']"
    Visual = f"{locator_xpath}", "//h4[text() = 'Visuals']"
    Audio = f"{locator_xpath}", "//h4[text() = 'Audio']"
    Text = f"{locator_xpath}", "//h4[text() = 'Text']"
    element = f"{locator_xpath}", "//h4[text() = 'Elements']"
    Styles = f"{locator_xpath}", "//h4[text() = 'Styles']"
    branding = f"{locator_xpath}", "//h4[text() = 'Branding']"
    format = f"{locator_xpath}", "//h4[text() = 'Format']"
    previous = By.ID, "previous_button"
    preview = By.ID, "btnPreview"
    Download_element = f"{locator_xpath}", "//a[text() = 'Download']"

    video_butn_after_click = f"{locator_xpath}", "(//img[@alt='The Early Phase of AI Exploring the Past Present and Future'])[2]"
    Scene_Duration = f"{locator_xpath}", "//span[text() = 'Scene duration:']"
    Video_Duration = f"{locator_xpath}", "//span[text() = 'Video duration:']"
    Intro = By.ID, "SceneNumberId_1_1"
    right_scroll_click = f"{locator_Css}", "button.slide-btn.scroll-rightbtn[fdprocessedid='38l60j']"
    article_name = (By.XPATH,
                    "//input[@aria-invalid='false' and @type='text' and contains(@class, 'MuiInputBase-input') and contains(@class, 'MuiOutlinedInput-input') and contains(@class, 'MuiInputBase-inputSizeSmall') and contains(@class, 'MuiInputBase-inputHiddenLabel')]")
    source = (f"{locator_xpath}", "//span[@class='author-name']")

    content = (f"{locator_Css}", "p[data-placeholder='Start typing here, or paste your script using ctrl+v']")
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    Proceed_generate = (f"{locator_xpath}", "//button[text() = 'Proceed']")
    Project = (f"{locator_xpath}", "//span[text()='My projects']")
    template = (By.ID, "template_614b1f33-0ef1-4396-bbb0-615f47333cf2")
    template_width = (f"{locator_xpath}", "//div[@class = 'aspect-ratio-card  MuiBox-root css-0']")
    Arrow = (By.ID, "Icon-Arrow-Down")
    WaterMarks = (f"{locator_xpath}", "//button[text()='Got it']")


class MyBrandingLocators:
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    MyBranding_Page_TITLE = "Pictory.AI - Home of AI Video Editing Technology"

    MyBranding = f"{locator_xpath}", "//span[text()='Brand kits']"

    Mybranding_loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    MyBranding_Page_url = {
        "dev": f'{dev_url}/branding',
        "staging": f'{dev_url}/branding',
        "prod": f'{dev_url}/branding',
        # Add more environments if needed
    }

    # branding_loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    branding_loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")

    brandCreate = (
        f"{locator_xpath}",
        "//button[contains(@class, 'MuiButton-outlinedPrimary') and contains(@class, 'MuiButton-sizeMedium')]")
    brandTemplate = (f"{locator_xpath}",
                     f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, 'MuiTypography-text_base') and contains(@class, 'modal-title')]")

    # Template
    brandName = (f"{locator_xpath}",
                 f"//p[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('body1')}') and contains(text(), 'Brand name')]")
    logo = (f"{locator_xpath}",
            f"//div[contains(@class, 'MuiBox-root')]//*[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and contains(text(), 'Brand logo')]")
    color = (f"{locator_xpath}", f"//span[text()='Brand colors']")
    font = (f"{locator_xpath}", "//span[text()='Brand font']")
    Create = (f"{locator_xpath}", "//div[normalize-space()='Create']")
    Cancel = (f"{locator_xpath}", "//button[normalize-space()='Cancel']")

    mybrand = (f"{locator_xpath}", "//span[@class='MuiTypography-root MuiTypography-text_2xl brand-hub css-guxprt']")

    # template field
    brand_name = (f"{locator_xpath}", "//input[@placeholder='Untitled brand']")
    color_name = (f"{locator_xpath}",
                  f"//div[contains(@class, 'uploaded-brand-logo') and contains(@class, 'position-relative') and contains(@class, 'add-more-logo-colors') and contains(@class, 'pointer') and .//span[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and text()='Add color']]")
    color_Input = (By.CLASS_NAME, "color-picker-input")

    dropdown_Font = (f"{locator_xpath}", "//input[@placeholder='Select font']")
    fonts = (f"{locator_xpath}", "//input[contains(@class, 'MuiInputBase-inputAdornedEnd')]")
    dropdown_button = (f"{locator_xpath}", "//button[contains(@class, 'MuiAutocomplete-popupIndicator')]")
    anton = (f"{locator_xpath}", "//div[contains(text(), 'Anton')]")

    brandSuccesful_text = (f"{locator_xpath}", "//p[contains(text(), 'Great Job! Brand successfully created')]")
    brandlimit_profesional = (f"{locator_xpath}", "//h5[@class='vertical-point-value' and text()='5 / 5']")

    brandlimit_starter1 = (f"{locator_xpath}", "//h5[@class='vertical-point-value' and text()='1 / 1']")
    brandlimit_starter0 = (f"{locator_xpath}", "//h5[@class='vertical-point-value' and text()='0 / 1']")

    branding_drop = (f"{locator_xpath}",
                     "//div[contains(@class, 'MuiInputBase-root') and contains(@class, 'MuiOutlinedInput-root') and contains(@class, 'MuiInputBase-colorPrimary') and contains(@class, 'MuiInputBase-formControl') and contains(@class, 'dropdown-tile')]")

    defaultbrand = (
        f"{locator_xpath}",
        f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and contains(text(), 'default_brand')]")
    branding_select = (
        f"{locator_xpath}", "(//span[contains(@class, 'MuiTypography-text_sm') and contains(text(), 'brand61')])[1]")
    continue_butn = (f"{locator_xpath}",
                     "//button[contains(@class, 'MuiButton-containedPrimary') and contains(text(), 'Continue')]")
    brand_successful = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('body2')}')]")
    # Visuals - Intro, Outro, others
    add_library_OutroIntro = (f"{locator_xpath}", "(//span[contains(text(), 'Add from library')])[1]")
    Intro = (f"{locator_xpath}", "//button[@class='btn btn-outline-secondary btn-sm' and contains(text(), 'intro')]")
    video = (f"{locator_xpath}", "(//video)[2]")
    Add = (f"{locator_xpath}", '(//span[@aria-label="Add to brand"])[1]')

    remove_butn = (f"{locator_xpath}", "//button[normalize-space()='Remove']")
    close = (f"{locator_xpath}",
             f"//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'MuiIconButton-sizeMedium')]//*[name()='svg' and @data-testid='CloseIcon']")
    # music - Library
    Add_butn = (f"{locator_xpath}", "//button[normalize-space()='Add']")
    addmusic_library = (f"{locator_xpath}", "(//span[contains(text(), 'Add from library')])[2]")
    searchTrack = (f"{locator_xpath}", "//input[@placeholder='Search tracks']")

    # music - Library
    deleteBrand = (f"{locator_xpath}", "//span[@aria-label='Delete']/button")
    AIVoice_library = (f"{locator_xpath}", "(//span[contains(text(), 'Add from library')])[3]")


class EditVideoLocators:
    Proceed_buton = (f"{locator_xpath}", "(//button[@id='btnGo'])[2]")
    name = (f"{locator_Css}", "input[placeholder='Enter your video name']")
    content = (f"{locator_Css}", "p[data-placeholder='Start typing here, or paste your script using ctrl+v']")

    youtube = (By.XPATH, "//input[@placeholder='https://']")
    # youtube = (By.ID, "mui-12")
    generate_button = (By.ID, "btnGenerate")
    Proceed_video = (f"{locator_xpath}", "//button[normalize-space()='Proceed']")
    textInput_loader = (f"{locator_xpath}", "//span[@role='progressbar']//*[name()='svg']")
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    progress = (f"{locator_xpath}", "//div[@id='dynamic']")
    project = (f"{locator_Css}",
               "input.MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputSizeSmall")

    # summary
    Transcription = (By.ID, "template_tab_1")
    Recent_Projects = (f"{locator_xpath}", "//span[contains(text() , 'Untitled Project')]")
    slider = (f"{locator_xpath}", "//li[normalize-space()='Remove filler words']//span[@class='slider round']")
    TranscriptionText = (f"{locator_Css}", "div.transcription-text")
    addhighlight = (By.XPATH, "//span[contains(text(), 'Add to highlights')]")

    highlight = (By.ID, "template_tab_2")
    Download = (f"{locator_xpath}", "//div[@id='generate-button-dropdown']//a//*[name()='svg']")
    previous = (f"{locator_xpath}", "//a[text()= 'Previous']")
    Download_Video = (f"{locator_xpath}", "//span[normalize-space()='Download video']")
    DownloadVideo_Butn = (f"{locator_xpath}", "//button[contains(text(),'Download video')]")

    demo_vid = (f"{locator_xpath}", "//a[normalize-space()='demo video']")
    defaultbrand = (
        f"{locator_xpath}",
        f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and contains(text(), 'brand01')]")
    branding_select = (f"{locator_xpath}",
                       f"//span[contains(@class,'{class_name.get('root')} {class_name.get('text')}')][normalize-space()='brand']")
    transcription = (f"{locator_xpath}", "//div[@id='p_0']/p[not(preceding-sibling::p[@id='p_0'])]")
    paras = (f"{locator_xpath}", "//*[@id='orignalArticleDiv']/div[2]")
    autohighlight = (
        f"{locator_xpath}", "//p[contains(@class, 'MuiTypography-root') and contains(text(), 'Auto highlight')]")

    download_highlight = (f"{locator_xpath}", "//button[text()='Download highlights video']")
    download_highlights_video = (f"{locator_xpath}", "//span[text()='Download highlights video']")
    chkbox = (f"{locator_xpath}", "(//div[@class='highlights-row']//input[@type='checkbox'])[1]")
    video_clip = (f"{locator_xpath}",
                  "//button[@type='button' and @title='Download video clips for selected highlights' and contains(@class, 'btn') and contains(@class, 'btn-default')]")
    chkbox1 = (f"{locator_xpath}", "(//div[@class='highlights-row']//input[@type='checkbox'])[2]")
    unhighlight_buton = (f"{locator_xpath}",
                         "//button[@type='button' and @title='Unhighlight selected sentences' and contains(@class, 'btn') and contains(@class, 'btn-default')]")

    CustomizeVideo = (f"{locator_xpath}",
                      "//a[contains(@class, 'btn btn-outline-default btn-submit btn-disabled btn--prevs1 mr-2 highlightVideoHover')]")
    view = (f"{locator_xpath}", "//div[@class='MuiBox-root css-15zum9u']")
    list_res = (f"{locator_xpath}", "//ul[@role='listbox']")

    transcription_Generation = (f"{locator_xpath}",
                                "//div[@role='alert' and contains(@class, 'Toastify__toast-body') and text()='Transcription is completed']")


class VisualVideoLocators:
    proceed = (f"{locator_xpath}",
               "//button[@id='btnGo' and contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'visuals-to-video-button')]")
    visual_txt = (f"{locator_xpath}", "//span[normalize-space()='Visualsto Video']")
    file_Import = (By.ID, "visual-to-upload")
    dropfiles = (f"{locator_xpath}", "//center[normalize-space()='Drag and drop files or browse computer']")


class StoryboardLocators:
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")

    Recent = (f"{locator_xpath}", "//button[contains(text(),'Recent')]")
    Recent_Projects = (f"{locator_xpath}", "//span[contains(text() , 'test virtualization')]")
    Storyboard_URL = {
        "dev": f'{dev_url}/storyboard/scripttovideo',
        "staging": f'{dev_url}/storyboard/scripttovideo',
        "prod": f'{dev_url}/storyboard/scripttovideo',
        # Add more environments if needed
    }

    Format = (f"{locator_xpath}", "//h4[normalize-space()='Format']")
    Text = (f"{locator_xpath}", "//h4[normalize-space()='Text']")
    selectVideo_resolution = (
        f"{locator_xpath}", "//h5[@class='mb-0 track-heading blue' and contains(text(), 'Select video resolution')]")

    landScape_click = (f"{locator_xpath}", "//img[@src='/icons/aspect-ratios/16x9.png']")
    landScape = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')} {class_name.get('body1')}') and contains(text(), 'Landscape')]")
    porTrait_click = (
        f"{locator_xpath}", "//img[contains(@src, '/icons/aspect-ratios/9x16.png') and @alt='9:16 Portrait']")
    porTrait = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')} {class_name.get('body1')}') and contains(text(), 'Portrait')]")
    sQuare_click = (f"{locator_xpath}", '//img[@alt="1:1 Square"]')
    sQuare = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')} {class_name.get('body1')}') and contains(text(), 'Square')]")

    textboxes = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')} {class_name.get('body1')}') and contains(text(), 'Default Text Boxes')]")

    headFont = (f"{locator_xpath}",
                "//button[contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-outlined') and contains(@class, 'MuiButton-outlinedGrey') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-outlinedSizeMedium') and contains(@class, 'MuiButton-fullWidth') and contains(text(), 'Add a Heading')]")
    headSize = (f"{locator_xpath}", "//input[@value = '66']")

    SubheadFont = (f"{locator_xpath}",
                   "//button[contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-outlined') and contains(@class, 'MuiButton-outlinedGrey') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-outlinedSizeMedium') and contains(@class, 'MuiButton-fullWidth') and contains(text(), 'Add a Subheading')]")
    SubheadSize = (f"{locator_xpath}", "//input[@value = '42']")

    BodyFont = (f"{locator_xpath}", "//button[contains(text(), 'Add a Body text')]")
    Bodysize = (f"{locator_xpath}", "//input[@value = '20']")
    Story = f"{locator_xpath}", "//p[text() = 'Story']"


class TeamLocators:
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    team = (f"{locator_xpath}", "//button[normalize-space()='Create a team']")
    Voiceover = (f"{locator_xpath}", "//button[contains(text(),'Voiceover')]")
    Upgrade_butn = (f"{locator_xpath}", "(//button[normalize-space()='Upgrade'])[4]")

    youtube = (
        f"{locator_xpath}",
        "(//input[contains(@class, 'MuiInputBase-input') and contains(@class, 'MuiInput-input')])[2]")

    defaultbrand = (f"{locator_xpath}",
                    f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and contains(text(), 'Selectdefault_brand')]")
    branding_select = (f"{locator_xpath}",
                       f"//span[contains(@class,'{class_name.get('root')} {class_name.get('text')}')][normalize-space()='Brand']")

    teamdefaultbrand = (f"{locator_xpath}",
                        f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and contains(text(), 'Brand01')]")
    team_BuyNow_butn = (f"{locator_xpath}",
                        "(//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-text') and contains(@class, 'MuiButton-textPrimary') and contains(text(), 'Buy Now')])[3]")
    Proceed_butn_0 = (f"{locator_xpath}",
                      "(//button[contains(@class, 'MuiButton-contained')])[2]")
    Proceed_butn = (f"{locator_xpath}",
                    "(//button[contains(@class, 'MuiButton-contained')])[3]")
    article_name = (
        f"{locator_xpath}", "//input[@value='The Early Phase of AI Exploring the Past Present and Future']")
    new_team = (f"{locator_xpath}", "//div[contains(@class, 'MuiTypography-root') and text()='New team']")
    # team_name = (f"{locator_xpath}", "//div[@class='MuiTypography-root MuiTypography-caption css-1p1lqln']")

    Plan_confirmation = (
        f"{locator_xpath}", "//button[contains(@class, 'MuiButton-containedPrimary') and text()='Confirm']")

    team_Project_url = {
        "dev": f'{dev_url}/myvideos',
        "staging": f'{dev_url}/myvideos',
        "prod": f'{dev_url}/myvideos',
        # Add more environments if needed
    }
    name = (f"{locator_xpath}", "//input[@placeholder='Type here...']")
    email = (f"{locator_xpath}", "//input[@placeholder='Enter email address']")
    team_butn = (f"{locator_xpath}", "//div[@class='MuiBox-root css-0' and text()='Create team']")
    start = (f"{locator_xpath}",
             "//a[@class='appcues-button-success appcues-button' and @data-step='end-flow' and contains(text(), 'Start a fresh project')]")
    TeamProject = (f"{locator_xpath}",
                   "//span[contains(@class, 'MuiTypography-root') and text()='Team projects']")
    team_account = (f"{locator_xpath}",
                    "//div[contains(@class, 'MuiTypography-root') and contains(text(), 'Pictory automate')]")
    teamaccount_name = (f"{locator_xpath}", "//span[normalize-space()='Pictory automate']")
    createProject = (f"{locator_xpath}", "//button[normalize-space()='Create project']")
    teamfirst_project = (f"{locator_xpath}",
                         "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1he72jf']")

    # Import Project
    ImportProjectTo_collaborate = (f"{locator_xpath}", "//button[normalize-space()='Import projects to collaborate']")
    Import_Myprojects = (
        f"{locator_xpath}", "//div[contains(@class, 'MuiBox-root') and contains(text(), 'Import my projects')]")
    personal_Workspace = (f"{locator_xpath}", "//button[@id='personal-workspace-tab']")
    project_files = (f"{locator_xpath}", "//button[@id='upload-project-tab']")
    cancel_butn = (f"{locator_xpath}", "//button[normalize-space()='Cancel']")
    import_butn = (f"{locator_xpath}", "//div[normalize-space()='Import']")
    createfolder = (f"{locator_xpath}", "//button[normalize-space()='Create folder']")
    folder_name = (f"{locator_Css}", "input[placeholder='Type here...']")
    createbtn = (f"{locator_xpath}", "//button[text() = 'Create']")

    error_message = (f"{locator_xpath}", "//span[@class='error-span']")

    Import_location = f"{locator_xpath}", "//button[text() = 'Import projects']"
    Search = (f"{locator_Css}", "input[placeholder='Search by name']")

    # Manage team Page elements
    ManageTeam = (f"{locator_xpath}",
                  f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, 'header-links-item') and contains(text(), 'Manage team')]")
    Team_member = (f"{locator_xpath}", "//span[normalize-space()='Team members']")

    Manage_team_URL = {
        "dev": f'{dev_url}/account-settings',
        "staging": f'{dev_url}/account-settings',
        "prod": f'{dev_url}/account-settings',
    }

    # HomePage url

    DEV_HOME_Page_URL = f"{dev_url}/textinput"
    STAGING_HOME_Page_URL = "https://master-v1-staging.d27l04s7h73icm.amplifyapp.com/textinput"
    PROD_HOME_Page_URL = "https://app.pictory.ai/textinput"

    add_team_member = (f"{locator_xpath}",
                       "//p[contains(@class, 'MuiTypography-body1') and contains(@class, 'css-117rfk8') and @style='font-size: 16px; margin-left: 5px;']")

    HOME_Page_URL = {
        "dev": f'{dev_url}/textinput',
        "staging": f'{dev_url}/textinput',
        "prod": f'{dev_url}/textinput',
    }

    Enter_email_field = (f"{locator_xpath}",
                         "//input[@placeholder='Enter email address' and @type='text' and @aria-label='Enter email address' and contains(@class, 'MuiInputBase-input')]")
    cancel_email_field = (f"{locator_xpath}", "//svg[contains(@data-testid, 'CancelRoundedIcon')]")
    send_Invite = (f"{locator_xpath}", "//button[normalize-space()='Send invite']")
    added_emailID = (f"{locator_xpath}", "//td[normalize-space()='pictoryautomate8642@gmail.com']")
    Delete_icon = (f"{locator_xpath}",
                   "//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1')]//*[name()='svg']")
    Delete_butn = (f"{locator_xpath}", "//button[normalize-space()='Delete']")
    userSuccesful_text = (f"{locator_xpath}",
                          f"//p[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('body2')}') and contains(text(), 'User deleted successfully')]")
