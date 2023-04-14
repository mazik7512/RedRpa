from Modules.Core.Abstract.General.WindowObjectsDescriptors.ObjectDescriptor import AbstractObjectDescriptor
from abc import ABC, abstractmethod


class AbstractTextObjectDescriptor(AbstractObjectDescriptor):

    @abstractmethod
    def get_text(self):
        pass
