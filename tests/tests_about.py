from selenium import webdriver
from pages.exist_about import Product_selection


def test_filter1():
    driver = webdriver.Chrome()
    ps = Product_selection(driver)
    ps.tests_audi()
    driver.quit()


def test_filter2():
    driver = webdriver.Chrome()
    ps = Product_selection(driver)
    ps.test_oil()
    driver.quit()
