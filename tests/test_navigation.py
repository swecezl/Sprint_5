import pytest
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestNavigation:
    def test_navigation_to_user_account_from_main_page(self, account_auth):
        account_auth.find_element(*TestLocators.user_account_header_button_locator).click()
        assert WebDriverWait(account_auth, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    def test_navigation_to_constructor_from_user_account_page(self, account_auth):
        account_auth.find_element(*TestLocators.user_account_header_button_locator).click()
        account_auth.find_element(*TestLocators.constructor_button_locator).click()
        assert WebDriverWait(account_auth, 3).until(expected_conditions.presence_of_element_located(TestLocators.header_constructor_page_locator))

    def test_navigation_logo_click_from_user_account_page(self, account_auth):
        account_auth.find_element(*TestLocators.user_account_header_button_locator).click()
        account_auth.find_element(*TestLocators.logo_locator).click()
        assert WebDriverWait(account_auth, 3).until(expected_conditions.presence_of_element_located(TestLocators.header_constructor_page_locator))
