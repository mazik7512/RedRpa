from RRPA.Modules.Core.Abstract.OS.Manager.OSTools import AbstractOSTools
from RRPA.Modules.Windows.Manager.Window import STDWindow
from RRPA.Modules.Windows.Manager.WindowManager import STDWindowManager
from win32 import win32gui


class STDOSTools(AbstractOSTools):

    @staticmethod
    def create_window(win_desc):
        window = STDWindow(win_desc)
        return window

    @staticmethod
    def create_window_manager(window):
        window_manager = STDWindowManager(window)
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
    def get_os_tools_name():
        return STDOSTools.__name__

    @staticmethod
    def get_os_tools_import_path():
        return "RRPA.Modules.Windows.Manager.OSTools"
