from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDInfoSection(STDSection):

    def __init__(self):
        super().__init__()
        self.add("executable_standart", "STD")
        self.add("executable_version", "1.0")

    def serialize(self, data):
        self._table_data = data

    def deserialize(self):
        return self._table_data
