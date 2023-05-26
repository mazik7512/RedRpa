from RRPA.Modules.Core.Abstract.Web.Tools.WebPage import AbstractWebPage


class STDWebPage(AbstractWebPage):

    def __init__(self, web_url, web_name):
        self._url = web_url
        self._name = web_name

    def get_name(self):
        return self._name

    def get_page(self):
        return self._url

