from selenium.webdriver.common.by import By

from config.config import Config
from pages.base_page import BasePage


class CareerPage(BasePage):
    EXPLORE_BTN = (By.XPATH, "//a[contains(@href,'open-roles')]")
    SW_DEV_POSITIONS = (By.XPATH, "//a[contains(@href,'Software%20Development') and contains(text(),'Open Position')]")

    def is_career_page(self):
        return "careers" in self.driver.current_url

    def has_explore_open_roles_button(self):
        return self.is_visible(self.EXPLORE_BTN)

    def click_explore_open_roles(self):
        self.scroll_to(self.EXPLORE_BTN)
        self.click(self.EXPLORE_BTN)

    def click_software_development_positions(self):
        self.scroll_to(self.SW_DEV_POSITIONS)
        self.click(self.SW_DEV_POSITIONS)
