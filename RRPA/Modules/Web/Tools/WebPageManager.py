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
        self._objects = {}
        self._actions = actions

    def open(self):
        handle = WebPageActionizer.open_page(self._driver, self._w_page.get_page())
        self._w_page.set_page_handle(handle)

    def close(self):
        WebPageActionizer.close_page(self._driver, self._w_page.get_page_handle())
        self._w_page.set_page_handle(None)

    def object_action(self, web_object, web_action, *params):
        action = getattr(WebObjectActionizer, web_action)
        action(self._objects[web_object], *params)

    def scan_for_objects(self):
        buttons = WebPageActionizer.scan_for_objects(self._driver, self._w_page.get_page_handle(), "button")
        links = WebPageActionizer.scan_for_objects(self._driver, self._w_page.get_page_handle(), "a")
        inputs = WebPageActionizer.scan_for_objects(self._driver, self._w_page.get_page_handle(), "input")
        self._add_buttons_objects(buttons)
        self._add_links_objects(links)
        self._add_inputs_objects(inputs)

    def _add_buttons_objects(self, objects):
        for obj in objects:
            spec_obj = STDWebButton(self._w_page, obj, self._actions)
            self._objects[WebObjectActionizer.get_attr(obj, 'value')] = spec_obj

    def _add_links_objects(self, objects):
        for obj in objects:
            spec_obj = STDWebLink(self._w_page, obj, self._actions)
            self._objects[WebObjectActionizer.get_attr(obj, 'value')] = spec_obj

    def _add_inputs_objects(self, objects):
        for obj in objects:
            spec_obj = STDWebInputField(self._w_page, obj, self._actions)
            self._objects[WebObjectActionizer.get_attr(obj, 'value')] = spec_obj
