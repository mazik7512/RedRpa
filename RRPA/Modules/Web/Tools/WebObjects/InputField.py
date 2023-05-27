from selenium.webdriver.remote.webelement import WebElement
from RRPA.Modules.Core.Abstract.Web.Objects.ObjectWrapper import AbstractWebObject
from RRPA.Modules.Web.Actions.ObjectActions import WebObjectActionizer


class STDWebInputField(AbstractWebObject):

    def __init__(self, page, handle, actions):
        self._page = page
        self._handle = handle
        self._actions = actions

    def click(self):
        WebObjectActionizer.click(self._actions, self._handle)

    def double_click(self):
        WebObjectActionizer.double_click(self._actions, self._handle)

    def hover(self):
        WebObjectActionizer.move_to_element(self._actions, self._handle)

    def get_text(self):
        WebObjectActionizer.get_text(self._handle)

    def input_text(self, text):
        WebObjectActionizer.input_text(self._handle, text)
