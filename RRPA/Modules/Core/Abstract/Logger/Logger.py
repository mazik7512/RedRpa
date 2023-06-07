from abc import ABC, abstractmethod


class AbstractLogger(ABC):

    @staticmethod
    @abstractmethod
    def add_output_file(filepath: str, colorization=False, timing=True):
        pass

    @staticmethod
    @abstractmethod
    def error(data, *args):
        pass

    @staticmethod
    @abstractmethod
    def success(data, *args):
        pass

    @staticmethod
    @abstractmethod
    def warning(data, *args):
        pass

    @staticmethod
    @abstractmethod
    def info(data, *args):
        pass
