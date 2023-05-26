from RRPA.Modules.Core.Abstract.Web.Tools.WebPageManager import AbstractWebPageManager
from RRPA.Modules.Web.Tools.WebPage import STDWebPage


class STDWebPageManager(AbstractWebPageManager):

    def __init__(self, web_url, web_name):
        self._w_page = STDWebPage(web_url, web_name)

    def open(self):
        pass

    def close(self):
        pass

    def object_action(self, web_object, web_action, *params):
        pass
