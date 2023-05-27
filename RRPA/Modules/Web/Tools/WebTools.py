from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from RRPA.AppData.Configs.WebDriverConfig import WEB_DRIVER_PATH
from RRPA.Modules.Core.Abstract.Web.Tools.WebTools import AbstractWebTools
from RRPA.Modules.Web.Tools.WebPageManager import STDWebPageManager


class STDWebTools(AbstractWebTools):

    _service = Service(executable_path=WEB_DRIVER_PATH)
    _driver = webdriver.Chrome(service=_service)
    _actions = ActionChains(_driver)

    @staticmethod
    def get_tools_name():
        return STDWebTools.__name__

    @staticmethod
    def get_tools_import_path():
        return STDWebTools.__module__

    @staticmethod
    def create_web_page_manager(url, wp_name):
        return STDWebPageManager(url, wp_name, STDWebTools._driver, STDWebTools._actions)

    @staticmethod
    def get_icon(web_page):
        pass

    @staticmethod
    def find_web_page(web_page_name):
        pass

    @staticmethod
    def get_pages():
        pass

