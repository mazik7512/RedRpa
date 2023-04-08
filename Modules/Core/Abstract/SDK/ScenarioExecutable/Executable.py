from abc import ABC, abstractmethod


class AbstractExecutable(ABC):

    @abstractmethod
    def serialization(self):
        pass

    @abstractmethod
    def deserialization(self) -> bytes:
        pass
