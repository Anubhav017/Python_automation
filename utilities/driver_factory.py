import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from helpers.webdriver_listener import WebDriverListener
from helpers.webdriver_extended import WebDriverExtended


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if os.name == 'nt':  # Windows
            chrome_driver_path = "./utilities/driver/chromedriver.exe"
        elif os.name == 'posix':  # Linux/Unix
            chrome_driver_path = ChromeDriverManager().install()
        else:
            raise OSError("Unsupported operating system")

        if config["browser"] == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)  # For debugging purposes
            chrome_options.add_argument("--window-size=1920,1080")  # Set screen size
            chrome_options.add_argument("start-maximized")
            chrome_options.add_argument("enable-features=NetworkServiceInProcess")
            chrome_options.add_argument(
                '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
            chrome_options.add_argument("--disable-features=SameSiteByDefaultCookies")
            chrome_options.add_argument("--disable-features=CookiesWithoutSameSiteMustBeSecure")
            chrome_options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")

            if config["headless_mode"]:
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--headless")

            driver = WebDriverExtended(
                webdriver.Chrome(service=ChromeService(chrome_driver_path), options=chrome_options),
                WebDriverListener(),
            )
            return driver

        elif config["browser"] == "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.use_chromium = True  # Use Chromium-based Edge
            edge_options.add_argument("--window-size=1920,1080")  # Consistent format with Chrome
            edge_options.add_argument("start-maximized")
            edge_options.add_argument("enable-features=NetworkServiceInProcess")
            edge_options.add_argument(
                '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--no-sandbox")

            if config["headless_mode"]:
                edge_options.add_argument("--headless")

            driver = WebDriverExtended(
                webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options),
                WebDriverListener(), config
            )
            return driver

        raise Exception("Provide a valid browser name in the config file")
