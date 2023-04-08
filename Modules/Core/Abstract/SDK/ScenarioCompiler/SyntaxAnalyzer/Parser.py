from abc import ABC, abstractmethod


class AbstractSyntaxParser(ABC):

    @abstractmethod
    def generate_ast(self):
        pass

    @abstractmethod
    def _error(self, error_data):
        pass
