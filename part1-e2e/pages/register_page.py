from playwright.sync_api import Page

from pages.base_page import BasePage


class RegisterPage(BasePage):
    path = "/index.php?rt=account/create"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name = page.locator("#AccountFrm_firstname")
        self.last_name = page.locator("#AccountFrm_lastname")
        self.email = page.locator("#AccountFrm_email")
        self.address = page.locator("#AccountFrm_address_1")
        self.city = page.locator("#AccountFrm_city")
        self.country = page.locator("#AccountFrm_country_id")
        self.zone = page.locator("#AccountFrm_zone_id")
        self.postcode = page.locator("#AccountFrm_postcode")
        self.login_name = page.locator("#AccountFrm_loginname")
        self.password = page.locator("#AccountFrm_password")
        self.confirm = page.locator("#AccountFrm_confirm")
        self.agree = page.locator("#AccountFrm_agree")
        self.continue_btn = page.locator("#AccountFrm button[title='Continue']")

    def register(self, customer: dict[str, str]) -> None:
        self.first_name.fill(customer["first_name"])
        self.last_name.fill(customer["last_name"])
        self.email.fill(customer["email"])
        self.address.fill(customer["address"])
        self.city.fill(customer["city"])
        self.country.select_option(label=customer["country"])
        # zones are reloaded over ajax after the country changes, wait for the one we want
        self.zone.locator("option", has_text=customer["zone"]).wait_for(state="attached")
        self.zone.select_option(label=customer["zone"])
        self.postcode.fill(customer["postcode"])
        self.login_name.fill(customer["login_name"])
        self.password.fill(customer["password"])
        self.confirm.fill(customer["password"])
        self.agree.check()
        self.continue_btn.click()
