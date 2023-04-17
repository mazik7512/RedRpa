from abc import ABC, abstractmethod
from RRPA.Modules.Core.Abstract.ObjectDetection.TemplateMatcher import TemplateMatcher
from RRPA.Modules.Core.Abstract.ObjectDetection.ObjectDetector import ObjectDetector


class ObjectFinder(ABC):

    def __init__(self, matcher: TemplateMatcher, detector: ObjectDetector):
        self.matcher = matcher
        self.detector = detector

    @abstractmethod
    def find_objects(self, image) -> list:
        pass
