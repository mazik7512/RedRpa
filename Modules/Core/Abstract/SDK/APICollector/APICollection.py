from abc import ABC, abstractmethod


class AbstractAPICollection(ABC):

    @abstractmethod
    def get_methods(self):
        pass

    @abstractmethod
    def add_method(self, method_name):
        pass

    @abstractmethod
    def get_api_name(self):
        pass

    @abstractmethod
    def get_api_filename(self):
        pass

    @abstractmethod
    def get_class_instance(self):
        pass
