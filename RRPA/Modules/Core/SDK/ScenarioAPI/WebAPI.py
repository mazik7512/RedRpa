from RRPA.Modules.Core.Abstract.SDK.ScenarioAPI.WebAPI import AbstractWebAPI
from RRPA.Modules.Core.Abstract.Web.Tools.WebTools import AbstractWebTools


class STDWebAPI(AbstractWebAPI):

    def __init__(self, tools):
        self._web_tools = tools['web']
        self._PAGES_POOL = {}

    def web_scan(self, page: str):
        self._PAGES_POOL[page].scan_for_objects()

    def web_open(self, url: str, web_page_name: str):
        self._PAGES_POOL[web_page_name] = self._web_tools.create_web_page_manager(url, web_page_name)
        self._PAGES_POOL[web_page_name].open()

    def web_click(self, page: str, web_object: str):
        self._PAGES_POOL[page].object_action(web_object, 'click')

    def web_double_click(self, page: str, web_object: str):
        self._PAGES_POOL[page].object_action(web_object, 'double_click')

    def web_input_text(self, page: str, web_object: str, text: str):
        self._PAGES_POOL[page].object_action(web_object, 'input_text', text)

    def web_hover(self, page: str, web_object: str):
        self._PAGES_POOL[page].object_action(web_object, 'move_to_element')

    def web_get_text(self, page: str, web_object: str):
        return self._PAGES_POOL[page].object_action(web_object, 'get_text')

    def web_click_and_hold(self, page: str, web_object: str):
        self._PAGES_POOL[page].object_action(web_object, 'click_and_hold')

    def web_release(self, page: str, web_object: str):
        self._PAGES_POOL[page].object_action(web_object, 'release')

    def web_close(self, page: str):
        self._PAGES_POOL[page].close()
