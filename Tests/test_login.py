import pytest
from locators import *
from urls import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_page(driver):
    driver.get(url_login)
    driver.find_element(*TestLocators.input_email_login_page_locator).send_keys("evgeniy_taranenko_5@ya.ru")
    driver.find_element(*TestLocators.input_password_login_page_locator).send_keys("123456")
    driver.find_element(*TestLocators.login_page_button_locator).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.make_order_button_locator))


def test_login_main_page(driver):
    driver.get(url_main_page)
    driver.find_element(*TestLocators.login_main_page_button_locator).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.input_email_login_page_locator)).send_keys("evgeniy_taranenko_5@ya.ru")
    driver.find_element(*TestLocators.input_password_login_page_locator).send_keys("123456")
    driver.find_element(*TestLocators.login_page_button_locator).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.make_order_button_locator))


def test_login_registration_page(driver):
    driver.get(url_register)
    driver.find_element(*TestLocators.login_button_locator).click()
    driver.find_element(*TestLocators.input_email_login_page_locator).send_keys("evgeniy_taranenko_5@ya.ru")
    driver.find_element(*TestLocators.input_password_login_page_locator).send_keys("123456")
    driver.find_element(*TestLocators.login_page_button_locator).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.make_order_button_locator))


def test_login_forgot_password_page(driver):
    driver.get(url_forgot_password_page)
    driver.find_element(*TestLocators.login_button_locator).click()
    driver.find_element(*TestLocators.input_email_login_page_locator).send_keys("evgeniy_taranenko_5@ya.ru")
    driver.find_element(*TestLocators.input_password_login_page_locator).send_keys("123456")
    driver.find_element(*TestLocators.login_page_button_locator).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.make_order_button_locator))
