from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.base_url: str = "https://discord.com"

    @property
    def path(self) -> str:
        raise NotImplementedError

    def open(self) -> None:
        """Navigates to a specific page."""
        safe_path = self.path.strip("/")
        url: str = f"{self.base_url}/{safe_path}"
        self.driver.get(url)

    def wait_for_element(
        self, locator: Tuple[str, str], timeout: int = 20
    ) -> WebElement:
        """Waits for an element to be present on the page and returns it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_element(self, locator: Tuple[str, str]) -> WebElement | None:
        """Tries to find an element on the page. Returns None if not found."""
        try:
            return self.driver.find_element(*locator)
        except Exception:
            return None

    def find_elements(self, locator: Tuple[str, str]) -> list[WebElement]:
        """Tries to find multiple elements on the page. Returns an empty list if not found."""
        return self.driver.find_elements(*locator)

    def click(self, locator: Tuple[str, str]) -> None:
        """Clicks on an element."""
        element = self.wait_for_element(locator)
        element.click()


    def is_displayed(self, locator: Tuple[str, str]) -> bool:
        """Checks if an element is displayed on the page."""
        element = self.find_element(locator)
        return element.is_displayed() if element else False

    def get_current_url(self) -> str:
        """Returns the current URL of the page."""
        return self.driver.current_url
