from RRPA.Modules.Core.Abstract.SDK.ScenarioAPI.WebAPI import AbstractWebAPI


class STDWebAPI(AbstractWebAPI):

    def __init__(self, web_tools):
        self._web_tools = web_tools

    def web_open(self, url: str, web_page_name: str):
        pass

    def web_click(self, page: str, web_object: str):
        pass

    def web_r_click(self, page: str, web_object: str):
        pass

    def web_double_click(self, page: str, web_object: str):
        pass

    def web_double_r_click(self, page: str, web_object: str):
        pass

    def web_input_text(self, page: str, web_object: str):
        pass

    def web_hover(self, page: str, web_object: str):
        pass

    def web_focus(self, page: str, web_object: str):
        pass

    def web_get_text(self, page: str, web_object: str):
        pass

    def web_close(self, page: str):
        pass
