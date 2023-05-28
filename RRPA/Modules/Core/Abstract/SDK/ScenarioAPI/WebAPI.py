from abc import ABC, abstractmethod


class AbstractWebAPI(ABC):

    @abstractmethod
    def web_open(self, url: str, web_page_name: str):
        pass

    @abstractmethod
    def web_scan(self, page: str):
        pass

    @abstractmethod
    def web_click(self, page: str, web_object: str):
        pass

    @abstractmethod
    def web_double_click(self, page: str, web_object: str):
        pass

    @abstractmethod
    def web_input_text(self, page: str, web_object: str, text: str):
        pass

    @abstractmethod
    def web_hover(self, page: str, web_object: str):
        pass

    @abstractmethod
    def web_get_text(self, page: str, web_object: str):
        pass

    @abstractmethod
    def web_close(self, page: str):
        pass

    @abstractmethod
    def web_click_and_hold(self, page: str, web_object: str):
        pass

    @abstractmethod
    def web_release(self, page: str, web_object: str):
        pass
