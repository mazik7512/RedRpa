from abc import abstractmethod
from RRPA.Modules.Core.Abstract.General.Tools.Tools import AbstractTools


class AbstractWebTools(AbstractTools):

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
    def create_web_page_manager(url, wp_name):
        pass

    @staticmethod
    @abstractmethod
    def close_web_page(web_page):
        pass

    @staticmethod
    @abstractmethod
    def get_icon(web_page):
        pass

    @staticmethod
    @abstractmethod
    def find_web_page(web_page_name):
        pass

    @staticmethod
    @abstractmethod
    def get_pages():
        pass
