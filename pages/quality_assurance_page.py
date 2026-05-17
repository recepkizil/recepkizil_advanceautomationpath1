import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

FILTER_LOCATION_INDEX = 1
FILTER_TEAM_INDEX = 2


class QualityAssurancePage(BasePage):
    FILTER_WRAPPERS = (By.CSS_SELECTOR, ".filter-button-wrapper")
    JOB_POSTINGS = (By.CSS_SELECTOR, ".posting")
    JOB_TITLE = (By.CSS_SELECTOR, "h5")
    JOB_LOCATION = (By.CSS_SELECTOR, ".sort-by-location")
    JOB_APPLY_BTN = (By.CSS_SELECTOR, "a.posting-btn-submit")

    def _select_filter(self, filter_index, option_text):
        wrappers = self.driver.find_elements(*self.FILTER_WRAPPERS)
        btn = wrappers[filter_index].find_element(By.CSS_SELECTOR, ".filter-button")
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(0.5)
        popup = wrappers[filter_index].find_element(By.CSS_SELECTOR, ".filter-popup")
        option = popup.find_element(By.XPATH, f".//*[text()='{option_text}']")
        self.driver.execute_script("arguments[0].click();", option)
        time.sleep(2)

    def filter_by_location(self, location):
        self._select_filter(FILTER_LOCATION_INDEX, location)

    def filter_by_team(self, team):
        self._select_filter(FILTER_TEAM_INDEX, team)

    def get_job_listings(self):
        self.wait.until(EC.presence_of_all_elements_located(self.JOB_POSTINGS))
        return self.driver.find_elements(*self.JOB_POSTINGS)

    def verify_all_jobs_match(self, expected_team_keyword, expected_location):
        jobs = self.get_job_listings()
        assert len(jobs) > 0, "No job listings found after applying filters"
        for job in jobs:
            title = job.find_element(*self.JOB_TITLE).text.strip()
            location = job.find_element(*self.JOB_LOCATION).text.strip()
            assert (expected_team_keyword.lower() in title.lower() or "qa" in title.lower()), (
                f"Expected '{expected_team_keyword}' or 'QA' in title but got: '{title}'"
            )
            assert expected_location.lower() in location.lower(), (
                f"Expected '{expected_location}' in location but got: '{location}'"
            )
        return jobs

    def click_apply_first_job(self):
        jobs = self.get_job_listings()
        self.scroll_to_element(jobs[0])
        btn = jobs[0].find_element(*self.JOB_APPLY_BTN)
        href = btn.get_attribute("href")
        btn.click()
        return href
