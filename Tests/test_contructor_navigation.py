import pytest
from urls import *
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_navigation_to_sauce(driver):
    driver.get(url_main_page)
    driver.find_element(*TestLocators.constructor_sauce_button_locator).click()
    assert WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'current')]/span[text()='Соусы']")))


def test_navigation_to_fillings(driver):
    driver.get(url_main_page)
    driver.find_element(*TestLocators.constructor_fillings_button_locator).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'current')]/span[text()='Начинки']")))


def test_navigation_to_buns(driver):
    driver.get(url_main_page)
    driver.find_element(*TestLocators.constructor_fillings_button_locator).click()
    driver.find_element(*TestLocators.constructor_buns_button_locator).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'current')]/span[text()='Булки']")))
