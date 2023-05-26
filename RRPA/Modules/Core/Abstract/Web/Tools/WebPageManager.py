from abc import ABC, abstractmethod


class AbstractWebPageManager(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def object_action(self, web_object, web_action, *params):
        pass
