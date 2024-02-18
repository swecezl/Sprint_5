import pytest
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_logout(self, account_auth):
        account_auth.find_element(*TestLocators.user_account_header_button_locator).click()
        WebDriverWait(account_auth, 3).until(expected_conditions.element_to_be_clickable(TestLocators.logout_button_locator))
        account_auth.find_element(*TestLocators.logout_button_locator).click()
        WebDriverWait(account_auth, 3).until(expected_conditions.visibility_of_element_located(TestLocators.header_login_page_locator))
