from RRPA.Modules.Core.Abstract.General.WindowObjectsDescriptors.TextObjectDescriptor import AbstractTextObjectDescriptor
from RRPA.Modules.Core.General.WindowObjectsDescriptors.ObjectDescriptor import STDObjectDescriptor


class STDTextObjectDescriptor(AbstractTextObjectDescriptor):

    def __init__(self, obj: STDObjectDescriptor, text=""):
        self._obj_desc = obj
        self._text = text

    def get_text(self):
        return self._text

    def get_object_type(self):
        return self._obj_desc.get_object_type()

    def get_object_typename(self):
        return self._obj_desc.get_object_typename()

    def get_points(self):
        return self._obj_desc.get_points()

    def __str__(self):
        temp = super().__str__()[:-1] + ";text=" + self._text + "}"
        return temp
