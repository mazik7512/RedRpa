from RRPA.Modules.Core.Abstract.ObjectDetection.ObjectFinder import ObjectFinder
from RRPA.Modules.Core.Abstract.ObjectDetection.TemplateMatcher import TemplateMatcher
from RRPA.Modules.Core.Abstract.ObjectDetection.ObjectDetector import ObjectDetector
from RRPA.Modules.Core.General.WindowObjectsDescriptors.ObjectDescriptor import STDObjectDescriptor


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
            obj = STDObjectDescriptor(template, template_type)
            objects.append(obj)
        return objects


