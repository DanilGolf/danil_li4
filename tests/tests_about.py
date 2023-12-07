from selenium import webdriver
from pages.parktronic_about import Product_selection


def test_filter():
    driver = webdriver.Chrome()
    ps = Product_selection(driver)
    ps.tests_audi()
    driver.quit()
