from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDInfoSection(STDSection):

    def __init__(self):
        super().__init__()
        self.add("executable_standart", "STD")
        self.add("executable_version", "1.0")

    def deserialize(self):
        result = "@info_section:{"
        for key in self._table_data:
            result += key + ":{ " + self._table_data[key] + " } " + ";"
        result += "}"
        return result
