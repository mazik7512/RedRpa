from abc import ABC, abstractmethod


class AbstractTools(ABC):

    @staticmethod
    @abstractmethod
    def get_tools_name():
        pass

    @staticmethod
    @abstractmethod
    def get_tools_import_path():
        pass
