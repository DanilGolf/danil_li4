from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Product_selection(Base):
    url = 'https://www.inmotionhosting.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    dedicated_servers = '//*[@id="navbarNavDropdown"]/ul[1]/li[4]/a'
    aspire_select = '//button[@data-term="12"]'

    def get_dedicated_servers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dedicated_servers)))

    # def get_password(self):
    # return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_aspire_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aspire_select)))

    def click_aspire_select(self):
        self.get_aspire_select().click()

    def click_dedicated_servers(self):
        self.get_dedicated_servers().click()
        # print("click login_button")

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_dedicated_servers()
        self.click_aspire_select()
