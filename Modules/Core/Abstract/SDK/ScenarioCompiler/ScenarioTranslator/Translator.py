from abc import ABC, abstractmethod


class AbstractTranslator(ABC):

    @abstractmethod
    def translate(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass
