from abc import ABC, abstractmethod


class AbstractExecutable(ABC):

    @abstractmethod
    def serialize(self, data: str):
        pass

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def get_sections(self):
        pass
