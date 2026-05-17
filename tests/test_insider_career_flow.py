import time

from config.config import Config
from pages.career_page import CareerPage
from pages.home_page import HomePage
from pages.quality_assurance_page import QualityAssurancePage


class TestInsiderCareerFlow:
    def test_insider_career_flow(self, driver):
        home = HomePage(driver)
        home.open()
        assert home.is_homepage(), "Ana sayfa doğrulanamadı — title 'Insider One' içermiyor"

        home.click_were_hiring()
        career = CareerPage(driver)
        assert career.is_career_page(), "Career sayfasına yönlendirilmedi — URL 'careers' içermiyor"
        assert career.has_explore_open_roles_button(), "'Explore open roles' butonu bulunamadı"

        career.click_explore_open_roles()
        career.click_software_development_positions()

        qa_page = QualityAssurancePage(driver)
        qa_page.filter_by_location(Config.FILTER_LOCATION)
        qa_page.filter_by_team(Config.FILTER_TEAM)

        jobs = qa_page.verify_all_jobs_match(
            expected_team_keyword="Quality Assurance",
            expected_location="Istanbul",
        )
        assert len(jobs) > 0, "Filtreleme sonrası hiç ilan bulunamadı"

        qa_page.click_apply_first_job()
        assert "lever.co/insiderone/" in driver.current_url, (
            f"Lever sayfasına yönlendirilmedi — mevcut URL: {driver.current_url}"
        )
        time.sleep(4)
