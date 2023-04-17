from abc import ABC, abstractmethod


class ObjectDetector(ABC):
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        self._load_model()

    @abstractmethod
    def _load_model(self) -> None:
        pass

    @abstractmethod
    def detect_object_type(self, image) -> int:
        pass
