from abc import ABC, abstractmethod


class AbstractCryptographer(ABC):

    @abstractmethod
    def set_keys(self, *keys):
        pass

    @abstractmethod
    def generate_keys(self, key_type=None):
        pass

    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, data):
        pass
