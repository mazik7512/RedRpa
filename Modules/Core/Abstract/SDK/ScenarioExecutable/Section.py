from abc import ABC, abstractmethod


class AbstractSection(ABC):

    @abstractmethod
    def get_section_data(self):
        pass

    @abstractmethod
    def add(self, name, data_to_add):
        pass

    @abstractmethod
    def deserialize(self):
        pass

    def get_data_by_name(self, name: str):
        pass
