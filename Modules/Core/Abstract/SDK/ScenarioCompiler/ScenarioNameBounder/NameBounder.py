from abc import ABC, abstractmethod


class AbstractNameResolver(ABC):

    @abstractmethod
    def link_names(self):
        pass

    @abstractmethod
    def _error(self, error_data):
        pass
