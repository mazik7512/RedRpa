from abc import ABC, abstractmethod


class AbstractWebObject(ABC):

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def double_click(self):
        pass

    @abstractmethod
    def hover(self):
        pass

