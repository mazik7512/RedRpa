from Modules.Core.Abstract.General.DataStructures.WorkResult import AbstractWorkResult


class STDWorkResult(AbstractWorkResult):

    def __init__(self):
        self._data = None
        self._errors = None

    def push(self, data):
        self._data = data

    def push_errors(self, errors):
        self._errors = errors

    def deserialize(self):
        return "errors=" + str(self._errors) + "\ndata=" + str(self._data)

    def get_errors(self):
        return self._errors

    def get_data(self):
        return self._data

    def __str__(self):
        return self.deserialize()
