from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from RRPA.AppData.Configs.WebDriverConfig import WEB_DRIVER_PATH


class WebObjectActionizer:
    @staticmethod
    def click(actions: ActionChains, elem):
        actions.click(elem).perform()

    @staticmethod
    def double_click(actions: ActionChains, elem):
        actions.double_click(elem).perform()

    @staticmethod
    def click_and_hold(actions: ActionChains, elem):
        actions.click_and_hold(elem).perform()

    @staticmethod
    def release(actions: ActionChains, elem):
        actions.release(elem).perform()

    @staticmethod
    def move_to_element(actions: ActionChains, elem):
        actions.move_to_element(elem).perform()

    @staticmethod
    def get_text(actions, elem):
        return elem.text

    @staticmethod
    def input_text(actions, elem, text):
        elem.text = text

    @staticmethod
    def get_attr(elem, attr):
        return elem.get_attribute(attr)
