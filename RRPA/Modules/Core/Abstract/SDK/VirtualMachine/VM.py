from abc import ABC, abstractmethod


class AbstractVirtualMachine(ABC):

    @abstractmethod
    def execute(self, file):
        pass

    @abstractmethod
    def _error(self, error_data):
        pass
