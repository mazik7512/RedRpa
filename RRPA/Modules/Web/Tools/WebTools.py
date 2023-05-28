from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from RRPA.AppData.Configs.WebDriverConfig import WEB_DRIVER_PATH
from RRPA.Modules.Core.Abstract.Web.Tools.WebTools import AbstractWebTools
from RRPA.Modules.Web.Tools.WebPageManager import STDWebPageManager


class STDWebTools(AbstractWebTools):

    _service = Service(executable_path=WEB_DRIVER_PATH)
    _driver = None
    _actions = None
    _inited = False
    #_driver = webdriver.Chrome(service=_service)
    #_actions = ActionChains(_driver)

    @staticmethod
    def _init_browser():
        if not STDWebTools._inited:
            STDWebTools._driver = webdriver.Chrome(service=STDWebTools._service)
            STDWebTools._actions = ActionChains(STDWebTools._driver)
            STDWebTools._inited = True

    @staticmethod
    def get_tools_name():
        return STDWebTools.__name__

    @staticmethod
    def get_tools_import_path():
        return STDWebTools.__module__

    @staticmethod
    def create_web_page_manager(url, wp_name) -> STDWebPageManager:
        STDWebTools._init_browser()
        return STDWebPageManager(url, wp_name, STDWebTools._driver, STDWebTools._actions)

    @staticmethod
    def get_icon(web_page):
        pass

