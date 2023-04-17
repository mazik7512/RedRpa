from abc import abstractmethod
from RRPA.Modules.Core.Abstract.General.WindowObjectsDescriptors.TemplateDescriptor import AbstractTemplateDescriptor


class AbstractObjectDescriptor(AbstractTemplateDescriptor):

    @abstractmethod
    def get_object_type(self):
        pass

    @abstractmethod
    def get_object_typename(self):
        pass
