from abc import ABC, abstractmethod
from Modules.Core.Abstract.OS.Manager.Window import AbstractWindow


class AbstractWindowManager(ABC):
    def __init__(self, window: AbstractWindow, cv_object_scanner=None, os_object_scanner=None):
        self.objects = []
        self.window = window
        self.cv_object_scanner = cv_object_scanner
        self.os_object_scanner = os_object_scanner

    @abstractmethod
    def cv_scan_for_objects(self):
        pass

    @abstractmethod
    def os_scan_for_object(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def resize(self, width, height):
        pass

    @abstractmethod
    def focus(self):
        pass

    @abstractmethod
    def object_action(self, _object_id, _action, *params):
        pass

    @abstractmethod
    def find_object(self, _object):
        pass

    @abstractmethod
    def find_object_by_type(self, _type):
        pass

    @abstractmethod
    def find_object_by_text(self, _text):
        pass
