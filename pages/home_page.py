from selenium.webdriver.common.by import By

from config.config import Config
from pages.base_page import BasePage


class HomePage(BasePage):
    WERE_HIRING_LINK = (By.XPATH, "//a[contains(., \"We're hiring\")]")

    def open(self):
        self.navigate_to(Config.BASE_URL)
        self.accept_cookies()
        return self

    def is_homepage(self):
        return "Insider One" in self.driver.title

    def click_were_hiring(self):
        element = self.find_clickable(self.WERE_HIRING_LINK)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)
