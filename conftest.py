import pytest
from urls import *
from selenium import webdriver
from locators import *


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def account_auth():
    driver = webdriver.Chrome()
    driver.get(url_login)
    driver.find_element(*TestLocators.input_email_login_page_locator).send_keys("evgeniy_taranenko_5@ya.ru")
    driver.find_element(*TestLocators.input_password_login_page_locator).send_keys("123456")
    driver.find_element(*TestLocators.login_page_button_locator).click()
    yield driver
    driver.quit()