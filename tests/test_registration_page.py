import pytest
from generate import *
from locators import *
from urls import *
from data import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationPage:
    def test_registration_success(self, driver):
        driver.get(url_register)
        driver.find_element(*TestLocators.input_registration_name_locator).send_keys(name)
        driver.find_element(*TestLocators.input_registration_login_locator).send_keys(generate_login())
        driver.find_element(*TestLocators.input_registration_password_locator).send_keys(generate_password(6))
        driver.find_element(*TestLocators.registration_button_locator).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.header_login_page_locator))

    def test_registration_fail(self, driver):
        driver.get(url_register)
        driver.find_element(*TestLocators.input_registration_name_locator).send_keys(name)
        driver.find_element(*TestLocators.input_registration_login_locator).send_keys(generate_login())
        driver.find_element(*TestLocators.input_registration_password_locator).send_keys(generate_password(random.randint(1, 5)))
        driver.find_element(*TestLocators.registration_button_locator).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.registration_error_text_locator))
