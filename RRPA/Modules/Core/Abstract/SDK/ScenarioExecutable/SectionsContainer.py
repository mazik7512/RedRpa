from abc import ABC, abstractmethod


class AbstractSectionContainer(ABC):

    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def get_section(self, section):
        pass

    @abstractmethod
    def add_section(self, section, section_data):
        pass

    @abstractmethod
    def get_keys(self):
        pass

    @abstractmethod
    def add_section_data(self, section, data):
        pass

    @abstractmethod
    def deserialize(self):
        pass
