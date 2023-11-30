import time

from selenium import webdriver


from pages.product_selection import Product_selection
from pages.purchase_of_goods import Purchase_of_goods


def test_filter():
    driver = webdriver.Chrome()

    print("Start Test")

    ps = Product_selection(driver)
    ps.authorization()
    time.sleep(10)

    fp = Purchase_of_goods(driver)
    fp.select_filter()

    print("Finish Test")
    time.sleep(10)
    driver.quit()
