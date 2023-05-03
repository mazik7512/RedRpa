from abc import ABC, abstractmethod


class AbstractSemanticAnalyzer(ABC):

    @abstractmethod
    def set_ast(self, ast):
        pass

    @abstractmethod
    def set_stdlib(self, stdlib):
        pass

    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod
    def _error(self, error_data):
        pass
