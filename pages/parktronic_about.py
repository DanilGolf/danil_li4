from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Product_selection(Base):
    url = 'https://www.exist.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    audi_button = '[href="/Catalog/Global/Cars/Audi"]'
    rs_8_button = '[href="/Catalog/Global/Cars/Audi/24479"]'
    motor_5_2_fsi = '[href*="/Audi/24479/0C900084"]'
    catalog_of_substitutes = '[onclick*="/24479/0C900084"]'
    body_button = '[data-id="100"]'
    parktronic_sensor = '[href*="12C00000_2412"]'
    hella_search_button = '[href*="/Price/?pid=29"]'
    hella_throttle_position_sensor = '[id="_29B0FCD7_01008801b606ee890544da000100957b_392_29"]'
    personal_cabinet = '#guestForm > h3'
    personal_cabinet_window = '[class="b login"]'
    window_r_8 = '''[onclick="geturlEx('24479');return false;"]'''

    def find_element(self, element):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))

    def tests_audi(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.find_element(self.audi_button).click()
        assert self.find_element(self.window_r_8), "Окно не найдено"
        self.find_element(self.rs_8_button).click()
        self.find_element(self.motor_5_2_fsi).click()
        self.find_element(self.catalog_of_substitutes).click()
        self.find_element(self.body_button).click()
        self.find_element(self.parktronic_sensor).click()
        self.find_element(self.hella_search_button).click()
        self.find_element(self.hella_throttle_position_sensor).click()
        assert self.find_element(self.personal_cabinet_window), "Окно не открылось"
        assert self.find_element(self.personal_cabinet).text == "Личный кабинет", "Оглавление не подходит"
