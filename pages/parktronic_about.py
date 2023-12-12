import time

from base.base_class import Base


class Product_selection(Base):
    url = 'https://www.exist.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
    catalog_button = '[class*=" mainmenu-list__button-ddl--catalogs"]'
    city = '[href="javascript:void(0)"]'
    motor_oil = '[title="Выбор моторных масел по параметрам"]'
    filter_o = '[class="h"]'
    oil_alpine = '''[onclick="_history.Add(event, '1_-10=2078');"]'''
    viscosity_5w_40 = '''[onclick="_history.Add(event, '1_6=2103');"]'''
    api_cl = '''[onclick="_history.Add(event, '1_2131=3511');"]'''
    oil_alpine_0100161 = '[class="img"]'
    window_alpine_0100161 = '#fancybox-outer'
    name_oil_motors = '#ajaxupdatepanel > h1'

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

    def test_oil(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.find_element(self.city).click()
        self.find_element(self.catalog_button).click()
        self.find_element(self.motor_oil).click()
        assert self.find_element(self.name_oil_motors).text == "Масла моторные", "Вкладка не открылась"
        filter_brend = self.find_elements(self.filter_o)[1]
        filter_brend.click()
        self.find_element(self.oil_alpine).click()
        time.sleep(3)
        filter_composition = self.find_elements(self.filter_o)[2]
        filter_composition.click()
        self.find_element(self.viscosity_5w_40).click()
        time.sleep(3)
        filter_api = self.find_elements(self.filter_o)[5]
        filter_api.click()
        self.find_element(self.api_cl).click()
        time.sleep(3)
        self.find_element(self.oil_alpine_0100161).click()
        time.sleep(3)
        assert self.find_element(self.window_alpine_0100161), "окно не найдено"
        time.sleep(10)


