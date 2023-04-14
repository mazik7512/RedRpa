from abc import ABC, abstractmethod


class AbstractTemplateDescriptor(ABC):

    @abstractmethod
    def get_points(self):
        pass
