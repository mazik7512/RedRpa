from abc import ABC, abstractmethod


class AbstractVirtualMachine(ABC):

    @abstractmethod
    def execute(self, file):
        pass
    