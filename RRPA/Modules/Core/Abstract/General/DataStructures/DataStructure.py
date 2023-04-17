from abc import ABC, abstractmethod


class AbstractDataStructure(ABC):

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def deserialize(self):
        pass
    