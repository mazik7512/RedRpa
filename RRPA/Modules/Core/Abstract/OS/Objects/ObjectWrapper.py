from abc import ABC, abstractmethod


class AbstractWindowObject(ABC):

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def double_click(self):
        pass

    @abstractmethod
    def hover(self):
        pass

    @abstractmethod
    def r_click(self):
        pass

    @abstractmethod
    def double_r_click(self):
        pass

    @abstractmethod
    def move_cursor(self):
        pass


