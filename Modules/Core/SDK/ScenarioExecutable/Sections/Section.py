from abc import abstractmethod
from Modules.Core.Abstract.SDK.ScenarioExecutable.Section import AbstractSection


class STDSection(AbstractSection):

    def __init__(self):
        self._table_data = {}

    def get_data_by_name(self, name: str):
        return self._table_data[name]

    def add(self, name, data_to_add):
        self._table_data[name] = data_to_add

    @abstractmethod
    def deserialize(self):
        pass

    def __str__(self):
        return str(self._table_data)
