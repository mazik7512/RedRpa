from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDExecSection(STDSection):

    def __init__(self):
        super().__init__()

    def deserialize(self):
        result = "@user_code_section:{ "
        for key in self._table_data:
            result += key + ":{ " + self._table_data[key] + " } " + ";"
        result += "}"
        return result
