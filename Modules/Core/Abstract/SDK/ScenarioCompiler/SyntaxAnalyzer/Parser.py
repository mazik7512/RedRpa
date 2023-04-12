from abc import ABC, abstractmethod


class AbstractSyntaxParser(ABC):

    @abstractmethod
    def set_tokens(self, tokens):
        pass

    @abstractmethod
    def generate_ast(self):
        pass

    @abstractmethod
    def _error(self, error_data):
        pass
