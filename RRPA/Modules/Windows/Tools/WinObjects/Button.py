from RRPA.Modules.Core.Abstract.OS.Objects.ObjectWrapper import AbstractWindowObject
from RRPA.Modules.Core.General.WindowObjectsDescriptors.ObjectDescriptor import STDObjectDescriptor
from RRPA.Modules.Windows.Actions.ObjectActions import ObjectActionizer


class STDButton(AbstractWindowObject):

    def __init__(self, hwnd, object_desc: STDObjectDescriptor):
        self._window = hwnd
        self._object = object_desc

    def click(self):
        ObjectActionizer.click(self._window.get_window(), self._object)

    def double_click(self):
        ObjectActionizer.double_click(self._window.get_window(), self._object)

    def hover(self):
        ObjectActionizer.hover(self._window.get_window(), self._object)

    def r_click(self):
        ObjectActionizer.r_click(self._window.get_window(), self._object)

    def double_r_click(self):
        ObjectActionizer.double_r_click(self._window.get_window(), self._object)

    def move_cursor(self):
        ObjectActionizer.move(self._window.get_window(), self._object)

    def get_text(self):
        return ObjectActionizer.get_text(self._window.get_window(), self._object)
