from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDInfoSection(STDSection):

    def __init__(self):
        super().__init__()
        self.add("executable_standart", "STD")

    def deserialize(self):
        result = "@info_section:{"
        for key, data in self._table_data:
            result.join(key).join(":{").join(data).join("}").join(";")
        result.join("}")
        return result
