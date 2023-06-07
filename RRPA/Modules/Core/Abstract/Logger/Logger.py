from abc import ABC, abstractmethod


class AbstractLogger(ABC):

    @staticmethod
    @abstractmethod
    def add_output_file(filepath: str, colorization=False, timing=True):
        pass

    @staticmethod
    @abstractmethod
    def error(*data, output_params):
        pass

    @staticmethod
    @abstractmethod
    def success(*data, output_params):
        pass

    @staticmethod
    @abstractmethod
    def warning(*data, output_params):
        pass

    @staticmethod
    @abstractmethod
    def info(*data, output_params):
        pass
