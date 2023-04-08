from Modules.Core.Abstract.ObjectDetection.ObjectFinder import ObjectFinder
from Modules.Core.Abstract.ObjectDetection.TemplateMatcher import TemplateMatcher
from Modules.Core.Abstract.ObjectDetection.ObjectDetector import ObjectDetector
from Modules.Core.Descriptors.ObjectDescriptor import ObjectDescriptor
import cv2


class ObjFinder(ObjectFinder):

    def __init__(self, matcher: TemplateMatcher, detector: ObjectDetector):
        super().__init__(matcher, detector)

    def find_objects(self, image) -> list:
        templates = self.matcher.find_templates(image)
        objects = []
        for template in templates:
            x, xw, y, yh = template.get_points()
            template_image = image[y:yh, x:xw]
            template_type = self.detector.detect_object_type(template_image)
            obj = ObjectDescriptor(template, template_type)
            objects.append(obj)
        return objects


