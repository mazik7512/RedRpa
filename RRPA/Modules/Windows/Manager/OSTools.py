import inspect
import struct
import win32ui
import pywintypes
import win32con
from PIL import Image

from RRPA.Modules.CVObjectScanning.ObjectScannerGenerator import STDCVObjectScannerGenerator
from RRPA.Modules.Core.Abstract.OS.Manager.OSTools import AbstractOSTools
from RRPA.Modules.Windows.Manager.Window import STDWindow
from RRPA.Modules.Windows.Manager.WindowManager import STDWindowManager
from win32 import win32gui
from win32 import win32api


class STDOSTools(AbstractOSTools):

    scanners = {'CV': STDCVObjectScannerGenerator.generate_cv_object_scanner()}

    @staticmethod
    def create_window(win_desc):
        window = STDWindow(win_desc)
        return window

    @staticmethod
    def create_window_manager(window):
        window_manager = STDWindowManager(window, STDOSTools.scanners)
        return window_manager

    @staticmethod
    def get_windows_list():
        windows_list = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windows_list)
        return windows_list

    @staticmethod
    def get_window_by_name(win_name):
        return win32gui.FindWindow(None, win_name)

    @staticmethod
    def get_window_name(win_desc):
        return win32gui.GetWindowText(win_desc)

    @staticmethod
    def get_os_tools_name():
        return STDOSTools.__name__

    @staticmethod
    def get_os_tools_import_path():
        return "RRPA.Modules.Windows.Manager.OSTools"

    @staticmethod
    def get_icon(win_desc):
        handle = win32gui.FindWindow(None, "Steam")
        test = win32gui.DefWindowProc(handle, win32con.WM_GETICON, win32con.ICON_SMALL, 0)
        print("defwindowproc=", test)
        test_class_long = win32gui.GetClassLong(handle, win32con.GCL_HICON)
        print("class_log=", test_class_long)
        res = win32gui.CopyIcon(test_class_long)
        print("res=", res)
        icon_info = win32gui.GetIconInfo(res)
        print(icon_info)
        icon = win32gui.GetObject(icon_info[3])
        print(icon)
        print(dir(icon))
        #wDC = win32gui.GetWindowDC(None)
        #dcObj = win32ui.CreateDCFromHandle(res)
        #cDC = dcObj.CreateCompatibleDC()
        #dataBitMap = win32ui.CreateBitmap()
        #dataBitMap.CreateCompatibleBitmap(dcObj, 16, 16)
        #cDC.SelectObject(dataBitMap)
        #cDC.BitBlt((0, 0), (16, 16), dcObj, (0, 0), win32con.SRCCOPY)
        #win32gui.DrawIconEx(wDC, 100, 100, res, 16, 16, 0, None, win32con.DI_IMAGE)
        #bmpinfo = dataBitMap.GetInfo()
        #bmpstr = dataBitMap.GetBitmapBits(True)
        #im = Image.frombuffer(
        #    'RGB',
        #    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        #    bmpstr, 'raw', 'BGRX', 0, 1)
        #im.show("test")
        #dcObj.DeleteDC()
        #cDC.DeleteDC()
        #win32gui.ReleaseDC(handle, wDC)
        #icon_info = win32gui.GetIconInfo(res)
        #print(icon_info)
        #icon_object = win32gui.GetObject(icon_info[3])
        #print(icon_object)
