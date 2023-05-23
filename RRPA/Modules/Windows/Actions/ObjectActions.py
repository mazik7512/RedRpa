from typing import Tuple
from RRPA.Modules.Core.General.WindowObjectsDescriptors.TemplateDescriptor import STDTemplateDescriptor
from RRPA.Modules.Core.General.WindowObjectsDescriptors.TextObjectDescriptor import STDTextObjectDescriptor
import win32con
import win32gui
import win32api


class ObjectActionizer:

    @staticmethod
    def click(hwnd: int, object_desc: STDTemplateDescriptor):
        x, y = ActionHelper.get_object_center(hwnd, object_desc)
        ObjectActionizer.move(hwnd, object_desc)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    @staticmethod
    def double_click(hwnd: int, object_desc: STDTemplateDescriptor):
        ObjectActionizer.click(hwnd, object_desc)
        ObjectActionizer.click(hwnd, object_desc)

    @staticmethod
    def r_click(hwnd: int, object_desc: STDTemplateDescriptor):
        x, y = ActionHelper.get_object_center(hwnd, object_desc)
        ObjectActionizer.move(hwnd, object_desc)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    @staticmethod
    def double_r_click(hwnd: int, object_desc: STDTemplateDescriptor):
        ObjectActionizer.click(hwnd, object_desc)
        ObjectActionizer.click(hwnd, object_desc)

    @staticmethod
    def hover(hwnd: int, object_desc: STDTemplateDescriptor):
        x, y = ActionHelper.get_object_center(hwnd, object_desc)
        lParam = win32api.MAKELONG(x, y)
        win32gui.PostMessage(hwnd, win32con.WM_MOUSEHOVER, 0, lParam)

    @staticmethod
    def move(hwnd: int, object_desc):
        x, y = ActionHelper.get_object_center(hwnd, object_desc)
        win32api.SetCursorPos((x, y))

    @staticmethod
    def get_text(hwnd: int, object_desc: STDTextObjectDescriptor):
        return object_desc.get_text()

    @staticmethod
    def input_text(hwnd: int, object_desc: STDTextObjectDescriptor, text):
        ObjectActionizer.click(hwnd, object_desc)
        for letter in text:
            win32api.keybd_event(ord(letter), 0, win32con.WM_KEYDOWN, 0)
            win32api.keybd_event(ord(letter), 0, win32con.WM_KEYUP, 0)


class ActionHelper:

    @staticmethod
    def get_object_center(hwnd: int, object_desc: STDTemplateDescriptor) -> Tuple[int, int]:
        x = object_desc.get_points()[0] + ((object_desc.get_points()[1] - object_desc.get_points()[0]) // 2)
        y = object_desc.get_points()[2] + ((object_desc.get_points()[3] - object_desc.get_points()[2]) // 2)
        x, y = win32gui.ClientToScreen(hwnd, (x, y))
        return x, y
