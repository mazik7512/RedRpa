from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDImportsSection(STDSection):

    def __init__(self):
        super().__init__()

    def serialize(self, data):
        self._table_data = data

    def deserialize(self):
        return self._table_data
