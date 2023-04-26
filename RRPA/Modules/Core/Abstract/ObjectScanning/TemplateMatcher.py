from abc import ABC, abstractmethod, abstractproperty


class AbstractTemplateMatcher(ABC):

    @abstractmethod
    def find_templates(self, image) -> list:
        pass
