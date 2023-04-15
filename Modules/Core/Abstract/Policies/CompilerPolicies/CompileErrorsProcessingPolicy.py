from abc import ABC, abstractmethod


class AbstractCompileErrorsProcessingPolicy(ABC):

    @staticmethod
    @abstractmethod
    def process_errors(errors_type, errors):
        pass
