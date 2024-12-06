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
    email_field = (f"{locator_Id}", "emailField")
    password_field = (f"{locator_Id}", "outlined-adornment-password")
    login_bn = (f"{locator_xpath}", "//button[normalize-space()='Login']")

    login_Loader = (f"{locator_xpath}", "//div[@class='dot-flashing']")
    Email_field_Required = (f"{locator_xpath}", "//*[@id='emailField-helper-text']")
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

    totalpay = (
        f"{locator_xpath}",
        "//span[contains(@class, 'cb-button__text') and normalize-space(text())='Complete Purchase']")
    # totalpay = (f"{locator_xpath}", "//span[contains(@class, 'cb-button__text') and contains(text(), 'Pay')]")
    credit_card = (f"{locator_xpath}", "//span[contains(@class, 'cb-payment__text') and text()='Credit Card']")

    # cards
    First = (By.ID, 'first_name')
    Last = (By.ID, 'last_name')
    Card_Number = (By.ID, 'number')
    month_input = (By.ID, 'exp_month')
    year_input = (By.ID, 'exp_year')
    biling_code = (By.ID, 'billing_zip')
    CVV_Cards = (By.ID, 'cvv')

    Terms_and_condition_Link = f"{locator_xpath}", "//a[text()='Terms and Conditions']"

    SIGNUP_Verify = {
        "dev": f'{dev_url}/questionnaire',
        "staging": f'{dev_url}/questionnaire',
        "prod": f'{dev_url}/questionnaire',
        # Add more environments if needed
    }

    HOME_Page_URL = {
        "dev": f'{dev_url}/home',
        "staging": f'{dev_url}/home',
        "prod": f'{dev_url}/home',
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
             "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-textPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-textSizeMedium') and contains(@class, 'upgrade-button') and contains(@class, 'button') and contains(text(), 'Buy now')]")
    renew_Professional=(f"{locator_xpath}", "//button[@id = 'ctaPlanCardProfessional']")
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
        f"{locator_xpath}",
        "(//span[contains(@class, 'MuiTypography-regular_xl_semibold') and contains(text(), '$')])[1]")
    Manage_Subscription = (f"{locator_xpath}", "//span[text() = 'Manage subscription']")

    # Gety image and eleven Lab VO
    buy_gety = (f"{locator_xpath}", "//span[contains(text(), 'Buy Add-on')]")
    Gety_enable = (f"{locator_xpath}", "(//h5[contains(@class, 'vertical-point-value') and text()='Enabled'])[1]")
    remove_addOn_butn = (f"{locator_Id}", "idDlgButtonPrimary")
    remove_addOn_Ok = (f"{locator_xpath}", "(//button[@id='idDlgButtonPrimary'])[2]")

    biling_Code = f"{locator_xpath}", "//input[@type='password' and @name='answer']"
    ok_buton = (f"{locator_Id}", "buttonSubmit")

    next = f"{locator_xpath}", "//span[normalize-space() = 'Next']"
    remove_addOn = (f"{locator_xpath}",
                    "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-text_sm') and contains(text(), 'Remove Add-on')]")
    # removegety = (f"{locator_xpath}", "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-text_2xl') and contains(@class, 'MuiTypography-text_2xl') and contains(text(), 'Thank you')]")
    removegety = (f"{locator_xpath}", "//p[contains(text(), 'Your Getty images add-on subscription ends on')]")

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
        "dev": f'{dev_url}/home',
        "staging": f'{dev_url}/home',
        "prod": f'{dev_url}/home',

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
    Upgrade_butn = (f"{locator_xpath}", "//span[text()='Upgrade']")
    cancel = (f"{locator_xpath}", "//span[text()='Cancel subscription']")
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
    discovr = (f"{locator_xpath}", "//span[text()='Discover']")
    dislink = (f"{locator_xpath}", "//span[contains(text(), 'Quick Start')]")
    tiplink = (f"{locator_xpath}", "//span[contains(text(), 'How To')]")
    HOME_Page_URL = f"{dev_url}/textinput"

    home = (f"{locator_xpath}", "//span[text()='Home']")

    DEV_tips_PAGE_URL = "https://kb.pictory.ai/en/"
    DEV_Discovr_PAGE_URL = "https://www.youtube.com/playlist?list=PLB8TfTqC4SQLHNE05rBFPFWDt736_EZrs"

    # WatchTutorial_Link = (f"{locator_xpath}", "//a[contains(text(), 'Watch tutorial')]")
    Project = (f"{locator_xpath}", "//span[text()='Projects']")

    loader = (f"{locator_xpath}", "//span[contains(@class, 'MuiCircularProgress-root')]")
    recent_Project = (f"{locator_xpath}", "//span[text()='Recent projects']")
    hover_Profile = (f"{locator_Css}", f"div.MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault")
    Demo = (f"{locator_xpath}", "//span[text()='Demo Project']")

    My_account = (f"{locator_xpath}", "//span[text() = 'My account']")
    My_Subscription = (f"{locator_xpath}", "//span[text() = 'My subscription']")
    Affiliate_dash = (f"{locator_xpath}", "//span[text() = 'Affiliate dashboard']")
    logout = (f"{locator_xpath}", "//span[text() = 'Log out']")
    BlogToVideo = (f"{locator_xpath}",
                   "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='URL to video']")
    editVideo = (f"{locator_xpath}",
                 "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='AI video editor']")
    VisualToVideo = (f"{locator_xpath}",
                     "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='Images to video']")
    PptToVideo = (f"{locator_xpath}",
                  "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='PPT to video']")
    ScriptToVideo = (f"{locator_xpath}",
                     "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='Text to video']")

    profileName = (f"{locator_xpath}", "//span[@id='idLblHelloUser' and contains(text(), 'Hello')]")

    help = (f"{locator_xpath}", "//span[text()='Help']")
    becomeAffiliate = (f"{locator_xpath}", "//span[text() = 'Become affiliate']")
    Affiliate = (f"{locator_xpath}", "//button[text()='Become an affiliate today']")


class PPTtoVideoLocators:
    Proceed_buton = (f"{locator_xpath}",
                     "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='PPT to video']")


class ScriptToVideoLocators:
    Proceed_buton = (f"{locator_xpath}",
                     "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='Text to video']")

    name = (f"{locator_Css}", "input[placeholder='Enter your video name']")
    content = (f"{locator_Css}", "p[data-placeholder='Start typing here, or paste your script using ctrl+v']")
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    Proceed_generate = (f"{locator_xpath}", "//button[text() = 'Proceed']")

    note_Story = (f"{locator_Css}", "p.addRemoveHighlightPTag span.editor-container")

    Recent_Project_EVUT = (f"{locator_xpath}",
                           "//span[text()='EVUT_autohighlight_defaultVO_dectext_coloroverlay_Transition_Element_Custom_stock_visual_img']")

    Recent_Project_scriptvideo = (f"{locator_xpath}",
                                  "//span[text()='scriptvideo_customVo_text_coloroverlay_Transition_Element_Custom_stock_visual_image']")
    Project = (f"{locator_xpath}", "//span[text()='My projects']")
    template = (By.ID, "template_614b1f33-0ef1-4396-bbb0-615f47333cf2")
    template_width = (f"{locator_xpath}", "//div[@class = 'aspect-ratio-card  MuiBox-root css-0']")
    saved_Video = (f"{locator_xpath}", "//span[text()='AI in health domain']")
    Recent_Project_A2v = (f"{locator_xpath}",
                          "//span[text()='A2V_Image_fetch']")

    # Arrow = (f"{locator_xpath}", "//*[@id='Icon-Arrow-Down']")
    Arrow = (By.ID, "Icon-Arrow-Down")
    voice_successful = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('body2')}')]")
    voice_applied = (f"{locator_xpath}",
                     f"//a[@id='voiceTrack1010']//div[contains(@class,'applied hide-on-hover')][normalize-space()='Applied']")

    editor = (
        f"{locator_xpath}", "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-h4b')]")

    complete = (f"{locator_xpath}", "//h6[@class='increasing-txt']")
    customization = (f"{locator_xpath}", "//h4[normalize-space()='Preparing for video customization']")
    ai_evolution_script = {
        "Introduction": (
            "Artificial Intelligence represents one of the most transformative technological advancements of the 21st century. "
            "This introduction explores the fascinating journey of AI from its earliest conceptualizations to its current breakthroughs, showcasing its profound impact on industries and daily life. "
            "AI, as a field of study, has evolved from the rudimentary ideas of automating tasks and solving problems to complex systems capable of learning, reasoning, and interacting with the world in sophisticated ways. "
            "The story of AI is marked by significant milestones, including the development of early algorithms, the creation of the first AI programs, and the ongoing evolution of machine learning and deep learning technologies. "
        ),

        "Early Foundations of AI": (
            "The origins of Artificial Intelligence can be traced back to ancient philosophical inquiries about the nature of intelligence and the possibility of creating intelligent machines. "
            "In the early 20th century, the formal study of AI began with the development of mathematical logic and theories of computation. Notable early figures include Alan Turing, whose work on the Turing Machine laid the groundwork for modern computing. "
            "The 1956 Dartmouth Conference is often considered the birth of AI as a formal field of study, where the term 'Artificial Intelligence' was coined by John McCarthy and his colleagues. "
            "During the early years of AI research, significant progress was made with the development of symbolic AI and the creation of the first AI programs. Early AI systems, such as the Logic Theorist and the General Problem Solver, demonstrated the potential of AI to solve complex problems. "
        ),

        "Healthcare Impact": (
            "Artificial Intelligence has made significant strides in transforming healthcare, driving innovations that enhance diagnostics, treatment plans, patient care, and overall medical practices. "
            "In diagnostics, AI-powered tools have revolutionized imaging techniques, enabling earlier and more accurate detection of diseases such as cancer, cardiovascular conditions, and neurological disorders. Machine learning algorithms analyze medical images to identify patterns and anomalies that may be missed by human radiologists. "
            "AI is also playing a critical role in developing personalized treatment plans. By analyzing patient data, including genetic information, medical history, and lifestyle factors, AI systems can recommend tailored treatment options that improve outcomes and minimize side effects. "
            "In patient care, AI-driven virtual assistants and chatbots provide round-the-clock support, answering questions, scheduling appointments, and offering medication reminders. These tools enhance patient engagement and streamline healthcare delivery. "
        ),

        "Business Transformation": (
            "Artificial Intelligence is driving significant business transformation by enhancing productivity, decision-making, and customer experiences across various industries. "
            "In the realm of productivity, AI-powered automation tools streamline repetitive tasks, reduce operational costs, and improve efficiency. Robotic Process Automation (RPA) and AI-driven software solutions handle tasks such as data entry, invoice processing, and customer service inquiries. "
            "AI also plays a crucial role in data-driven decision-making. Advanced analytics and machine learning algorithms analyze vast amounts of data to uncover insights, identify trends, and predict future outcomes. This enables businesses to make informed decisions, optimize strategies, and gain a competitive edge. "
            "Customer experiences are significantly enhanced through AI-powered personalization. By analyzing customer behavior, preferences, and interactions, AI systems deliver tailored recommendations, targeted marketing campaigns, and personalized product offerings. This improves customer satisfaction and drives brand loyalty. "
        ),

        "Ethical Considerations": (
            "As Artificial Intelligence continues to evolve, ethical considerations have become increasingly important. This section examines the ethical dimensions of AI, focusing on issues such as privacy, fairness, transparency, and accountability. "
            "Privacy concerns arise from the collection and use of personal data by AI systems. Ensuring that data is handled responsibly and with consent is crucial to maintaining trust and protecting individuals' privacy. The section will explore best practices for data protection and the role of regulations such as the General Data Protection Regulation (GDPR). "
            "Fairness and bias are critical issues in AI development. AI systems can inadvertently perpetuate or exacerbate existing biases if the data used to train them is biased. This section will discuss strategies for mitigating bias in AI algorithms and ensuring fairness in AI-driven decision-making processes. "
            "Transparency and accountability are essential for building trust in AI systems. The section will explore the importance of transparency in AI development, including the need for explainable AI and clear communication about how AI systems make decisions. "
            "Public engagement and dialogue are also critical for shaping the future of AI. This section will emphasize the importance of inclusive and transparent discussions about the ethical implications of AI and the role of stakeholders in ensuring positive societal outcomes."
        ),

        "Education Revolution": (
            "Artificial Intelligence is revolutionizing education by personalizing learning experiences, automating administrative tasks, and making education more accessible worldwide. "
            "Intelligent tutoring systems powered by AI provide personalized learning experiences tailored to the needs of individual students. These systems adapt to students' learning styles, track their progress, and offer targeted feedback to enhance their understanding of complex concepts. "
            "AI also automates administrative tasks, such as grading, scheduling, and student enrollment. This automation reduces the administrative burden on educators, allowing them to focus more on teaching and student engagement. "
            "The integration of AI into education extends to enhancing accessibility for students with disabilities and those in underserved regions. AI-driven tools support inclusive education by providing assistive technologies, language translation, and adaptive learning platforms. "
            "The future of AI in education holds promise for further advancements, including the development of more sophisticated adaptive learning systems, AI-powered educational content, and innovative pedagogical approaches."
        ),

        "Transportation Advancements": (
            "Artificial Intelligence has significantly impacted the transportation sector, driving advancements in autonomous vehicles, smart traffic management systems, and overall safety and efficiency. "
            "Autonomous vehicles, or self-driving cars, represent one of the most notable applications of AI in transportation. AI technologies, including computer vision, machine learning, and sensor fusion, enable vehicles to navigate and make decisions in complex environments. "
            "Smart traffic management systems use AI to optimize traffic flow, reduce congestion, and improve road safety. By analyzing real-time traffic data, AI systems can adjust traffic signals, manage road usage, and provide real-time information to drivers. "
            "AI is also enhancing safety and efficiency in public transportation. AI powered systems optimize route planning, manage fleet operations, and improve passenger experiences. "
            "Case studies of AI applications in transportation highlight the impact of these technologies on reducing travel times, lowering emissions, and enhancing overall mobility. "
            "The challenges of implementing AI in transportation include addressing regulatory concerns, ensuring safety and reliability, and managing the integration of AI with existing infrastructure. "
            "The future of AI in transportation holds promise for further innovations, including advanced autonomous driving capabilities, smart city infrastructure, and the development of sustainable transportation solutions."
        ),

        "Environmental Sustainability": (
            "Artificial Intelligence is contributing to environmental sustainability by optimizing resource use, combating climate change, and promoting eco-friendly technologies. "
            "AI technologies are used to analyze environmental data, model climate change scenarios, and develop strategies for mitigating its effects. Machine learning algorithms process vast amounts of data to identify patterns, predict environmental changes, and inform policy decisions. "
            "In resource management, AI helps optimize the use of natural resources, such as water, energy, and raw materials. AI driven systems improve efficiency in agriculture, energy production, and waste management, reducing environmental impact and promoting sustainability. "
            "AI is also playing a role in the development of eco-friendly technologies, such as renewable energy sources, smart grids, and green manufacturing practices. These technologies contribute to reducing carbon emissions and promoting a circular economy. "
            "Case studies of AI applications in environmental sustainability illustrate the positive impact of these technologies on reducing environmental footprint and enhancing conservation efforts. "
            "The challenges of leveraging AI for environmental sustainability include addressing data quality issues, ensuring the responsible use of AI, and fostering collaboration among stakeholders. "
            "The future of AI in environmental sustainability holds promise for further advancements in climate modeling, resource optimization, and the development of innovative solutions for a sustainable future."
        ),

        "Entertainment Innovation": (
            "Artificial Intelligence is revolutionizing the entertainment industry by transforming content creation, enhancing user experiences, and personalizing recommendations. "
            "In content creation, AI technologies are used to generate and edit music, video, and visual art. AI algorithms analyze existing content to create new works, assist in scriptwriting, and enhance special effects in films and games. "
            "AI is also used to personalize user experiences by analyzing viewing habits, preferences, and interactions. AI-driven recommendation systems suggest content tailored to individual tastes, improving user satisfaction and engagement. "
            "The integration of AI in gaming has led to more immersive and interactive experiences. AI algorithms control non-player characters, generate dynamic game environments, and adapt gameplay based on player behavior. "
            "Case studies of AI applications in entertainment highlight the innovative ways in which AI is shaping the industry, from creating blockbuster films to developing cutting-edge video games. "
            "The challenges of integrating AI into entertainment include addressing ethical concerns related to content creation, ensuring data privacy, and managing the impact of AI on creative industries. "
            "The future of AI in entertainment holds promise for further advancements in content generation, interactive experiences, and personalized media."
        ),

        "Cybersecurity Measures": (
            "Artificial Intelligence plays a crucial role in cybersecurity by enhancing threat detection, data protection, and maintaining digital security in a rapidly evolving landscape. "
            "AI-driven cybersecurity systems analyze network traffic, detect anomalies, and identify potential threats in real-time. Machine learning algorithms improve the accuracy of threat detection by learning from historical data and adapting to new attack patterns. "
            "Data protection is another critical area where AI contributes to cybersecurity. AI technologies help secure sensitive information by detecting unauthorized access, preventing data breaches, and ensuring compliance with data protection regulations. "
            "The use of AI in maintaining digital security involves implementing advanced encryption techniques, managing access controls, and monitoring for signs of cyberattacks. AI systems also provide insights into emerging threats and vulnerabilities. "
            "Case studies of AI applications in cybersecurity illustrate the effectiveness of these technologies in preventing and responding to cyber incidents. These examples highlight the benefits of AI in enhancing security measures and protecting digital assets. "
            "The challenges of using AI in cybersecurity include addressing issues of false positives, ensuring the ethical use of AI, and managing the evolving nature of cyber threats. "
            "The future of AI in cybersecurity holds promise for further advancements in threat detection, data protection, and the development of proactive security measures."
        ),

        "AI in Legal Tech": (
            "Artificial Intelligence is transforming the legal industry with advancements in document analysis, case prediction, and assisting legal professionals in managing complex cases. "
            "AI technologies are used to streamline legal processes by automating tasks such as document review, legal research, and contract analysis. AI-powered tools help lawyers and judges analyze case law, identify relevant precedents, and draft legal documents more efficiently. "
            "Case prediction is another area where AI is making an impact. Machine learning algorithms analyze historical case data to predict the likely outcomes of legal disputes, helping lawyers develop more effective strategies and advise clients on potential risks. "
            "AI-assisted legal research tools provide insights into complex legal issues, improve the accuracy of legal analysis, and reduce the time required to conduct research. These tools enhance the efficiency of legal professionals and improve the quality of legal services. "
            "Case studies of AI applications in the legal industry highlight the benefits of these technologies in improving access to justice, reducing costs, and enhancing the overall effectiveness of legal services. "
            "The ethical considerations of AI in the legal field include issues of fairness, transparency, and the potential impact on the legal profession. Ensuring that AI systems are used responsibly and ethically is crucial for maintaining trust in the legal system."
        ),

        "AI in Manufacturing": (
            "Artificial Intelligence is revolutionizing manufacturing processes, driving automation, quality control, and predictive maintenance."
            "AI technologies enhance manufacturing efficiency by automating production lines, optimizing processes, and improving product quality."
            "Quality control is another area where AI plays a significant role. Machine learning algorithms analyze data from sensors and cameras to detect defects, monitor production standards, and ensure consistent product quality. "
            "Predictive maintenance is a key application of AI in manufacturing. AI systems analyze equipment data to forecast potential failures, schedule maintenance, and prevent unplanned downtime. This approach improves operational efficiency and reduces maintenance costs. "
            "Case studies of AI applications in manufacturing highlight the positive impact of these technologies on productivity, efficiency, and cost reduction. Examples from industries such as automotive, electronics, and consumer goods illustrate the benefits of AI in modern manufacturing. "
            "The challenges of implementing AI in manufacturing include issues of integration with existing systems, high costs, and the need for skilled personnel. Addressing these challenges is essential for maximizing the benefits of AI in manufacturing."
        ),

        "AI in Drug Discovery": (
            "Artificial Intelligence is accelerating drug discovery by optimizing the development of new pharmaceuticals and analyzing vast datasets."
            "AI technologies are used to analyze biological data, identify potential drug candidates, and predict the efficacy of drug compounds. Machine learning algorithms process complex datasets to uncover patterns and insights that aid in the drug discovery process."
            "In drug development, AI optimizes clinical trial designs, analyzes trial data, and improves patient recruitment. AI-driven tools enhance the efficiency of clinical trials, reduce costs, and accelerate the development of new therapies."
            "Case studies of AI applications in drug discovery illustrate the transformative impact of these technologies on pharmaceutical research and development. Examples highlight how AI is being used to identify novel drug candidates and streamline the drug development process. "
            "The challenges of integrating AI into drug discovery include issues of data quality, regulatory considerations, and the need for interdisciplinary collaboration. Addressing these challenges is crucial for realizing the full potential of AI in drug discovery."
        ),

        "AI in Disaster Response": (
            "Artificial Intelligence is improving disaster response efforts through predictive analytics, resource allocation, and enhanced management during emergencies. "
            "AI technologies analyze data from various sources, such as satellite imagery, social media, and sensor networks, to predict and respond to natural and man-made disasters. Machine learning algorithms process this data to identify patterns and provide insights for emergency response planning. "
            "Resource allocation is another critical area where AI contributes to disaster response. AI-driven systems optimize the distribution of resources, such as medical supplies, personnel, and equipment, based on real-time needs and availability. "
            "AI also enhances disaster management by providing decision support tools that improve coordination, communication, and overall response effectiveness. These tools assist in managing logistics, assessing damage, and coordinating relief efforts. "
            "Case studies of AI applications in disaster response highlight the positive impact of these technologies on improving response times, resource management, and overall effectiveness in managing emergencies. "
            "The challenges of using AI in disaster response include ensuring data accuracy, addressing ethical considerations, and managing the integration of AI with existing response systems. "
            "The future of AI in disaster response holds promise for further advancements in predictive analytics, resource optimization, and enhanced emergency management capabilities."
        ),

        "Human Augmentation": (
            "Artificial Intelligence is enhancing human capabilities through augmentation technologies, including prosthetics, cognitive enhancement, and overall performance improvement. "
            "In the field of prosthetics, AI driven technologies are improving the functionality and usability of artificial limbs. Advanced prosthetic devices use AI to provide more natural movement, enhance control, and improve the overall quality of life for individuals with limb loss. "
            "Cognitive enhancement is another area where AI is making an impact. AI-powered tools and systems assist individuals with cognitive impairments, improve memory, and support learning and decision-making processes. These technologies enhance cognitive abilities and support mental health. "
            "AI also contributes to overall performance improvement in various domains, including sports, workplace productivity, and everyday tasks. AI-driven tools provide personalized feedback, optimize training regimens, and enhance performance through data-driven insights. "
        ),

        "Content Moderation": (
            "Artificial Intelligence plays a significant role in moderating and filtering content on digital platforms, addressing challenges related to safety, compliance, and the prevention of harmful content. "
            "AI-driven content moderation systems analyze text, images, and videos to detect and remove inappropriate or harmful content. Machine learning algorithms are trained to identify patterns and recognize content that violates platform policies or legal regulations. "
            "The challenges of content moderation include managing the vast volume of user-generated content, addressing issues of context and nuance, and ensuring the accuracy of automated moderation systems. AI systems must balance the need for effective moderation with the protection of free expression. "
            "Case studies of AI applications in content moderation highlight the effectiveness of these technologies in improving platform safety and compliance. Examples include social media platforms, online marketplaces, and news websites. "
            "The future of AI in content moderation involves advancements in natural language processing, contextual understanding, and ethical considerations. Ensuring transparency, fairness, and accountability in content moderation practices is crucial for maintaining trust and integrity on digital platforms."
        ),

        "Supply Chain Management": (
            "Artificial Intelligence is optimizing supply chain management by improving logistics, inventory management, and overall efficiency. "
            "AI-driven supply chain solutions analyze data from various sources, such as sensors, logistics systems, and market trends, to optimize inventory levels, forecast demand, and manage supply chain operations. "
            "In logistics, AI technologies enhance route planning, transportation management, and warehouse operations. Machine learning algorithms optimize delivery routes, reduce transportation costs, and improve supply chain visibility. "
            "AI also contributes to inventory management by predicting demand, managing stock levels, and minimizing inventory holding costs. These technologies improve accuracy and efficiency in managing inventory and supply chain processes. "
            "Case studies of AI applications in supply chain management illustrate the benefits of these technologies in improving efficiency, reducing costs, and enhancing overall supply chain performance. Examples from industries such as retail, manufacturing, and logistics highlight the impact of AI on supply chain operations. "
        ),
        "Language Translation": (
            "Artificial Intelligence has advanced language translation technologies, enabling real-time applications, breaking down language barriers, and enhancing global communication. "
            "AI-driven language translation systems use machine learning algorithms to analyze and translate text and speech between different languages. These systems improve translation accuracy and fluency, making communication across language barriers more seamless. "
            "Real-time translation applications, such as translation apps and devices, enable users to communicate instantly in different languages. AI technologies enhance the effectiveness of these applications by providing context-aware translations and improving language understanding. "
            "The integration of AI in language translation supports global communication by facilitating international business, travel, and cultural exchange. AI-driven translation tools break down language barriers and promote cross-cultural interactions. "
            "The challenges of using AI in language translation include addressing issues of accuracy, context, and cultural nuances. Ensuring the quality and reliability of AI-driven translations is crucial for maintaining effective communication across languages."
        ),
        "Human Computer Interaction": (
            "Artificial Intelligence is impacting human-computer interaction (HCI) by introducing innovations in user interfaces, experience design, and enhancing overall usability. "
            "AI technologies improve user interfaces by enabling natural language processing, voice recognition, and gesture-based interactions. These advancements make it easier for users to interact with computers and devices using intuitive and natural methods. "
            "In experience design, AI-driven systems create personalized and adaptive user experiences. By analyzing user behavior and preferences, AI technologies tailor interactions to individual needs, enhancing usability and satisfaction. "
            "AI also contributes to enhancing overall usability by optimizing software design, automating repetitive tasks, and providing intelligent assistance. These improvements streamline user interactions and make technology more accessible. "
        ),
        "Emotional Intelligence": (
            "Artificial Intelligence has the capability to detect and respond to human emotions, exploring applications in customer service, mental health, and other areas requiring emotional understanding. "
            "AI systems use natural language processing, sentiment analysis, and facial recognition technologies to identify and interpret human emotions. These capabilities enable AI to respond empathetically and provide appropriate support in various contexts. "
            "In customer service, AI-powered chatbots and virtual assistants use emotional intelligence to interact with users, address concerns, and provide personalized assistance. These systems enhance customer experiences by understanding and responding to emotional cues. "
            "AI is also making an impact in mental health by providing support through AI-driven therapy apps, mood tracking, and emotional well-being monitoring. These applications assist individuals in managing their mental health and accessing support when needed. "
        ),
        "Aerospace Innovations": (
            "Artificial Intelligence plays a significant role in aerospace advancements, including space exploration, aviation technology, and engineering innovations. "
            "In space exploration, AI technologies are used to analyze data from space missions, control spacecraft, and assist in the discovery of celestial objects. AI driven systems enhance the capabilities of space probes, satellites, and rovers, enabling more sophisticated exploration and research. "
            "Aviation technology benefits from AI through advancements in autonomous flight systems, predictive maintenance, and air traffic management. AI powered systems improve flight safety, optimize flight routes, and enhance overall efficiency in aviation operations. "
            "AI also contributes to engineering innovations by assisting in the design and development of advanced aerospace technologies. Machine learning algorithms analyze data from simulations, optimize designs, and improve performance in aerospace engineering. "
        )
    }

    WaterMarks = (f"{locator_xpath}", "//button[text()='Got it']")
    Download = (f"{locator_xpath}", "//a[text() = 'Download']")
    highlight_scripteditor = (f"{locator_xpath}", "//button[text()='Highlight']")
    bold = (f"{locator_xpath}", "//strong")
    clip_Board = (f"{locator_xpath}", "//button[contains(text(), 'Paste from clipboard')]")
    char_len = (f"{locator_xpath}", "(//span[contains(@class, 'MuiTypography-subtitle2b_resp')])[4]")

    # Voiceover
    apply_butn = (f"{locator_xpath}",
                  "//a[@id='voiceTrack1010']//div[contains(@class,'apply show-on-hover')][normalize-space()='Apply']")
    Voice = (
        f"{locator_xpath}", "//span[contains(@class, 'MuiTypography-root MuiTypography-regular_sm track-hd')]")
    voice_search = (f"{locator_xpath}", "//input[@placeholder='Search voices']")

    progress = (f"{locator_xpath}", "//div[@id='dynamic']")
    premiumapply_butn = (
        f"{locator_xpath}",
        "//a[@id='voiceTrack3023']//div[contains(@class,'apply show-on-hover MuiBox-root')][normalize-space()='Generate and Apply']")
    premiumvoice_applied = (f"{locator_xpath}",
                            f"//a[@id='voiceTrack3023']//button[contains(@class,'MuiButtonBase-root MuiButton-root')][normalize-space()='Applied']")

    Copypreview_link = (
        f"{locator_xpath}",
        f"//p[contains(@class, '{class_name.get('root')} {class_name.get('body1')}') and contains(text(), 'Copy preview link')]")
    close = (By.ID, "closeIcon")

    # Voiceover multi
    applyfrench_butn = (f"{locator_xpath}",
                        "//a[@id='voiceTrack1071']//div[contains(@class,'apply show-on-hover')][normalize-space()='Apply']")
    appliedfrench_butn = (f"{locator_xpath}",
                          "//a[@id='voiceTrack1071']//div[contains(@class,'applied hide-on-hover')][normalize-space()='Applied']")

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

    Voiceover_buton = (f"{locator_xpath}", "(//button[contains(text(),'Voiceover')])[2]")
    adjust_buton = (f"{locator_Id}", "recording-adjust")
    apply_butn_custom = (
        f"{locator_xpath}", "//button[contains(@class, 'MuiButtonBase-root') and contains(text(), 'Apply')]")
    close_buton = (f"{locator_Id}", "closeIcon")

    entire = (f"{locator_Id}", "recording-apply-to-all")
    customVoiceover = (f"{locator_xpath}", "(//button[contains(text(),'My uploads')])[2]")
    preview = (f"{locator_xpath}", "//a[@id='btnPreview']")
    Download_element = f"{locator_xpath}", "//a[contains(@class, 'btn-submit') and contains(@class, 'btn--nexts2') and text()='Download']"
    Scene_Duration = f"{locator_xpath}", "//span[text() = 'Scene duration:']"
    Video_Duration = f"{locator_xpath}", "//span[text() = 'Video duration:']"
    Intro = By.ID, "SceneNumberId_1_1"
    Outro = By.ID, "SceneNumberId_5_1"
    right_scroll_click = f"{locator_Css}", "button.slide-btn.scroll-rightbtn[fdprocessedid='38l60j']"

    auto_visual = (f"{locator_xpath}",
                   "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'centered-in-container') and contains(@class, 'background-layer')]")
    background = (f"{locator_xpath}",
                  "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-outlinedSecondary') and text()='Run in background']")
    Video_Generation = (f"{locator_xpath}",
                        "//div[@role='alert' and contains(@class, 'Toastify__toast-body') and contains(text(), 'Video Generation is completed')] |"
                        "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-text_2xl') and contains(text(), 'Video generation failed!')] |"
                        "//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'font-size-4') and contains(text(), 'Video generation errored.')]"
                        )

    Video_Generation_Progress = (f"{locator_xpath}",
                                 "//div[@role='alert' and @class='Toastify__toast-body' and text()='Video generation is in progress']")
    curentPlan = (
        f"{locator_Css}", "button.MuiButton-outlined.MuiButton-outlinedPrimary.MuiButton-sizeMedium[disabled]")

    Video_Generationprogress = (f"{locator_xpath}",
                                "//p[contains(@class, 'MuiTypography-body1') and contains(@class, 'font-size-4') and contains(@class, 'grey') and contains(@class, 'mt-0') and contains(@class, 'mb-0') and contains(@class, 'css-117rfk8') and contains(text(), 'Generating video.')]")

    transition = f"{locator_xpath}", "//div[@id='AllScene_1_1']//*[name()='svg']"
    transition_applied = f"{locator_xpath}", "//div[contains(@class, 'transition-wipeup') and contains(@class, 'MuiBox-root')]"

    # Layer
    addLayer = (f"{locator_xpath}", "(//div[@aria-label='Add as layer'])[2]")
    video = (f"{locator_xpath}", "(//button[contains(@class, 'MuiButton-textPrimary')])[2]")
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

    # Element apply
    element_apply = (
        f"{locator_xpath}", "(//div[contains(@class, 'element-svg-shapes') and contains(@class, 'MuiBox-root')])[1]")

    copyallscene = (
        f"{locator_xpath}", "//button[@aria-label='Copy to all scenes']")

    copyscene_text = (f"{locator_xpath}", "//p[contains(text(), 'Element copied to all scenes.')]")

    color = (f"{locator_xpath}", "svg[xmlns='http://www.w3.org/2000/svg'][width='16'][height='15']")
    colorSel = (f"{locator_xpath}", "(//div[contains(@class, 'ColorCircle') and contains(@class, 'MuiBox-root')])[4]")

    scene1 = (f"{locator_xpath}",
              "(//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-regular_xs') and text()='Scene 1'])[1]")

    video_generate = (f"{locator_xpath}", "(//h5[@class = 'vertical-point-value'])[3]")
    Plan_card = (By.CLASS_NAME, "vertical-point MuiBox-root css-0")


class MyProjectLocators:
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    MyProject_Page_TITLE = "Pictory.AI - Home of AI Video Editing Technology"

    Project = (f"{locator_xpath}", "//span[text()='My projects']")

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
    Search = (f"{locator_Id}", "searchValue")
    Delete = (f"{locator_xpath}", "//button[text()='Delete']")
    MyProject = f"{locator_xpath}", "//span[text()='My projects']"
    createProject = f"{locator_xpath}", "//button[text() = 'Create project']"

    branding_select = (f"{locator_xpath}",
                       "//span[contains(@class,'MuiTypography-root MuiTypography-text_sm')][normalize-space()='brand_template']")
    createfolder = f"{locator_xpath}", "//button[text() = 'Create folder']"
    folder_name = (f"{locator_Css}", "input[placeholder='Type here...']")
    video_MoveTo = (f"{locator_Css}", "svg[data-testid='DriveFileMoveOutlinedIcon']")
    createbtn = f"{locator_xpath}", "//button[text() = 'Create']"
    Import_location = f"{locator_xpath}", "//div[@aria-label='Import projects']"


class ArticleToVideoLocators:
    Proceed_buton = (f"{locator_xpath}",
                     "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='URL to video']")
    generate_vid = (f"{locator_Id}", "articleToVideoBtn")

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

    MyBranding = f"{locator_xpath}", "//span[text()='Brand kits' or text()='Brand Kits']"

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
    color_name = (f"{locator_Id}",
                  f"idDlgCreateBrandOpenColorPicker")
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
    Intro = (f"{locator_xpath}", "//button[contains(@class, 'keyword-button') and .//span[contains(text(), 'intro')]]")
    video = (f"{locator_xpath}", "(//video)[2]")
    Add = (f"{locator_xpath}", '(//div[@aria-label="Add to brand"])[1]')

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
    Proceed_buton = (f"{locator_xpath}",
                     "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-normal_sm_7') and text()='AI video editor']")
    name = (f"{locator_Css}", "input[placeholder='Enter your video name']")
    content = (f"{locator_Css}", "p[data-placeholder='Start typing here, or paste your script using ctrl+v']")

    youtube = (By.XPATH, "//input[@placeholder='https://']")
    # youtube = (By.ID, "mui-12")
    generate_button = (By.ID, "btnGenerate")
    Proceed_video = (f"{locator_xpath}", "//button[normalize-space()='Proceed']")
    textInput_loader = (f"{locator_xpath}", "//span[@role='progressbar']//*[name()='svg']")
    Upload_video = (f"{locator_xpath}", "//button[contains(@class, 'MuiButtonBase-root') and text()='Upload']")
    LOGO_VISIBLE = (f"{locator_xpath}", "//img[@title='Pictory']")
    # progress = (f"{locator_xpath}", "//div[@id='dynamic']")
    progress = (f"{locator_xpath}",
                "//h1[contains(@class, 'font-size-2') and contains(@class, 'bold') and contains(@class, 'sortof-black') and contains(text(), 'Transcription is in progress.')]")
    project = (f"{locator_Css}", "input.MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputSizeSmall")
    speak = (f"{locator_xpath}", "//input[@type='checkbox' and contains(@class, 'MuiSwitch-input')]")
    generate_vid = (f"{locator_xpath}", "//button[span[text()='Generate video']]")
    edit_board = (f"{locator_xpath}", "//button[span[text()='Edit in Storyboard']]")

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
    playvid = (f"{locator_xpath}", "//*[@data-testid='PlayCircleOutlineIcon']")
    pausevid = (f"{locator_xpath}", "//*[@data-testid='PauseCircleOutlineIcon']")
    defaultbrand = (
        f"{locator_xpath}",
        f"//span[contains(@class, '{class_name.get('root')}') and contains(@class, '{class_name.get('text')}') and contains(text(), 'brand01')]")
    branding_select = (f"{locator_xpath}",
                       f"//span[contains(@class,'{class_name.get('root')} {class_name.get('text')}')][normalize-space()='brand']")
    transcription = (f"{locator_xpath}", "//div[@id='p_0']/p[not(preceding-sibling::p[@id='p_0'])]")
    video_upl = (f"{locator_xpath}", "//input[@type='file' and @accept='.ogg,.mp4,.webm,.mov,.mp3,.wav']")

    paras = (f"{locator_xpath}", "//*[@id='orignalArticleDiv']/div[2]")
    autohighlight = (
        f"{locator_xpath}", "//p[contains(@class, 'MuiTypography-root') and contains(text(), 'Auto highlight')]")

    download_highlight = (f"{locator_xpath}", "//button[text()='Download highlights video']")
    download_highlights_video = (f"{locator_xpath}", "//span[text()='Download highlights video']")
    chkbox = (f"{locator_xpath}", "(//div[@class='highlights-row']//input[@type='checkbox'])[1]")
    video_clip = (f"{locator_xpath}",
                  "//button[@type='button' and @title='Download video clips for selected highlights' and contains(@class, 'btn') and contains(@class, 'btn-default')]")
    edit_highlight = (f"{locator_xpath}", "//span[text()='Edit text']")
    chkbox1 = (f"{locator_xpath}", "(//div[@class='highlights-row']//input[@type='checkbox'])[2]")
    unhighlight_buton = (f"{locator_xpath}",
                         "//button[@type='button' and @title='Unhighlight selected sentences' and contains(@class, 'btn') and contains(@class, 'btn-default')]")

    CustomizeVideo = (f"{locator_xpath}",
                      "//a[contains(@class, 'btn btn-submit mr-2 highlightVideoHover')]")
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
        f"{locator_xpath}", "//p[contains(text(), '9:16 Portrait')]")
    porTrait = (f"{locator_xpath}", "//span[contains(text(), 'Portrait')]")
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
    createfolder = (f"{locator_Id}", "idBtnCreateFolder")
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
