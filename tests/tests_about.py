import time

from selenium import webdriver
from pages.parktronic_about import Product_selection


def test_filter():
    driver = webdriver.Chrome()
    ps = Product_selection(driver)
    ps.check_web()
    driver.quit()
