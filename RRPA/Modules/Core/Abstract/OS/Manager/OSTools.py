from abc import ABC, abstractmethod
from RRPA.Modules.Core.Abstract.OS.Manager.Window import AbstractWindow
from RRPA.Modules.Core.Abstract.OS.Manager.WindowManager import AbstractWindowManager


class AbstractOSTools(ABC):

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
    def get_os_tools_name():
        pass

    @staticmethod
    @abstractmethod
    def get_os_tools_import_path():
        pass

    @staticmethod
    @abstractmethod
    def get_window_name(win_desc):
        pass

    @staticmethod
    @abstractmethod
    def get_icon(win_desc):
        pass
