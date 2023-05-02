import pywintypes
import win32con

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
        print(handle)
        #test = win32gui.SendMessage(handle, win32con.WM_GETICON, win32con.ICON_SMALL)
        test = win32gui.DefWindowProc(handle, win32con.WM_GETICON, win32con.ICON_SMALL, 1)
        print(test)
        icon = win32gui.LoadImage(handle, test % 65535, win32con.IMAGE_ICON, 0, 0, win32con.LR_DEFAULTSIZE)

        print(icon)

        #module = win32api.GetModuleFileName("TelegramDesktop")
        try:
            icon_names = win32api.EnumResourceNames(handle, win32con.RT_STRING)
            print(icon_names)
        except pywintypes.error as e:
            print(e)
            return
        for icon_name in icon_names:
            rec = win32api.LoadResource(win_desc, win32con.RT_ICON, icon_name)
            hicon = win32gui.CreateIconFromResource(rec, True)
            info = win32gui.GetIconInfo(hicon)
            bminfo = win32gui.GetObject(info[3])
            print("%2d: 0x%08X -> %d %d " % (icon_name, hicon, bminfo.bmWidth, bminfo.bmHeight))
