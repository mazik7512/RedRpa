from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from RRPA.AppData.Configs.WebDriverConfig import WEB_DRIVER_PATH


class WebObjectActionizer:

    _service = Service(executable_path=WEB_DRIVER_PATH)
    _driver = webdriver.Chrome(service=_service)
    _actions = ActionChains(_driver)

    @staticmethod
    def _find_element(element_text):
        return WebObjectActionizer._driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(object_text))

    @staticmethod
    def click(object_text):

        elem = WebObjectActionizer._find_element(object_text)
        elem.click()

    @staticmethod
    def double_click(object_text):
        elem = WebObjectActionizer._find_element(object_text)
        elem.click()
        elem.click()

    @staticmethod
    def r_click(object_text):
        elem = WebObjectActionizer._find_element(object_text)
