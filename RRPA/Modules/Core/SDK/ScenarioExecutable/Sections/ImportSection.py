from RRPA.Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDImportSection(STDSection):

    def __init__(self):
        super().__init__()

    def serialize(self, data):
        self._table_data = data

    def deserialize(self):
        return self._table_data

    def get_section_data(self):
        result = ""
        for key in self._table_data:
            for inner_key in self._table_data[key]:
                result += self._table_data[key][inner_key] + "\n"
        result += "\n\n"
        return result
