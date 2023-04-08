from abc import ABC, abstractmethod


class AbstractScenarioAPI(ABC):

    @abstractmethod
    def CV_scan(self, window):
        pass

    @abstractmethod
    def OS_scan(self,window):
        pass

    @abstractmethod
    def click_on_object(self, window, _object):
        pass

    @abstractmethod
    def hover_on_object(self, window, _object):
        pass

    @abstractmethod
    def double_click_on_object(self, window, _object):
        pass

    @abstractmethod
    def r_click_on_object(self, window, _object):
        pass

    @abstractmethod
    def double_r_click_on_object(self, window, _object):
        pass

    @abstractmethod
    def move_to_object(self, window, _object):
        pass

    @abstractmethod
    def move_window(self, window, points):
        pass

    @abstractmethod
    def close_window(self, window):
        pass

    @abstractmethod
    def focus_window(self, window):
        pass

    @abstractmethod
    def get_text(self, window, _object):
        pass

    @abstractmethod
    def input_text(self, window, _object, text):
        pass
