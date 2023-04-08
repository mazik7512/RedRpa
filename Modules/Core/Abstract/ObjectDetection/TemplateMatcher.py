from abc import ABC, abstractmethod, abstractproperty


class TemplateMatcher(ABC):

    @abstractmethod
    def find_templates(self, image) -> list:
        pass
