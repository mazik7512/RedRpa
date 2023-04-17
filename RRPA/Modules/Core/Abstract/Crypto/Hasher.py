from abc import ABC, abstractmethod


class AbstractHasher(ABC):

    @abstractmethod
    def hash_string(self, data):
        pass

    @abstractmethod
    def hash_array(self, data):
        pass

    @abstractmethod
    def hash_int(self, data):
        pass
