from abc import ABC, abstractmethod
from RRPA.Modules.Core.Abstract.OS.Tools.Window import AbstractWindow
from RRPA.Modules.Core.Abstract.OS.Tools.WindowManager import AbstractWindowManager
from RRPA.Modules.Core.Abstract.General.Tools.Tools import AbstractTools


class AbstractOSTools(AbstractTools):

    @staticmethod
    @abstractmethod
    def get_windows_list():
        pass

    @staticmethod
    @abstractmethod
    def get_window_by_name(win_name):
        pass

    @staticmethod
    @abstractmethod
    def create_window(win_desc) -> AbstractWindow:
        pass

    @staticmethod
    @abstractmethod
    def create_window_manager(window) -> AbstractWindowManager:
        pass

    @staticmethod
    @abstractmethod
    def get_tools_name():
        pass

    @staticmethod
    @abstractmethod
    def get_tools_import_path():
        pass

    @staticmethod
    @abstractmethod
    def get_window_name(win_desc):
        pass

    @staticmethod
    @abstractmethod
    def get_icon(win_desc):
        pass

    @staticmethod
    @abstractmethod
    def sleep(seconds):
        pass
