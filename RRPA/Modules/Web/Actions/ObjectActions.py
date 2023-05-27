from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from RRPA.AppData.Configs.WebDriverConfig import WEB_DRIVER_PATH


class WebObjectActionizer:
    @staticmethod
    def click(actions: ActionChains, elem):
        actions.click(elem)

    @staticmethod
    def double_click(actions: ActionChains, elem):
        actions.double_click(elem)

    @staticmethod
    def click_and_hold(actions: ActionChains, elem):
        actions.click_and_hold(elem)

    @staticmethod
    def release(actions: ActionChains, elem):
        actions.release(elem)

    @staticmethod
    def move_to_element(actions: ActionChains, elem):
        actions.move_to_element(elem)

    @staticmethod
    def get_text(elem):
        return elem.text

    @staticmethod
    def input_text(elem, text):
        elem.text = text

    @staticmethod
    def get_attr(elem, attr):
        return elem.get_attribute(attr)
