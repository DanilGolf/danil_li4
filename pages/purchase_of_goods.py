import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Purchase_of_goods(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    continue_button_1 = "//input[@id = 'sidebar-next-step']"
    choice_domain_name = '//*[@id="domain-search-section"]/div/form/div[3]/label/span'
    continue_button_2 = "//input[@id = 'sidebar-next-step']"
    billing_word = '//*[@id="new-returning-customer-section"]/form/section/div[1]/div/h2'
    total = '//*[@id="cart_items"]/div[3]/div/h3[1]/text()[3]'
    # Getters

    def get_continue_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_1)))

    def get_choice_domain_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choice_domain_name)))

    def get_continue_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_2)))

    def get_billing_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.billing_word)))

   # def get_total_test(self):
        #return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total)))

    def click_on_element(self, element):
        return element.click()

    def text_element_1(self, element):
        return element.text

    def select_filter(self):
        self.click_on_element(self.get_continue_button_1())
        self.click_on_element(self.get_choice_domain_name())
        self.click_on_element(self.get_continue_button_2())
        self.assert_word(self.get_billing_word(), 'Billing Details')
        #print(self.text_element_1(self.get_total_test()))

        time.sleep(10)

