from RRPA.Modules.Core.Abstract.SDK.ScenarioAPI.CoreAPI import AbstractScenarioAPI
from RRPA.Modules.Core.Abstract.OS.Manager.OSTools import AbstractOSTools


class STDScenarioAPI(AbstractScenarioAPI):

    def __init__(self, win_helper: AbstractOSTools):
        self._WINDOWS_POOL = {}
        self._win_helper = win_helper

    def _create_window_manager_object(self, win_name):
        win_desciptor = self._win_helper.get_window_by_name(win_name)
        window = self._win_helper.create_window(win_desciptor)
        window_manager = self._win_helper.create_window_manager(window)
        self._WINDOWS_POOL[win_desciptor] = window_manager
        return self._WINDOWS_POOL[win_desciptor]

    def _find_window_in_pool(self, win_name):
        win_descriptor = self._win_helper.get_window_by_name(win_name)
        return self._WINDOWS_POOL[win_descriptor]

    def CV_scan(self, window: str):
        wnd = self._create_window_manager_object(window)
        wnd.cv_scan_for_objects()

    def OS_scan(self, window: str):
        wnd = self._create_window_manager_object(window)
        wnd.os_scan_for_objects()

    def click_on_object(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "click")

    def hover_on_object(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "hover")

    def double_click_on_object(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "double_click")

    def r_click_on_object(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "r_click")

    def double_r_click_on_object(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "double_r_click")

    def move_to_object(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "move")

    def get_text(self, window: str, _object: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "get_text")

    def input_text(self, window: str, _object: str, text: str):
        wnd = self._find_window_in_pool(window)
        _obj = wnd.find_object(_object)
        wnd.object_action(_obj, "input_text", text)

    def move_window(self, window: str, x: int, y: int):
        wnd = self._find_window_in_pool(window)
        wnd.move(x, y)

    def close_window(self, window: str):
        wnd = self._find_window_in_pool(window)
        wnd.close()

    def focus_window(self, window: str):
        wnd = self._find_window_in_pool(window)
        wnd.focus()
