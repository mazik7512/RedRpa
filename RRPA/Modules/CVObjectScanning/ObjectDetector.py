from keras.models import load_model
from RRPA.Modules.Core.Abstract.ObjectScanning.ObjectDetector import AbstractObjectDetector
import cv2
import numpy as np


class STDCVObjectDetector(AbstractObjectDetector):
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        self._load_model()
        self.img_width = 96
        self.img_height = 96

    def _load_model(self) -> None:
        self.model = load_model(self.model_path)

    def _preprocess_image(self, image):
        image = cv2.resize(image, (self.img_height, self.img_width))
        image = np.array(image) / 255
        image = image.reshape(-1, self.img_height, self.img_width, 3)
        return image

    def detect_object_type(self, image) -> int:
        preprocessed_image = self._preprocess_image(image)
        res = self.model.predict(preprocessed_image)
        res = np.argmax(res)
        return res

