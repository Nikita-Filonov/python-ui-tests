import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @allure.title("Successful registration")
    def test_successful_registration(
            self,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.check_visible(email="", username="", password="")
        registration_page.registration_form.fill(
            email="user@example.com",
            username="Playwright",
            password="qwerty"
        )
        registration_page.click_registration_button()

        dashboard_page.navbar.check_visible("Playwright")
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.check_visible_scores_chart()
        dashboard_page.check_visible_courses_chart()
        dashboard_page.check_visible_students_chart()
        dashboard_page.check_visible_activities_chart()
