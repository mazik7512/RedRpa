from abc import ABC, abstractmethod


class AbstractWindow(ABC):
    def __init__(self, window):
        self._window = window

    @abstractmethod
    def get_window(self):
        pass

    @abstractmethod
    def get_window_title(self):
        pass

    @abstractmethod
    def get_window_bitmap(self):
        pass

    @abstractmethod
    def get_window_points(self):
        pass

    @abstractmethod
    def get_window_width(self):
        pass

    @abstractmethod
    def get_window_height(self):
        pass
