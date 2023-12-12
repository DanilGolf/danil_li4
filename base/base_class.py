from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))

    def exist_element(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements.__len__() > 0:
            return True
        else:
            return False