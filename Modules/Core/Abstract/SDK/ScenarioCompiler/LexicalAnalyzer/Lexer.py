from abc import ABC, abstractmethod


class AbstractLexer(ABC):

    @abstractmethod
    def get_next_token(self):
        pass

    @abstractmethod
    def get_token_list(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass
