from RRPA.Modules.Core.General.WindowObjectsDescriptors.ObjectDescriptor import STDObjectDescriptor
from RRPA.Modules.Core.Abstract.OS.Manager.Window import AbstractWindow


class WindowObject:
    def __init__(self, window: AbstractWindow, object_desc: STDObjectDescriptor):
        self._object = object_desc
        self._window = window


