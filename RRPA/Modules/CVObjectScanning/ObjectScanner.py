from RRPA.Modules.Core.Abstract.ObjectScanning.ObjectScanner import AbstractObjectScanner
from RRPA.Modules.Core.Abstract.ObjectScanning.TemplateMatcher import AbstractTemplateMatcher
from RRPA.Modules.Core.Abstract.ObjectScanning.ObjectDetector import AbstractObjectDetector
from RRPA.Modules.Core.General.WindowObjectsDescriptors.ObjectDescriptor import STDObjectDescriptor


class STDCVObjectScanner(AbstractObjectScanner):

    def __init__(self, matcher: AbstractTemplateMatcher, detector: AbstractObjectDetector):
        self._matcher = matcher
        self._detector = detector
        self._name = "CV"

    def find_objects(self, image) -> list:
        templates = self._matcher.find_templates(image)
        objects = []
        for template in templates:
            x, xw, y, yh = template.get_points()
            template_image = image[y:yh, x:xw]
            template_type = self._detector.detect_object_type(template_image)
            obj = STDObjectDescriptor(template, template_type)
            objects.append(obj)
        return objects

    def get_object_finder_name(self):
        return self._name

