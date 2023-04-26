from abc import ABC, abstractmethod


class AbstractObjectDetector(ABC):
    @abstractmethod
    def detect_object_type(self, image) -> int:
        pass
