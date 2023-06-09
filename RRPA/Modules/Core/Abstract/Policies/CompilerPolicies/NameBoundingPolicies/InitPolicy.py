from abc import ABC, abstractmethod


class AbstractInitPolicy(ABC):

    @staticmethod
    @abstractmethod
    def generate_init_api(*args):
        pass

    @staticmethod
    @abstractmethod
    def generate_init_tools(*args):
        pass
