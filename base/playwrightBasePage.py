import os
from pathlib import Path
from playwright.sync_api import Page, Locator, BrowserContext
from playwright.sync_api import expect
from playwrighttests.conftest import logger


class PlaywrightBasePage:
    ROOT_PATH = str(Path(__file__).parent.parent)

    def __init__(self, page: Page):
        self.page = page

    def do_click(self, selector: str, timeout: int = 120000):
        self.wait_for_element(selector, timeout).click()

    def do_send_keys(self, selector: str, text: str, timeout: int = 120000):
        self.wait_for_element(selector, timeout).fill(text)

    def wait_for_element(self, selector: str, timeout: int = 120000):
        try:
            return self.page.wait_for_selector(selector, timeout=timeout)
        except TimeoutError:
            print(f"Element with selector '{selector}' not found within {timeout/1000} seconds.")
            return None

    def click_project_file(self):
        self.page.get_by_text("Projectfile").click()

    def is_enabled(self, selector: str, timeout: int = 120000) -> bool:
        try:
            expect(self.page.locator(selector)).to_be_enabled(timeout=timeout)
            return True

        except TimeoutError:
            print(f"Element with selector '{selector}' did not become enabled within {timeout} ms.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def background_click(self, selector: str, timeout: int = 120000) -> bool:
        if self.is_enabled(selector, timeout):
            try:
                self.page.locator(selector).click(timeout=timeout)
                logger.info('background clicked :')

                return True
            except TimeoutError:
                print(f"Click operation on element with selector '{selector}' timed out after {timeout} ms.")
                return False
        else:
            print(f"Element with selector '{selector}' is not enabled.")
            return False

    def is_visible(self, selector: str, timeout: int = 1200000) -> bool:
        try:
            element = self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            return element.is_visible() if element else False
        except Exception as e:
            logger.error(f"Element with selector {selector} is not visible: {e}")
            return False

    def do_clear(self, selector: str, timeout: int = 120000):
        element = self.wait_for_element(selector, timeout)
        element.fill('')

    def do_element_DOM(self, locator: str):
        self.page.wait_for_selector(locator, state='attached', timeout=642000)
        return self.page.locator(locator).first

    def do_click_text(self, selector: str, timeout: int = 120000):
        self.wait_for_element(selector, timeout).click()

    def do_elements(self, locator: str, timeout: int = 120000) -> list:
        return self.page.locator(locator).all()

    def do_hover(self, selector: str):
        element = self.wait_for_element(selector)
        element.hover()

    def do_accept_Alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        logger.info("Dialog accepted automatically.")

    def is_elementvisible(self, selector: str, timeout: int = 840000) -> bool:
        try:
            element = self.page.locator(selector)
            element.wait_for(state="attached", timeout=timeout)

            expect(element).to_be_visible(timeout=timeout)
            return True

        except Exception as e:
            logger.error(f"Error checking visibility of element with selector '{selector}': {str(e)}")
            return False

    def get_title(self, title: str, timeout: int = 120000) -> str:
        self.page.wait_for_function(f'document.title.includes("{title}")', timeout=timeout)
        return self.page.title()

    def is_loader_invisible(self, selector: str, timeout: int = 628000) -> bool:
        logger.info(f"Checking visibility of loader with selector: {selector}")
        loader = self.page.locator(selector)
        try:
            loader.wait_for(state="hidden", timeout=timeout)
            logger.info(f"Loader '{selector}' is now invisible.")
            return True
        except TimeoutError:
            logger.error(f"Loader '{selector}' is still visible after {timeout}ms.")
            return False

    def do_element_Page_Load(self, timeout: int = 120000):
        self.page.wait_for_load_state('load', timeout=timeout)
        return True

    def do_element_loader(self, selector: str, timeout: int = 120000):
        return self.page.wait_for_selector(selector, state='hidden', timeout=timeout)

    def click_apply_button(self, locator: str):
        try:
            # Waits for the element to be present in the DOM (attached) without requiring visibility
            self.page.wait_for_selector(locator, state='attached', timeout=120000)
            self.page.locator(locator).click()
        except Exception as e:
            print(f"Error: {e}")  # Handle any exceptions that occur

    def do_element_text(self, selector: str, timeout: int = 120000) -> str:
        return self.wait_for_element(selector, timeout).inner_text()

    def do_element(self, selector: str, timeout: int = 642000) -> Locator:
        element = self.page.wait_for_selector(selector, timeout=timeout)
        if element:
            element.wait_for_element_state("visible", timeout=timeout)
            element.wait_for_element_state("stable", timeout=timeout)
            return element

    def do_element_One(self, selector: str) -> Locator:
        elements = self.do_elements(selector)
        if elements:
            return elements[0]

    def get_Video_Generation_element(self, locator: str):
        element = self.page.locator(locator).first
        element.wait_for(state='visible', timeout=3620000)  # 3620 seconds timeout
        return element

    def scrollclick_element(self, selector: str, timeout: int = 120000):
        try:
            element = self.wait_for_element(selector, timeout)
            self.page.evaluate("element => element.click()", element)
        except Exception as e:
            print(f"Error: {e}")

    def select_dropdown_by_visible_text(self, selector: str, visible_text: str):
        dropdown = self.page.locator(selector)
        dropdown.select_option(label=visible_text)

    def select_dropdown_by_value(self, selector: str, value: str):
        dropdown = self.page.locator(selector)
        dropdown.select_option(value=value)

    def do_clickOperation(self, selector: str, timeout: int = 120000) -> bool:
        try:
            if self.is_elementvisible(selector):
                element = self.page.locator(selector)
                element.click()
                logger.info(f"Clicked on element with selector '{selector}'.")
                return True
        except Exception as e:
            print(f"Element with selector '{selector}' not found within the timeout period.")

    def select_dropdown_by_index(self, selector: str, index: int):
        dropdown = self.page.locator(selector)
        # Get all options in the dropdown
        options = dropdown.locator('option').all()
        if index < 0 or index >= len(options):
            raise ValueError(f"Index {index} is out of bounds for the dropdown with {len(options)} options.")
        value = options[index].get_attribute('value')
        dropdown.select_option(value=value)

    def make_element_visible(self, selector: str):
        try:
            escaped_selector = selector.replace("'", "\\'")

            js_code = f"""
                var element = document.querySelector('{escaped_selector}');
                if (element) {{
                    element.style.display = 'block';
                    element.style.opacity = '1';
                    element.style.visibility = 'visible';
                }}
            """
            self.page.evaluate(js_code)
            print(f"Attempted to make the element with selector {selector} visible.")

            if self.page.locator(selector).is_visible():
                print(f"Element with selector {selector} is now visible.")
            else:
                print(f"Element with selector {selector} is still not visible.")
        except Exception as error:
            print(f"Error making element visible: {error}")
            raise

    def get_Proceed_buton_click(self):
        try:
            proceed_button_selector = "button:has-text('Proceed')"  # Adjust this selector as needed
            proceed_button = self.page.locator(proceed_button_selector)
            expect(proceed_button).to_be_enabled(timeout=60000)
            proceed_button.click()
            print("Clicked the Proceed button.")

        except Exception as error:
            print(f"Error during file upload or clicking proceed: {error}")
            raise

    def get_uploadmp4_file(self, selector: str, file_path: str):
        try:
            absolute_path = os.path.abspath(file_path)
            if not os.path.exists(absolute_path):
                raise FileNotFoundError(f"The file {absolute_path} does not exist.")

            # Make the file input element visible
            self.make_element_visible(selector)

            # Locate the file input element and set the file
            file_input = self.page.locator(selector)
            file_input.set_input_files(absolute_path)
            print(f"File {os.path.basename(file_path)} uploaded successfully.")

            self.page.wait_for_selector(f"text={os.path.basename(file_path)}", timeout=120000)
            print(f"File {os.path.basename(file_path)} is visible in the UI.")

        except Exception as error:
            print(f"Error during file upload or clicking proceed: {error}")
            raise

    def scrollToclick_element(self, locator: str):
        element = self.do_element(locator)
        element.scroll_into_view_if_needed()  # Scroll the element into view
        element.click()  # Click the element

    def get_switchToelement(self, selector: str, timeout: int = 120000):
        self.wait_for_element(selector, timeout)
        return self.page.frame_locator(selector)

    def action_hover_Onelement(self, selector: str, timeout: int = 120000):
        element = self.wait_for_element(selector, timeout)
        self.page.mouse.move(element.bounding_box()['x'] + 90, element.bounding_box()['y'] + 50)

    def do_switch_to_window(self):
        total_pages = self.context.pages
        if len(total_pages) > 1:
            new_page = total_pages[-1]  # Switch to the most recent page
            new_page.bring_to_front()
