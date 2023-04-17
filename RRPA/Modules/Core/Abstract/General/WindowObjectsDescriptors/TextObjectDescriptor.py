from RRPA.Modules.Core.Abstract.General.WindowObjectsDescriptors.ObjectDescriptor import AbstractObjectDescriptor
from abc import abstractmethod


class AbstractTextObjectDescriptor(AbstractObjectDescriptor):

    @abstractmethod
    def get_text(self):
        pass
