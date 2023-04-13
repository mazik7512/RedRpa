from Modules.Core.Abstract.OS.Manager.ObjectWrapper import WindowObject
from Modules.Core.General.WindowObjectDescriptors.ObjectDescriptor import ObjectDescriptor
from Modules.Windows.Actions.ObjectActions import ObjectActionizer


class STDInputField(WindowObject):

    def __init__(self, hwnd, object_desc: ObjectDescriptor):
        super().__init__(hwnd, object_desc)

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
        ObjectActionizer.get_text(self._window.get_window(), self._object)

    def input_text(self, text):
        ObjectActionizer.input_text(self._window.get_window(), self._object, text)
