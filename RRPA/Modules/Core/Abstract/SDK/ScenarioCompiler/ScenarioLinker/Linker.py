from abc import ABC, abstractmethod


class AbstractLinker(ABC):

    @abstractmethod
    def add_data_to_link(self, data_name, data):
        pass

    @abstractmethod
    def link(self):
        pass
