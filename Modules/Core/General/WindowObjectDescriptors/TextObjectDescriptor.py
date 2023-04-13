from Modules.Core.General.WindowObjectDescriptors.ObjectDescriptor import ObjectDescriptor
from Modules.Core.General.WindowObjectDescriptors.TemplateDescriptor import TemplateDescriptor


class TextObjectDescriptor(ObjectDescriptor):
    def __init__(self, obj: ObjectDescriptor, text=""):
        super().__init__(TemplateDescriptor(obj.points), obj.type)
        self.text = text

    def get_text(self):
        return self.text

    def __str__(self):
        temp = super().__str__()[:-1] + ";text=" + self.text + "}"
        return temp
