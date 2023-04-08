from abc import ABC, abstractmethod


class AbstractSyntaxNodeDescriptor(ABC):

    @abstractmethod
    def set_type(self, _type):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass
