from selenium.webdriver.remote.webelement import WebElement
from RRPA.Modules.Core.Abstract.Web.Objects.ObjectWrapper import AbstractWebObject
from RRPA.Modules.Web.Actions.ObjectActions import WebObjectActionizer


class STDWebButton(AbstractWebObject):

    def __init__(self, page, object_handle: WebElement, actions):
        self._page = page
        self._handle = object_handle
        self._actions = actions

    def click(self):
        WebObjectActionizer.click(self._actions, self._handle)

    def double_click(self):
        WebObjectActionizer.double_click(self._actions, self._handle)

    def hover(self):
        WebObjectActionizer.move_to_element(self._actions, self._handle)

    def get_instance(self):
        return self._handle
