from abc import ABC, abstractmethod


class AbstractErrorProcessingPolicy(ABC):

    @staticmethod
    @abstractmethod
    def process_errors(errors):
        pass
