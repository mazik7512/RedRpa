from abc import ABC, abstractmethod


class AbstractUtils(ABC):

    @staticmethod
    @abstractmethod
    def parse_protocol(raw_data):
        pass

    @staticmethod
    @abstractmethod
    def hash_data(raw_data):
        pass
