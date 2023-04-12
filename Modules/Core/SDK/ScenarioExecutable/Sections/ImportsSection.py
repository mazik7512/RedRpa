from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDImportsSection(STDSection):

    def __init__(self):
        super().__init__()

    def deserialize(self):
        result = "@import_section:{"
        for key in self._table_data:
            result += key + ":{"
            for inner_key in self._table_data[key]:
                result += inner_key + ":{ " + self._table_data[key][inner_key] + " } " + ";"
            result += "}"
        result += "}"
        return result
