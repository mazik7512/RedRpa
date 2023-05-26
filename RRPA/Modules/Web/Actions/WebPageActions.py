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

    @staticmethod
    def close_page(driver: webdriver.Chrome, url):
        driver.close()
