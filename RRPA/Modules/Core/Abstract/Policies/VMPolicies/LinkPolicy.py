from abc import ABC, abstractmethod


class AbstractLinkPolicy(ABC):

    @staticmethod
    @abstractmethod
    def link_lib(import_data, lib_path):
        pass
