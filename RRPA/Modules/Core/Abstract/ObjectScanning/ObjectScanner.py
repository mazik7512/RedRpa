from abc import ABC, abstractmethod
from RRPA.Modules.Core.Abstract.ObjectScanning.TemplateMatcher import AbstractTemplateMatcher
from RRPA.Modules.Core.Abstract.ObjectScanning.ObjectDetector import AbstractObjectDetector


class AbstractObjectScanner(ABC):

    @abstractmethod
    def find_objects(self, image) -> list:
        pass

    @abstractmethod
    def get_object_finder_name(self):
        pass
