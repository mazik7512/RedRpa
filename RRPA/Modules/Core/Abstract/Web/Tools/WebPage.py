from abc import ABC, abstractmethod


class AbstractWebPage(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_page(self):
        pass

    @abstractmethod
    def set_page_handle(self, handle):
        pass

    @abstractmethod
    def get_page_handle(self):
        pass
