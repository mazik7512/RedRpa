from abc import ABC, abstractmethod


class AbstractImportPolicy(ABC):

    @staticmethod
    @abstractmethod
    def generate_import(import_name):
        pass
