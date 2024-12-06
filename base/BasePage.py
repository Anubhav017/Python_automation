import time
from pathlib import Path

from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from locator.locators import SubscriptionLocators


class BasePage:
    ROOT_PATH = str(Path(__file__).parent.parent)

    def __init__(self, driver):  # constructor of Base class
        self.driver = driver

    '''
    @allure.step("Opening main page")
    def open(self):
        self.driver.open()

    
    '''

    def do_click(self, by_locname, locator):  # This function will Perform click of the element
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((by_locname, locator))).click()

    def do_clear(self, by_locname, locator):
        element = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((by_locname, locator)))
        element.clear()

    def do_send_keys(self, by_locname, locator, text):  # This function will add text in the field of the element
        WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located((by_locname, locator))).send_keys(text)

    def do_elements(self, by_locname, locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_all_elements_located((by_locname, locator)))
        elements = self.driver.find_elements(by_locname, locator)
        return elements

    def is_visible(self, by_locname, locator):  # This function will wait until the element is visible
        element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located((by_locname, locator)))
        return bool(element)

    def do_elements_DOM(self, by_locname, locator):
        WebDriverWait(self.driver, 30).until(ec.presence_of_all_elements_located((by_locname, locator)))
        elements = self.driver.find_elements(by_locname, locator)
        return elements

    def get_title(self, title):  # This is mainly used to get the title of the page
        WebDriverWait(self.driver, 30).until(ec.title_contains(title))
        return self.driver.title

    def is_loader_invisible(self, by_locname, locator):  # This function will wait until the element is visible
        element = WebDriverWait(self.driver, 284, poll_frequency=2).until(ec.invisibility_of_element_located((by_locname, locator)))
        element = WebDriverWait(self.driver, 230, poll_frequency=2).until(ec.invisibility_of_element_located((by_locname, locator)))
        return bool(element)

    def do_element_Page_Load(self):
        # Wait for the page to load completely
        wait = WebDriverWait(self.driver, 30)
        element_loaded = wait.until(
            lambda driver: self.driver.execute_script("return document.readyState") == "complete")
        return bool(element_loaded)

    def do_element_loader(self, by_locname, locator):
        loader = WebDriverWait(self.driver, 60).until(ec.invisibility_of_element_located((by_locname, locator)))
        return loader

    @staticmethod
    def do_scrollTo_bottom_Click(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()

    def do_element_text(self, by_locname, locator):  # This is mainly return the text of the element
        element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located((by_locname, locator)))
        return element.text

    def do_element(self, by_locname, locator):  # This is mainly return the text of the element
        WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located((by_locname, locator)))
        element = self.driver.find_element(by_locname, locator)
        return element

    def is_visible_DOM(self, by_locname, locator):  # This function will wait until the element is visible
        element = WebDriverWait(self.driver, 120).until(ec.presence_of_element_located((by_locname, locator)))
        return bool(element)

    def get_webelement(self, by_locname, locator):  # This is mainly return the text of the element
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((by_locname, locator)))
        return bool(element)

    def do_element_DOM(self, by_locname, locator):  # This is mainly return the text of the element
        WebDriverWait(self.driver, 114).until(ec.presence_of_element_located((by_locname, locator)))
        element = self.driver.find_element(by_locname, locator)
        return element

    def do_action_scrollTo_Click_offset(self, by_locname,
                                        locator):  # This is mainly used to Perform hover and click operation on element
        element_to_click = self.driver.find_element(by_locname, locator)
        ActionChains(self.driver).move_to_element_with_offset(element_to_click, 90, 50).click().perform()

    def is_clickable(self, by_locname, locator):  # This function will Perform click when the element will be clickable
        element = WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable((by_locname, locator)))
        element.click()

    def do_Video_Generation_element(self, by_locname, locator):  # This is mainly return the text of the element
        WebDriverWait(self.driver, 310, poll_frequency=1).until(ec.visibility_of_element_located((by_locname, locator)))
        element = self.driver.find_element(by_locname, locator)
        return element if element else None

    def get_url(self, Current_url):  # This is mainly used to get the URL of the page
        WebDriverWait(self.driver, 30).until(ec.url_contains(Current_url))
        return self.driver.current_url

    def select_dropdown_ByvisibleText(self, by_locname, locator, VisibleText):  # This is mainly used to provide visible Text in the field
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((by_locname, locator)))
        drop = Select(element)
        drop.select_by_visible_text(VisibleText)

    def select_dropdown_Byvalue(self, by_locator, value):  # This is mainly used to provide value in the field
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        drop = Select(element)
        drop.select_by_value(value)

    def select_dropdown_Byindex(self, by_locator, index):  # This is mainly used to provide index in the field
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        drop = Select(element)
        drop.select_by_index(index)

    def do_Backgroud_color(self, by_locator):  # This is mainly used to get background color of element
        element_clr = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        background_clr = element_clr.value_of_css_property("background-color")
        hex_background_clr = Color.from_string(background_clr).hex

        return hex_background_clr

    def do_element_color(self, by_locname, locator):  # This is mainly used to get color of element
        element_clr = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((by_locname, locator)))
        color = element_clr.value_of_css_property("color")
        hex_color = Color.from_string(color).hex
        return hex_color

    def scrollToview_element(self, by_locname, locator):  # This is mainly used scroll and view element
        element = WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((by_locname, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            element.click()

    def scrollToviewclick_element(self, by_locname, locator):  # This is mainly used scroll and view element
        element = WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((by_locname, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            time.sleep(10)
            element.click()

    def scrollclick_element_DOM(self, by_locname, locator):  # This is mainly used scroll and click element
        try:
            WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((by_locname, locator)))
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((by_locname, locator))))

            # self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            print(f"Error: {e}")

    def scrollToview_footer_element(self, by_locname, locator):  # This is mainly used scroll and view element
        element = WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((by_locname, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def scrollToclick_element(self, by_locname, locator):  # This is mainly used scroll and click element
        try:
            WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((by_locname, locator)))
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((by_locname, locator))))

            # self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            print(f"Error: {e}")

    def get_switchToelement(self):  # This is used to Switch to frames
        WebDriverWait(self.driver, 30).until(ec.frame_to_be_available_and_switch_to_it(
            WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "iframe")))))

    def add_billingaddress(self, Address, City,
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
                if self.is_visible(*SubscriptionLocators.payment):
                    self.scrollToclick_element_DOM(*SubscriptionLocators.payment)
                    self.driver.switch_to.default_content()

                """
                if self.is_visible(*SubscriptionLocators.payment):
                    self.scrollToclick_element_DOM(*SubscriptionLocators.payment)
                    self.driver.switch_to.default_content()
                
                """
        except StaleElementReferenceException:
            print("exception handled")

    def scrollToclick_element_DOM(self, by_locname, locator):  # This is mainly used scroll and click element
        try:

            element = WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((by_locname, locator)))
            self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            print(f"Error: {e}")

    def action_hover_layer(self, value):
        actions = ActionChains(self.driver)
        actions.move_to_element(value).perform()

    def action_hover_Onelement(self, value):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(value, 90, 50).perform()

    def do_action_scrollTo_Click(self, by_locname, locator):  # This is mainly used to Perform hover and click operation on element
        element_to_click = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((by_locname, locator)))
        # element_to_click = self.driver.find_element(by_locname, locator)
        ActionChains(self.driver).move_to_element(element_to_click).click().perform()

    def list_elements(self, by_locator):  # This is mainly used to get list of element
        elements = []
        elements = self.driver.find_elements(by_locator)

        for element in elements:
            print(element.text)
            if elements.text == 'Buy now':
                elements.click()
                break
