from AppData.Configs.ObjectDetectionConfig import OBJECT_TYPES
from Modules.Core.General.WindowObjectDescriptors.TemplateDescriptor import TemplateDescriptor


class ObjectDescriptor(TemplateDescriptor):
    def __init__(self, template: TemplateDescriptor, _type: int):
        super().__init__(template.points)
        self.type = _type

    def get_object_typename(self) -> str:
        return OBJECT_TYPES[self.type]

    def get_object_type(self):
        return self.type

    def __str__(self):
        temp = self.get_object_typename() + super().__str__()
        return temp
