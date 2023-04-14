from Modules.Core.Abstract.General.WindowObjectsDescriptors.ObjectDescriptor import AbstractObjectDescriptor
from Modules.Core.General.WindowObjectsDescriptors.TemplateDescriptor import STDTemplateDescriptor
from AppData.Configs.ObjectDetectionConfig import OBJECT_TYPES


class STDObjectDescriptor(AbstractObjectDescriptor):

    def __init__(self, template: STDTemplateDescriptor, _type: int):
        self._template_desc = template
        self._type = _type

    def get_object_typename(self) -> str:
        return OBJECT_TYPES[self._type]

    def get_object_type(self):
        return self._type

    def get_points(self):
        return self._template_desc.get_points()

    def __str__(self):
        temp = self.get_object_typename() + super().__str__()
        return temp
