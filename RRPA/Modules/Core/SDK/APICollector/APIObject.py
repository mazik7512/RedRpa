from RRPA.Modules.Core.Abstract.SDK.APICollector.APIObject import AbstractAPIObject


class STDAPIObject(AbstractAPIObject):

    def __init__(self, obj_name, obj_data):
        self._name = obj_name
        self._data = obj_data

    def get_object_name(self):
        return self._name

    def get_object_data(self):
        return self._data

    def __str__(self):
        return self._name

