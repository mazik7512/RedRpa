from abc import abstractmethod
from RRPA.Modules.Core.Abstract.General.Tools.Tools import AbstractTools
from RRPA.Modules.Core.Abstract.Web.Tools.WebPageManager import AbstractWebPageManager


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
    def create_web_page_manager(url, wp_name) -> AbstractWebPageManager:
        pass

    @staticmethod
    @abstractmethod
    def get_icon(web_page):
        pass


