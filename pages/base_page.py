import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        try:
            return self.find_visible(locator).is_displayed()
        except Exception:
            return False

    def navigate_to(self, url):
        self.driver.get(url)

    def accept_cookies(self):
        try:
            btn = self.find_clickable((By.ID, "wt-cli-accept-all-btn"))
            btn.click()
            time.sleep(0.5)
        except Exception:
            pass
