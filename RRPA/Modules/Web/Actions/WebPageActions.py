from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from RRPA.AppData.Configs.WebDriverConfig import WEB_DRIVER_PATH


class WebPageActionizer:

    @staticmethod
    def open_page(driver: webdriver.Chrome, url):
        driver.switch_to.new_window()
        driver.get(url)
        return driver.current_window_handle

    @staticmethod
    def close_page(driver: webdriver.Chrome, handle):
        driver.switch_to.window(handle)
        driver.close()

    @staticmethod
    def scan_for_objects(driver: webdriver.Chrome, page, object_type):
        driver.switch_to.window(page)
        elements = driver.find_elements(By.TAG_NAME, object_type)
        return elements
