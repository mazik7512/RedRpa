from RRPA.Modules.Core.Abstract.Web.Tools.WebPageManager import AbstractWebPageManager
from RRPA.Modules.Web.Tools.WebPage import STDWebPage
from RRPA.Modules.Web.Actions.WebPageActions import WebPageActionizer
from RRPA.Modules.Web.Actions.ObjectActions import WebObjectActionizer
from RRPA.Modules.Web.Tools.WebObjects.Button import STDWebButton
from RRPA.Modules.Web.Tools.WebObjects.InputField import STDWebInputField
from RRPA.Modules.Web.Tools.WebObjects.Link import STDWebLink


class STDWebPageManager(AbstractWebPageManager):

    def __init__(self, web_url, web_name, driver, actions):
        self._w_page = STDWebPage(web_url, web_name)
        self._driver = driver
        self._objects = []
        self._actions = actions

    def open(self):
        handle = WebPageActionizer.open_page(self._driver, self._w_page.get_page())
        self._w_page.set_page_handle(handle)

    def close(self):
        WebPageActionizer.close_page(self._driver, self._w_page.get_page_handle())
        self._w_page.set_page_handle(None)

    def object_action(self, web_object, web_action, *params):
        action = getattr(WebObjectActionizer, web_action)
        action(web_object, *params)

    def scan_for_objects(self):
        buttons = WebPageActionizer.scan_for_objects(self._driver, self._w_page.get_page_handle(), "button")
        links = WebPageActionizer.scan_for_objects(self._driver, self._w_page.get_page_handle(), "link")
        inputs = WebPageActionizer.scan_for_objects(self._driver, self._w_page.get_page_handle(), "input")
        self._add_objects_by_type(buttons, type(STDWebButton))
        self._add_objects_by_type(links, type(STDWebLink))
        self._add_objects_by_type(inputs, type(STDWebInputField))

    def _add_objects_by_type(self, objects, obj_type):
        for obj in objects:
            self._objects.append(obj_type(self._w_page, obj, self._actions))

