from abc import ABC, abstractmethod


class AbstractTranslator(ABC):

    @abstractmethod
    def translate(self):
        pass
