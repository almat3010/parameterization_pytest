import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_diff_language(browser):
    browser.get(link)
    add_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket) > 0