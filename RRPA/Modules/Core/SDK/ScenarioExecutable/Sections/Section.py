from abc import abstractmethod
from RRPA.Modules.Core.Abstract.SDK.ScenarioExecutable.Section import AbstractSection


class STDSection(AbstractSection):

    def __init__(self):
        self._table_data = {}

    def get_names(self):
        return self._table_data.keys()

    def get_data_by_name(self, name: str):
        return self._table_data[name]

    def get_section_data(self):
        result = ""
        for key in self._table_data:
            if self._table_data[key]:
                result += self._table_data[key] + "\n"
        return result

    def add(self, name, data_to_add):
        self._table_data[name] = data_to_add

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def serialize(self, data):
        pass

    def __str__(self):
        return str(self._table_data)
