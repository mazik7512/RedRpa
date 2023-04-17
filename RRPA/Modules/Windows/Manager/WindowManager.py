from RRPA.Modules.Core.Abstract.OS.Manager.WindowManager import AbstractWindowManager
from RRPA.Modules.Core.Abstract.OS.Manager.Window import AbstractWindow
from RRPA.Modules.Windows.Manager.WinObjects.Button import STDButton
from RRPA.Modules.Windows.Manager.WinObjects.InputField import STDInputField
from RRPA.Modules.Windows.Actions.WindowActions import WindowActionizer
import numpy as np
import cv2


class STDWindowManager(AbstractWindowManager):

    def __init__(self, window: AbstractWindow, object_scanner=None, os_object_scanner=None):
        super().__init__(window, object_scanner, os_object_scanner)

    @staticmethod
    def decode_image(bitmap):
        np_arr = np.frombuffer(bitmap.getbuffer(), np.uint8)
        img_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        return img_np

    def _add_objects(self, objects):
        for obj in objects:
            if obj._type == 0:
                self.objects.append(STDButton(self.window.get_window(), obj))
            elif obj._type == 1:
                self.objects.append(STDInputField(self.window.get_window(), obj))

    def os_scan_for_object(self):
        _objects = self.os_object_scanner.find_objects(self.window)
        self._add_objects(_objects)

    def cv_scan_for_objects(self):
        window_screen = STDWindowManager.decode_image(self.window.get_window_bitmap())
        _objects = self.cv_object_scanner.find_objects(window_screen)
        self._add_objects(_objects)

    def open(self):
        pass

    def close(self):
        WindowActionizer.close(self.window.get_window())

    def move(self, x, y):
        width = self.window.get_window_width()
        height = self.window.get_window_height()
        WindowActionizer.move(self.window.get_window(), x, y, width, height, False)

    def resize(self, width, height):
        points = self.window.get_window_points()
        x = points[0]
        y = points[1]
        WindowActionizer.move(self.window.get_window(), x, y, width, height, True)

    def focus(self):
        WindowActionizer.focus(self.window.get_window())

    def object_action(self, _object_id, _action, *params):
        object_action = getattr(self.objects[_object_id], _action)
        object_action(*params)

    def find_object(self, _object):
        if type(_object) == str:
            return self.find_object_by_text(_object)
        elif type(_object) == int:
            return self.find_object_by_type(_object)
        else:
            return -1

    def find_object_by_type(self, _type):
        for i in range(len(self.objects)):
            if self.objects[i].get_type() == _type:
                return i

    def find_object_by_text(self, _text):
        for i in range(len(self.objects)):
            if self.objects[i].get_text() == _text:
                return i
