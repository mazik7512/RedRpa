from RRPA.Modules.Core.Abstract.OS.Tools.WindowManager import AbstractWindowManager
from RRPA.Modules.Core.Abstract.OS.Tools.Window import AbstractWindow
from RRPA.Modules.Windows.Actions.ObjectActions import ObjectActionizer
from RRPA.Modules.Windows.Tools.WinObjects.Button import STDButton
from RRPA.Modules.Windows.Tools.WinObjects.InputField import STDInputField
from RRPA.Modules.Windows.Actions.WindowActions import WindowActionizer
from RRPA.Modules.Core.General.Algorithms.StringComparator import STDStringComparator
import numpy as np
import cv2


class STDWindowManager(AbstractWindowManager):

    def __init__(self, window: AbstractWindow, object_scanners: dict = {}):
        super().__init__(window, object_scanners)

    @staticmethod
    def decode_image(bitmap):
        np_arr = np.frombuffer(bitmap.getbuffer(), np.uint8)
        img_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        return img_np

    def _add_objects(self, objects):
        for obj in objects:
            if obj.get_object_type() == 0:
                self.objects.append(STDButton(self.window, obj))
            elif obj.get_object_type() == 1:
                self.objects.append(STDInputField(self.window, obj))

    def os_scan_for_object(self):
        os_scanner = self._scanners['OS']
        _objects = os_scanner.find_objects(self.window)
        self._add_objects(_objects)

    def cv_scan_for_objects(self):
        cv_scanner = self._scanners['CV']
        self.focus()
        window_screen = STDWindowManager.decode_image(self.window.get_window_bitmap())
        _objects = cv_scanner.find_objects(window_screen)
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

    def click_on_points(self, x, y):
        ObjectActionizer.click_on_points(self.window.get_window(), x, y)

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
            if self.objects[i].get_text() and \
                    STDStringComparator.compare_strings(self.objects[i].get_text(), _text) > 80:
                return i
        return -1
