from abc import ABC, abstractmethod


class AbstractExecutableGenerator(ABC):

    @abstractmethod
    def generate_executable_sections(self):
        pass

    @abstractmethod
    def add_section(self, section_type: str, section_data):
        pass
