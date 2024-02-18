import pytest
from urls import *
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorNavigation:
    def test_navigation_to_sauce(self, driver):
        driver.get(url_main_page)
        driver.find_element(*TestLocators.constructor_sauce_button_locator).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.constructor_sauce_active_button_locator))

    def test_navigation_to_fillings(self, driver):
        driver.get(url_main_page)
        driver.find_element(*TestLocators.constructor_fillings_button_locator).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.constructor_fillings_active_button_locator))

    def test_navigation_to_buns(self, driver):
        driver.get(url_main_page)
        driver.find_element(*TestLocators.constructor_fillings_button_locator).click()
        driver.find_element(*TestLocators.constructor_buns_button_locator).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.constructor_buns_active_button_locator))
