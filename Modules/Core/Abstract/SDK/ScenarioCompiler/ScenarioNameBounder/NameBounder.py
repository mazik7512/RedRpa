from abc import ABC, abstractmethod


class AbstractNameBounder(ABC):

    @abstractmethod
    def link_names(self):
        pass

    @abstractmethod
    def _error(self, error_data):
        pass

    @abstractmethod
    def set_ast(self, ast):
        pass

    @abstractmethod
    def set_apis(self, apis):
        pass
