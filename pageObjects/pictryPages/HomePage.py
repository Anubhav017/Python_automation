import traceback

from selenium.common import StaleElementReferenceException

from base.BasePage import BasePage
from locator.locators import HomeLocators


class HomePage(BasePage):

    def __init__(self, driver):  # constructor of page class
        super().__init__(driver)

    def is_logo_exist(self):  # This is used to get Logo of login Page
        if self.is_loader_invisible(*HomeLocators.loader):
            return self.is_visible(*HomeLocators.LOGO_VISIBLE)

    def get_video_text(self, by_locname, locator):  # This is used to get element text of login Page
        if self.is_visible(by_locname, locator):
            return self.do_element_text(by_locname, locator)

    def get_HomePage_url(self, current_url):  # This is used to get Login Url of login Page
        return self.get_url(current_url)

    def ScrollclickOperation(self, by_locname, locator):  # This is used to perform scroll and click to button
        try:
            if self.is_visible(by_locname, locator):
                return self.scrollToclick_element(by_locname, locator)
        except StaleElementReferenceException:
            print(traceback.format_exc())

    def get_elements(self, by_locname, locator):  # This is used to get element text of login Page
        if self.is_visible_DOM(by_locname, locator):
            return self.do_elements_DOM(by_locname, locator)

    def get_element_text(self, by_locname, locator):  # This is used to get element text of login Page
        if self.is_loader_invisible(*HomeLocators.loader):
            print("loader is not visible")
            return self.do_element_text(by_locname, locator)

    def get_element_DOM(self, by_locname, locator):  # This is used to get element text of login Page
        if self.is_visible_DOM(by_locname, locator):
            return self.do_element_DOM(by_locname, locator)

    def get_HomePage_title(self, title):  # This is used to get Login Title of login Page
        return self.get_title(title)
